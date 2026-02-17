import streamlit as st
from support_bot import classify_intent, generate_response

st.set_page_config(page_title="Customer Support Chatbot")

st.title("💬 Customer Support Chatbot")

user_input = st.text_input("How can we help you today?")

if st.button("Send"):
    if user_input:
        intent = classify_intent(user_input)
        response = generate_response(intent, user_input)

        st.markdown(f"**Detected Intent:** `{intent}`")
        st.markdown("**Support Response:**")
        st.write(response)