import streamlit as st

st.title("Simple Sales Dashboard")
month=st.selectbox("Months",["January","February","March","April","May","June","July","August","September","October","November","December"])
sales={"January":10000,"February":15000,"March":12000,"April":18000,"May":20000,"June":22000,"July":25000,"August":24000,"September":21000,"October":23000,"November":26000,"December":30000}
st.metric(label="Total Sales",value=sales[month])
st.bar_chart(list(sales.values()))
