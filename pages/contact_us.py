import streamlit as st
from send_email import send_email


st.header("Contact Me")
with st.form(key="mail"):
    user_mail = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: new mail from {user_mail}

From: {user_mail}
{raw_message}
   """
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your email has been sent successfully!")