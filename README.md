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

