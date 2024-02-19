# this code goes in Quantopian research
# We used this file to approximate a return percentile that would correspond to a given CVaR percentile

from quantopian.research import run_pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline import Pipeline, CustomFactor
from quantopian.pipeline.factors import SimpleMovingAverage, AverageDollarVolume, RollingPearsonOfReturns, Returns, RollingLinearRegressionOfReturns
from quantopian.pipeline.data import morningstar
from quantopian.pipeline.filters.morningstar import IsPrimaryShare
from quantopian.pipeline.filters.morningstar import Q1500US

import pandas as pd
import numpy as np

class AvgRet(CustomFactor):
    def compute(self, today, asset_ids, out, values):
        values = pd.DataFrame(values)
        out[:] = np.nanmean(values.pct_change(axis=0),axis=0)
        
class StdDev(CustomFactor):
    def compute(self, today, asset_ids, out, prices):
        prices = pd.DataFrame(prices)
        out[:] = np.nanstd(prices.pct_change(axis=0),axis=0,ddof=1)
'''        
class CVaR(CustomFactor):
    def compute(self, today, asset_ids, out, values):
        values = pd.DataFrame(values)
        values = values.pct_change(axis=0)
        for j in range(len(values.columns)):
            p=np.nanpercentile(values.ix[:,j],10)
            for i in range(len(values.index)):
                if values.ix[i,j]>p:
                    values.ix[i,j]=np.NaN
        out[:] = np.nanmean(values,axis=0)
'''

class CVaR(CustomFactor):
    def compute(self, today, asset_ids, out, values):
        values = pd.DataFrame(values)
        values = values.pct_change(axis=0)
        for j in range(len(values.columns)):
            p=np.nanpercentile(values.ix[:,j],10)
            out[j] = np.nanmean(values.ix[values.ix[:,j]<=p,j])

class AVaR(CustomFactor):
    def compute(self, today, asset_ids, out, values):
        values = pd.DataFrame(values)
        values = values.pct_change(axis=0)
        out[:] = np.nanpercentile(values,3.0,axis=0)

spyder=symbols(8554)

def make_pipeline():
    avg_ret = AvgRet(inputs=[USEquityPricing.close],window_length=100,mask=Q1500US())
    std_dev = StdDev(inputs=[USEquityPricing.close],window_length=100,mask=Q1500US())
    cvar = CVaR(inputs=[USEquityPricing.close],window_length=252,mask=Q1500US())
    avar = AVaR(inputs=[USEquityPricing.close],window_length=252,mask=Q1500US())
    sharpe = avg_ret/std_dev
    starr = -avg_ret/cvar
    diff=avar-cvar
    shorts = sharpe.percentile_between(0,2.5)
    longs = sharpe.percentile_between(97.5,100)
    securities_to_trade = (shorts | longs)
    
    corr = RollingPearsonOfReturns(
    target=symbols("SPY"), 
    returns_length=30, 
    correlation_length=100,
    )

    return Pipeline(
        columns={
            'corr': corr,
            'cvar': cvar,
            'avar': avar,
            'diff': diff
        },
    screen=securities_to_trade
    )

result = run_pipeline(make_pipeline(), '2016-10-31', '2016-10-31')
result

#metNeta = np.nanmean(result.ix[result[\"longs\"]==True]['corr'])-np.nanmean(result.ix[result[\"shorts\"]==True]['corr'])\n",
meanDIF = np.nanmean(result.ix[:,'diff'])
print meanDIF
