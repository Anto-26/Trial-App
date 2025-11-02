import streamlit as st

# App title
st.title("👋 Personalized Greeting App")

# Ask the user to enter their name
name = st.text_input("Enter your name:")

# Add a button to trigger the greeting
if st.button("Say Hi"):
    if name.strip() != "":
        st.success(f"Hi, {name}! 👋 Welcome to my Streamlit app.")
    else:
        st.warning("Please enter your name before clicking the button.")
