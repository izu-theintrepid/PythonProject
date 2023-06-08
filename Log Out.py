import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
st.title("Welcome to the Vitalities :wave:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Login")
    with st.form("login_form"):
        vit_mail_login = st.text_input("VIT Mail ID")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

        if login_button:
            if vit_mail_login == "@vit.ac.in" and password == "bababooie":
                switch_page("Academics")
            else:
                st.error("Invalid username or password")

with col2:
    st.subheader("Sign Up")
    with st.form("signup_form"):
        new_name = st.text_input("Enter Name:")
        reg_no = st.text_input("Registration Number:")
        hostel_block = st.text_input("Hostel Block:")
        room_no = st.text_input("Room Number:")
        vit_mail = st.text_input("VIT Mail ID:")
        new_password = st.text_input("New Password:", type="password")
        confirm_password = st.text_input("Confirm Password:", type="password")
        signup_button = st.form_submit_button("Sign Up")

        if signup_button:
            if new_password == confirm_password:
                st.success("Account created successfully!")
            else:
                st.error("Passwords do not match")
