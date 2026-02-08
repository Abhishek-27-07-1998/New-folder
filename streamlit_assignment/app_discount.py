import streamlit as st

st.title("Price Calculator")
original_price=st.number_input("Enter a number:",key="number")
discount_perc=st.slider("Select discount percentage:",0,100,10,key="discount")

if st.button("Calculate Discount"):
    discounted_price=original_price-(original_price*discount_perc/100)
    st.success(f"Discounted price: {discounted_price}")
    comparision_data=[["Original Price",original_price], ["Discount",f"{discount_perc}%"],["Final Price",discounted_price]]
    st.table(comparision_data)    