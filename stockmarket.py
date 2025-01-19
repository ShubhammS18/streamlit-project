import streamlit as st
import pandas as pd
import numpy as np
import datetime
import yfinance as yf
st.title('Stock Market Analysis')

ticker_symbol = st.text_input('Enter the stock ticker symbol:','AAPL')

st.write('You entered:', ticker_symbol)

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input('Start date', datetime.date(2020, 1, 1))
with col2:
    end_date = st.date_input('End date', datetime.date(2020, 12, 31))

data = yf.download(ticker_symbol,start= start_date,end= end_date)

st.write(data)
st.line_chart(data['Close'])

st.bar_chart(data['Volume'])