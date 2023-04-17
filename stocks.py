import pandas as pd
import streamlit as st
import yfinance as yf
from datetime import date

st.set_page_config(layout="wide")
st.title("Stock Price App")
tickerSymbol = st.text_input(label='Enter a ticket symbol', placeholder='Ticker Symbol')

tickerData = yf.Ticker(tickerSymbol)

if tickerSymbol !="":
    st.write("#### Stock Information for "+tickerSymbol)
    st.markdown("---")
    col1, col2 = st.columns([4, 3])
    with col1:
        st.write("Enter Start Date")
    with col2:
        st.write("Enter End Date")
 
    col1, col2, col3, colSpace, col4, col5, col6 = st.columns(7)
    with col1:
        yearStart = st.number_input(label='Year', value=1792, min_value=0, max_value=date.today().year, key=1)
    with col2:
        monthStart = st.number_input(label='Month', value=5, min_value=1, max_value=12, key=2)
    with col3:
        dayStart = st.number_input(label='Day', value=17, min_value=1, max_value=31, key=3)
    
    with col4:
        yearEnd = st.number_input(label='Year', value=date.today().year, min_value=0, max_value=date.today().year, key=4)
    with col5:
        monthEnd = st.number_input(label='Month', value=date.today().month, min_value=1, max_value=12, key=5)
    with col6:
        dayEnd = st.number_input(label='Day', value=date.today().day, min_value=1, max_value=31, key=6)

    tickerDF = tickerData.history(start=f"{yearStart}-{monthStart}-{dayStart}", end=f"{yearEnd}-{monthEnd}-{dayEnd}")
        
    col1, col2 = st.columns(2)
    with col1:
        st.write("")
        st.write("Closing Price vs Time")
        st.line_chart(tickerDF.Close)

    with col2:
        st.write("")
        st.write("Volume vs Time")
        st.line_chart(tickerDF.Volume)

    col1, col2 = st.columns(2)
    with col1:
        st.write(tickerSymbol+" Price Chart")
        st.write(tickerDF)
    with col2:
        st.write("Future and Historic Earning Dates")
        st.write(tickerData.earnings_dates)
    