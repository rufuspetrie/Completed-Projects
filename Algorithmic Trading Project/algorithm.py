"""
Amin and Rufus' Trade Algorithm
Note: we borrowed a good chunk of code from the pipeline tutorial and the momentum sample algorithm
"""

from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline, CustomFactor
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import SimpleMovingAverage, AverageDollarVolume, RollingPearsonOfReturns
from quantopian.pipeline.data import morningstar
from quantopian.pipeline.filters.morningstar import IsPrimaryShare
from quantopian.pipeline.filters.morningstar import Q500US, Q1500US

import pandas as pd
import numpy as np

class AvgRet(CustomFactor):
    def compute(self, today, asset_ids, out, values):
        values = pd.DataFrame(values)
        out[:] = np.nanmean(values.pct_change(axis=0),axis=0)
        
# This class calculates average daily returns
        
class CVaR(CustomFactor):
    def compute(self, today, asset_ids, out, values):
        values = pd.DataFrame(values)
        values = values.pct_change(axis=0)      
        out[:] = np.nanpercentile(values,1,axis=0)
        
# This class approximates CVaR (I discuss this further in my readme)
         
def make_pipeline():           
    sma_200 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=200)
    not_a_penny_stock = (sma_200 > 5)
    dollar_volume = AverageDollarVolume(window_length=20)
    is_liquid = (dollar_volume > 1e7)
    tradeable_stocks = (
        Q1500US()
        & not_a_penny_stock
        & is_liquid
    ) # Initial Screen

    avg_ret = AvgRet(inputs=[USEquityPricing.close],window_length=252,mask=tradeable_stocks)
    cvar = CVaR(inputs=[USEquityPricing.close],window_length=252,mask=tradeable_stocks)
    starr = -avg_ret/cvar
    # Note: there is a minus here becuase our expected shortfalls were negative values,
    # so we had to flip them to make the Starr Ratio.
    shorts = starr.percentile_between(0,2.5)
    longs = starr.percentile_between(97.5,100)
    securities_to_trade = (shorts | longs)
    
    beta = RollingPearsonOfReturns(
    target=sid(8554), 
    returns_length=30, 
    correlation_length=100,
    mask=securities_to_trade
    )
    # Market correlation calculation
    
    pipe_screen = securities_to_trade
    
    pipe_columns = {
        'longs':longs,
        'shorts':shorts,
        'beta': beta,
        'starr': starr
    }
    
    pipe = Pipeline(columns = pipe_columns, screen = pipe_screen)
    return pipe

def initialize(context):
    
    context.spy = sid(8554)
    
    attach_pipeline(make_pipeline(), 'starr_ratio')
    
    context.shorts = None
    context.longs = None
    context.output = None
    
    schedule_function(rebalance, date_rules.month_start())
    schedule_function(cancel_open_orders, date_rules.every_day(),
                      time_rules.market_close())
    
def before_trading_start(context, data):    
    context.output = pipeline_output('starr_ratio')
    ranks = context.output['starr']
    
    context.longs = ranks[context.output['longs']]
    context.shorts = ranks[context.output['shorts']]
    
    context.active_portfolio = context.longs.index.union(context.shorts.index)
    context.assets=context.active_portfolio
      
def handle_data(context, data):
    pass
 
def cancel_open_orders(context, data):
    open_orders = get_open_orders()
    for security in open_orders:
        for order in open_orders[security]:
            cancel_order(order)
            
    record(lever=context.account.leverage,
           exposure=context.account.net_leverage,
           num_pos=len(context.portfolio.positions))
    
def rebalance(context, data):
             
    for security in context.shorts.index:
        if get_open_orders(security):
            continue
        if data.can_trade(security):
            order_target_percent(security, -1.00 / len(context.shorts.index))
            
    for security in context.longs.index:
        if get_open_orders(security):
            continue
        if data.can_trade(security):
            order_target_percent(security, 1.00 / len(context.longs.index))
            
    # These two functions fill our long and short orders.
            
    for security in context.portfolio.positions:
        if get_open_orders(security):
            continue
        if data.can_trade(security):
            if security not in (context.longs.index | context.shorts.index):
                order_target_percent(security, 0)
                
    context.moBeta = 1.00*np.nanmean(context.output.ix[context.output["longs"]==True]['beta'])-1.00*np.nanmean(context.output.ix[context.output["shorts"]==True]['beta'])
    
    order_target_percent(context.spy, -(context.moBeta))
    
    # These two lines of code calculate the net beta of our portfolio and target a portfolio percentage of SPY such that we offset of market exposure
    
