import streamlit as st
import os

st.set_page_config(page_title='Academics', page_icon=':books:', layout='wide')

st.subheader('Access previous year question papers and notes! :books:')
st.write('Select the year and branch to find/upload the question papers and notes:')
sub_name = st.text_input('Enter the subject name:')
sub_code = st.text_input('Enter the subject course code:')
look_for = st.selectbox('Look for/Upload:', ('Question Papers', 'Notes'))
year = st.selectbox('Select the year', ('2019', '2020', '2021'))
branch = st.selectbox('Select the branch', ('CSE', 'ECE', 'EEE', 'MECH', 'CIVIL'))
left_column, right_column = st.columns(2)
with left_column:
    st.subheader('Find Question Papers and notes:')
    if st.button('Find'):
        st.write('You selected:', year, branch)
        st.write('Here are the question papers and notes:')
        st.write('Question Papers:')
        st.write('Notes:')

with right_column:
    st.subheader('Upload Question Papers and notes:page_with_curl::')
    uploaded_file = st.file_uploader("Click here to Upload:file_folder:", type=["pdf", "jpg", "jpeg", "png"], accept_multiple_files=False)
    if st.button('Upload'):
        if uploaded_file is not None:
            file_name = uploaded_file.name
            file_data = uploaded_file.read()

            save_directory = 'C:/Users/sammy/OneDrive/Desktop/Prod/PythonTheoryDA/'#change path(obvio)👉🏻👈🏻
            os.makedirs(save_directory, exist_ok=True)
            file_path = os.path.join(save_directory, file_name)
            with open(file_path, "wb") as f:
                f.write(file_data)

            st.success("File saved successfully!")
        else:
            st.warning("No file selected!")
