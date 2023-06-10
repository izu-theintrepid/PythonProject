


import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import mysql.connector as mycon
import pandas as pd

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
#connect to mysql
con=mycon.connect(host='localhost',user='root',passwd='isradps1234',database='vitalities')

if con.is_connected:
    
    cur=con.cursor()

#main function

st.title("Welcome to the Vitalities :wave:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Login")
    with st.form("login_form"):
        vit_mail_login = st.text_input("VIT Mail ID")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

        if login_button:
            query="select vmail,password from users"
            cur.execute(query)
            result=cur.fetchall()
            for i in result:
                if vit_mail_login == i[0] and password == i[1]:
                    switch_page("forum")
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
            if (new_name or reg_no or hostel_block or room_no or vit_mail or new_password or confirm_password) == "":
                st.error("Please fill all the details")
            else:
                if new_password != confirm_password:
                    st.error("Passwords do not match")
                else:
                    cur.execute("insert into users values('{}', '{}', '{}', {}, '{}', '{}')".format(new_name,reg_no,hostel_block,int(room_no),vit_mail,new_password))
                    con.commit()

                    st.success("Account created successfully!")
                    switch_page("forum")
                    
            


 
# import streamlit as st
# import pandas as pd
# import mysql.connector as con
# import pickle
# from pathlib import Path

# import streamlit_authenticator as stauth # pip install streamlit-authenticate
# from streamlit_extras.switch_page_button import switch_page

# mycon=con.connect(host='localhost',user='root',passwd='isradps1234',database='vitalities')

# if mycon.is_connected:
#     print("connection successful")


# def new_page():
#     st.subheader("VITalidsdsties")

# st.set_page_config(
#     page_title="Log in",layout="wide",
#     page_icon=":wave:"

# )
# st.subheader("VITalities")

# col1, col2 ,col3= st.columns(3)

# with col1:
#     with st.container():
#         st.title(" ")
# with col2:
#     with st.container():
#         st.title("Login")
#         username=st.text_input("Username")
#         password=st.text_input("Password",type='password')
#         if st.button("Login"):
#             switch_page("next_page")