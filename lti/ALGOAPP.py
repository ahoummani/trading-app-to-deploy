#!/usr/bin/env python
# coding: utf-8

# In[1]:


from indicators import *


# In[2]:


from Marché import Data 


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime


# In[4]:



plt.style.use('seaborn-whitegrid')
plt.rcParams['figure.figsize'] = (10,8)


# In[12]:


@st.cache(suppress_st_warning=True)
def getsec():
    return list(Data.MasiComposition()['symbols'])


# In[31]:


securities = getsec()


st.markdown('# Algorithmic Trading Indicators ')
st.markdown('**Author : HOUMMANI Ayoub')

st.markdown(' ')
option = st.sidebar.selectbox('Choose a security', securities)

start = st.sidebar.date_input('Start date', datetime.date(2016,6,1))
end = st.sidebar.date_input('End date', datetime.date(2016,6,1))

start = start.strftime('%Y-%m-%d')
end = end.strftime('%Y-%m-%d')
@st.cache(suppress_st_warning=True)
def getData(name, start, end):
    data=Data.GetSingleData(name, start=start, end=end)
    data.index = pd.to_datetime(data.index)
    return data
data = getData(option, start, end)
indicators = ['Accumulation Distribution Line', 'Average True Range', 'Bollinger Bands', 'Chaikin Money Flow'
              ,'Chaikin Oscillator',"Chande Momentum Oscillator","Commodity Channel Index","Detrended Price Oscillator"
              ,"Directional Movement Index","Double Exponential Moving Average","Ease Of Movement","Envelopes"
              ,"Fibonacci Retracement","Forecast Oscillator","Ichimoku Cloud","Intraday Movement Index"
              ,"Klinger Oscillator","Linear Regression Indicator","Linear Regression Slope","Market Facilitation Index"
              ,"Mass Index","Median Price","Momentum","Moving Average","Moving Average Convergence Divergence"
              ,"Negative Volume Index","On Balance Volume","Parabolic SAR","Performance",'Positive Volume Index'
              ,"Price And Volume Trend","Price Channel","Price Oscillator","Price Rate Of Change"
              ,"Projection Bands","Projection Oscillator","Qstick","Range Indicator",'Relative Momentum Index'
              ,"Relative Strength Index","Relative Volatility Index","Standard Deviation","Stochastic Momentum Index"
              ,"Stochastic Oscillator","Swing Index","TimeSeries Forecast","Triple Exponential Moving Average"
              ,"Typical Price","Ultimate Oscillator","Vertical Horizontal Filter","Volatility Chaikins"
              ,"Volume Oscillator","Volume Rate Of Change","Weighted Close","Wilders Smoothing"
              ,"Williams Accumulation Distribution","Williams R"]
option_two = st.sidebar.selectbox('Choose an Indicator', indicators)
st.set_option('deprecation.showPyplotGlobalUse', False)

if option_two == 'Accumulation Distribution Line':
    indicator = AccumulationDistributionLine(input_data=data)
    st.pyplot(fig=indicator.getTiGraph())
if option_two == 'Average True Range':
    indicator = AverageTrueRange(input_data=data)
    st.pyplot(fig=indicator.getTiGraph())    
if option_two == 'Bollinger Bands':
    indicator = BollingerBands(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Chaikin Money Flow':
    indicator = ChaikinMoneyFlow(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Chaikin Oscillator':
    indicator = ChaikinOscillator(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Chande Momentum Oscillator':
    indicator = ChandeMomentumOscillator(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Commodity Channel Index':
    indicator = CommodityChannelIndex(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Detrended Price Oscillator':
    indicator = DetrendedPriceOscillator(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Directional Movement Index':
    indicator = DirectionalMovementIndex(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Double Exponential Moving Average':
    indicator = DoubleExponentialMovingAverage(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Ease Of Movement':
    indicator = EaseOfMovement(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Envelopes':
    indicator = Envelopes(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Fibonacci Retracement':
    indicator = FibonacciRetracement(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Forecast Oscillator':
    indicator = ForecastOscillator(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Ichimoku Cloud':
    indicator = IchimokuCloud(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Intraday Movement Index':
    indicator = IntradayMovementIndex(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Klinger Oscillator':
    indicator = KlingerOscillator(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Linear Regression Indicator':
    indicator = LinearRegressionIndicator(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Linear Regression Slope':
    indicator = LinearRegressionSlope(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Market Facilitation Index':
    indicator = MarketFacilitationIndex(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Mass Index':
    indicator = MassIndex(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Median Price':
    indicator = MedianPrice(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Momentum':
    indicator = Momentum(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Moving Average':
    indicator = MovingAverage(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Moving Average Convergence Divergence':
    indicator = MovingAverageConvergenceDivergence(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Negative Volume Index':
    indicator = NegativeVolumeIndex(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'On Balance Volume':
    indicator = OnBalanceVolume(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Parabolic SAR':
    indicator = ParabolicSAR(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Performance':
    indicator = Performance(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Positive Volume Index':
    indicator = PositiveVolumeIndex(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Price And Volume Trend':
    indicator = PriceAndVolumeTrend(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Price Channel':
    indicator = PriceChannel(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Price Oscillator':
    indicator = PriceOscillator(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Price Rate Of Change':
    indicator = PriceRateOfChange(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Projection Bands':
    indicator = ProjectionBands(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Projection Oscillator':
    indicator = ProjectionOscillator(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Qstick':
    indicator = Qstick(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Range Indicator':
    indicator = RangeIndicator(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Relative Momentum Index':
    indicator = RelativeMomentumIndex(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Relative Strength Index':
    indicator = RelativeStrengthIndex(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Relative Volatility Index':
    indicator = RelativeVolatilityIndex(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Standard Deviation':
    indicator = StandardDeviation(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Stochastic Momentum Index':
    indicator = StochasticMomentumIndex(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Stochastic Oscillator':
    indicator = StochasticOscillator(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Swing Index':
    indicator = SwingIndex(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'TimeSeries Forecast':
    indicator = TimeSeriesForecast(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Triple Exponential Moving Average':
    indicator = TripleExponentialMovingAverage(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Typical Price':
    indicator = TypicalPrice(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Ultimate Oscillator':
    indicator = UltimateOscillator(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Vertical Horizontal Filter':
    indicator = VerticalHorizontalFilter(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Volatility Chaikins':
    indicator = VolatilityChaikins(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Volume Oscillator':
    indicator = VolumeOscillator(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Volume Rate Of Change':
    indicator = VolumeRateOfChange(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Weighted Close':
    indicator = WeightedClose(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Wilders Smoothing':
    indicator = WildersSmoothing(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Williams Accumulation Distribution':
    indicator = WilliamsAccumulationDistribution(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 
if option_two == 'Williams R':
    indicator = WilliamsR(input_data=data)
    st.pyplot(fig=indicator.getTiGraph()) 


      
        


# In[29]:


indicators = ['Accumulation Distribution Line', 'Average True Range', 'Bollinger Bands', 'Chaikin Money Flow'
              ,'Chaikin Oscillator']


# In[30]:


indicators


# In[ ]:




