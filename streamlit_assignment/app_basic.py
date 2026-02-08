import streamlit as st

st.title("Welcome to Streamlit")
username=st.text_input("Enter your username",key="username")
#st.write(f"Hello {username}")

if st.button("Greet Me"):
    st.write(f"Hello.! {username}")
    