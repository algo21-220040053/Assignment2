# Assignment2
The project is an assignment about behavior finance for Algo Trading.
## Brief introduction
The empirical study finds that most markets have "monthly effect", that is, the average return rate of one or some specific months is significantly 
different from that of other months year after year. 

This article discovered the monthly effect in Chinese market from Jan 1, 2010 to Dec 31, 2020. According to our discovery, we constructed a simple strategy and did backtest on it.
## Monthly rate of return
Perform a visual analysis of the index's monthly return rate, and mark the point where the return rate is higher than the third-quarter quantile. 

<div align=center><img width="640" alt="上证月度收益率" src="https://user-images.githubusercontent.com/78734848/117835085-48c53400-b2aa-11eb-8a72-a93e7993b286.png">
  
<img width="640" alt="创业板月度收益率" src="https://user-images.githubusercontent.com/78734848/117835288-714d2e00-b2aa-11eb-83d7-d30b26126634.png"><div align=left>

## Average monthly rate of return
The following is a statistical analysis of the monthly mean return. The figure shows that some months have a positive mean return, and some months have a negative mean return.
The average yield in February, March, April, October, November and December were greater than 1% of the Shanghai Composite Index. However, the average yield in January, June 
and August were less than -1%. The situation on the Gem index is similar, but there are certain differences in some months. 

<div align=center><img width="640" alt="上证月度平均收益率" src="https://user-images.githubusercontent.com/78734848/117837398-03a20180-b2ac-11eb-9af0-facab0bbe9a7.png">
  
<img width="640" alt="创业板月度平均收益率" src="https://user-images.githubusercontent.com/78734848/117837436-0997e280-b2ac-11eb-9b0d-6d360c4cb999.png"><div align=left>

## Backtest
According to the statistical analysis in the second part, construct a simple monthly timing strategy and conduct historical backtesting. That is, first perform statistical 
analysis on the historical index data to calculate the historical average of the monthly return. When the average monthly return is greater than 1%, change the month to long,
and change the month to short when the average monthly return is less than -1%. The remaining months are equivalent to short positions. 
### Shanghai Composite Index backtest
<div align=center><img width="640" alt="上证回测" src="https://user-images.githubusercontent.com/78734848/117839573-eec66d80-b2ad-11eb-8f9a-2a16cf966840.png"><div align=left>
Output:
做多月份：[2, 4, 10, 11, 12]
做空月份：[1, 6, 8]
策略年胜率为：70.0%
策略月胜率为：50.0%
总收益率：  策略：237.32%，指数：21.75%
年化收益率：策略：12.93%, 指数：1.99%
最大回撤：  策略：26.36%, 指数：45.92%
策略Alpha： 0.13, Beta：0.14，夏普比率：1.91

### Gem Index backtest
<div align=center><img width="640" alt="创业板回测" src="https://user-images.githubusercontent.com/78734848/117839809-27fedd80-b2ae-11eb-8b38-0c2c535c6a0c.png"><div align=left>
Output:
做多月份：[2, 3, 5, 10]
做空月份：[1]
策略年胜率为：70.0%
策略月胜率为：64.0%
总收益率：  策略：248.67%，指数：156.79%
年化收益率：策略：13.3%, 指数：9.89%
最大回撤：  策略：40.79%, 指数：65.34%
策略Alpha： 0.11, Beta：0.26，夏普比率：1.61



