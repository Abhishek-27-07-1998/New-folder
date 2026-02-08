import streamlit as st

st.title("Product Form")
st.sidebar.title("Product Details")
name=st.sidebar.text_input("Product Name")
category=st.sidebar.selectbox("Category",["All","Electronics","Shoes","Clothing","Books","Home&Kitchen"])
price=st.sidebar.number_input("Price")
product_added=st.button("Add Product")
if product_added and name and category !="All" and price>0:
    st.success("Product added successfully!")
    st.write(f"Product Name: {name}")
    st.write(f"Category: {category}")
    st.write(f"Price: ${price}")
elif product_added:
    st.error("Please fill in all the details to add the product.")