import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pylab import mpl
import tushare as ts
from pyecharts.charts import Bar

mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

token='f6b511d8d4529f19319e1861edadda749e64a5b8573102deec80cfd8'
ts.set_token(token)

# ----------------------analyse---------------------------------------
# get the daily return
def get_daily_ret(code='sh', start='20100101', end='20201231'):
    df = ts.get_k_data(code, start=start, end=end)
    df.index = pd.to_datetime(df.date)
    daily_ret = df['close'].pct_change()
    daily_ret.dropna(inplace=True)
    return daily_ret

# resample into monthly return and plot it
def plot_mnthly_ret(code,title):
    daily_ret = get_daily_ret(code)
    mnthly_ret = daily_ret.resample('M').apply(lambda x : ((1+x).prod()-1))
    plt.rcParams['figure.figsize']=[20,5]
    mnthly_ret.plot()
    dates=mnthly_ret[mnthly_ret>mnthly_ret.quantile(0.75)].index
    for i in range(0,len(dates)):
        plt.scatter(dates[i], mnthly_ret[dates[i]],color='r')
    labs = mpatches.Patch(color='red',alpha=.5, label="月收益率高于3/4分位")
    plt.title(title+'月度收益率',size=15)
    plt.legend(handles=[labs])
    plt.show()

# plot mean monthly return
def plot_mean_ret(code,title):
    daily_ret = get_daily_ret(code)
    mnthly_ret = daily_ret.resample('M').apply(lambda x : ((1+x).prod()-1))
    mrets=(mnthly_ret.groupby(mnthly_ret.index.month).mean()*100).round(2)
    attr=[str(i)+'月' for i in range(1,13)]
    v=list(mrets)
    bar=Bar()
    bar.add_xaxis(attr)
    bar.add_yaxis(title+'月平均收益率%',v)
    return bar.render()

# ------------------------backtest-------------------------------------
def month_ret_stats(code):
    daily_ret = get_daily_ret(code)
    mnthly_ret = daily_ret.resample('M').apply(lambda x : ((1+x).prod()-1))
    ret_stats=mnthly_ret.groupby(mnthly_ret.index.month).describe()
    pnm=ret_stats[ret_stats['mean']>0.01].index.to_list()
    nnm=ret_stats[ret_stats['mean']<-0.01].index.to_list()
    return pnm,nnm

def Month_Strategy(code, is_short):
    daily_ret = get_daily_ret(code)
    mnthly_ret = daily_ret.resample('M').apply(lambda x: ((1 + x).prod() - 1))
    df = pd.DataFrame(mnthly_ret.values, index=mnthly_ret.index, columns=['ret'])
    pnm, nnm = month_ret_stats(code)
    print(f'做多月份：{pnm}')
    df['signal'] = 0
    for m in pnm:
        df.loc[df.index.month == m, 'signal'] = 1
    if is_short == True:
        for n in nnm:
            df.loc[df.index.month == n, 'signal'] = -1
        print(f'做空月份：{nnm}')
    df['capital_ret'] = df.ret.mul(df.signal)
    df['策略净值'] = (df.capital_ret + 1.0).cumprod()
    df['指数净值'] = (df.ret + 1.0).cumprod()
    return df

def performance(df):
    df1 = df.loc[:, ['ret', 'capital_ret']]
    year_ret = df1.resample('A').apply(lambda x: (x + 1.0).prod() - 1.0)
    year_ret.dropna(inplace=True)
    year_win_rate = len(year_ret[year_ret['capital_ret'] > 0]) / len(year_ret[year_ret['capital_ret'] != 0])
    month_win_rate = len(df1[df1['capital_ret'] > 0]) / len(df1[df1['capital_ret'] != 0])
    total_ret = df[['策略净值', '指数净值']].iloc[-1] - 1
    annual_ret = pow(1 + total_ret, 12 / len(df1)) - 1
    dd = (df[['策略净值', '指数净值']].cummax() - \
          df[['策略净值', '指数净值']]) / \
         df[['策略净值', '指数净值']].cummax()
    d = dd.max()
    beta = df[['capital_ret', 'ret']].cov().iat[0, 1] / df['ret'].var()
    alpha = (annual_ret['策略净值'] - annual_ret['指数净值'] * beta)
    exReturn = df['capital_ret'] - 0.03 / 12
    sharper_atio = np.sqrt(len(exReturn)) * exReturn.mean() / exReturn.std()
    TA1 = round(total_ret['策略净值'] * 100, 2)
    TA2 = round(total_ret['指数净值'] * 100, 2)
    AR1 = round(annual_ret['策略净值'] * 100, 2)
    AR2 = round(annual_ret['指数净值'] * 100, 2)
    MD1 = round(d['策略净值'] * 100, 2)
    MD2 = round(d['指数净值'] * 100, 2)
    S = round(sharper_atio, 2)
    print(f'策略年胜率为：{round(year_win_rate * 100, 2)}%')
    print(f'策略月胜率为：{round(month_win_rate * 100, 2)}%')
    print(f'总收益率：  策略：{TA1}%，指数：{TA2}%')
    print(f'年化收益率：策略：{AR1}%, 指数：{AR2}%')
    print(f'最大回撤：  策略：{MD1}%, 指数：{MD2}%')
    print(f'策略Alpha： {round(alpha, 2)}, Beta：{round(beta, 2)}，夏普比率：{S}')

def plot_performance(df,name):
    d1=df[['策略净值','指数净值']]
    d1[['策略净值','指数净值']].plot(figsize=(15,7))
    plt.title(name+'—'+'月份择时交易策略回测',size=15)
    plt.xlabel('')
    ax=plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.show()

def main_bt(code='sh',name='上证综指',is_short=False):
    df=Month_Strategy(code,is_short)
    print(f'回测标的：{name}指数')
    performance(df)
    plot_performance(df,name)


if __name__ == '__main__':
    plot_mnthly_ret('sh', '上证综指')
    plot_mnthly_ret('cyb', '创业板')
    plot_mean_ret('sh', '上证综指')
    plot_mean_ret('cyb', '创业板')
    main_bt()
    main_bt('cyb', '创业板')

