from datetime import date, datetime
import streamlit as st
import yfinance as yf
import plotly.express as px



st.title("Streamlit Work.")


st.write("Using Streamlit you are able to view the stock prices of five selected stocks.")
st.write("Select at least two stocks to compare their overall stock prices over a given period of time.")
st.write("Created by Callum Doyle.")
st.write("School email: ctdoyle2@buffs.wtamu.edu")
st.write("Primary email: caldoyle5@outlook.com")
st.write("github: https://github.com/CalDoyle5")


st.markdown("<h1 style='text-align:center; color:yellow; font-family: monospace;'> Five Stock Price Comparison App. </h1>",
            unsafe_allow_html=True)

st.markdown("## **Check Stock Information**")
st.write("Please select at least two stocks")

stock_names = ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TWTR']


selected_tickers = st.multiselect(
    'Select stocks to check. Default stocks are: AAPL and AMZN', options=stock_names, default=['AAPL', 'AMZN'])
st.write("You selected: ", selected_tickers)


st.markdown("## **Check Stock Price History** ")


start_date = st.date_input('Start Date', datetime(2021, 1, 1))

end_date = st.date_input("End Date")


today = date.today()
if st.button("Submit") and len(selected_tickers) >= 2:
    
    if start_date > today or end_date > today:
        st.write("## **Please select a valid date period.**")
    else:
        
        data = yf.download(tickers=selected_tickers,
                           start=start_date, end=end_date)
        
        with st.spinner(text='In progress'):
            high = data['High']

            fig = px.line(
                high,
                x=high.index,
                y=list(high.columns),
                title=f"High stock price: {start_date} to {end_date}",
                labels={"value": "Stock Price ($)", "variable": "Stock"}
            )
            st.write(fig)
            st.success('Done')
