import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import os


import mysql.connector as mycon
#connect to mysql
con=mycon.connect(host='localhost',user='root',passwd='isradps1234',database='vitalities')

if con.is_connected:
    
    cur=con.cursor()

#main function
st.set_page_config(page_title='Academics',page_icon=':books:',layout='wide')

st.subheader('Access previous year question papers and notes! :books:')
st.write('Select the year and branch to find/upload the question papers and notes:')
sub_name=st.text_input('Enter the subject name:')
sub_code=st.text_input('Enter the subject course code:')
look_for=st.selectbox('Look for/Upload:',('Question Papers','Notes'))
year = st.selectbox('Select the year',('2019','2020','2021'))
branch = st.selectbox('Select the branch',('CSE','ECE','EEE','MECH','CIVIL'))
left_column, right_column = st.columns(2)
with left_column:
    st.subheader('Find Question Papers and notes:')
    if st.button('Find'):
        if (sub_name or sub_code )!="":
            st.write('You selected:',year,branch)
            st.write('Here are the question papers and notes:')
            st.write('Question Papers:')
            query="select filename from academics where year=%s and branch=%s and type='Question Papers' and subname=%s and subcode=%s"
            cur.execute(query,(year,branch,sub_name,sub_code))
            result=cur.fetchall()
            print(result)
            for i in result:
                with open(i[0],'rb') as file1:
                    st.image(file1.read(),use_column_width=True)
            cur.close()
            con.commit()
            
            
        

with right_column:
    st.subheader('Upload Question Papers and notes:page_with_curl::')
    uploaded_file = st.file_uploader("Click here to Upload:file_folder:", type=["pdf","jpg","jpeg","png"], accept_multiple_files=False)

   
    if st.button("Submit!"):
        if uploaded_file is not None:
            file_name = uploaded_file.name
            file_data = uploaded_file.read()
            # Prepare the SQL INSERT statement with placeholders
            sql = "INSERT INTO academics (subname, subcode, type, year, branch, filename) " \
                  "VALUES (%s, %s, %s, %s, %s, %s)"

            # Execute the INSERT statement with the file data as a parameter
            cur.execute(sql, (sub_name, sub_code, look_for, year, branch, file_name))
            con.commit()
            cur.close()
            
            con.close()



            # save_directory = './C:/Users/ishan/AppData\Local\Programs\Python\Python311\VITalities'
            # os.makedirs(save_directory, exist_ok=True)
            # file_path = os.path.join(save_directory, file_name)
            with open(file_name, "wb") as f:
                f.write(file_data)

            st.success("File saved successfully!")
    else:
        st.warning("No file selected!")