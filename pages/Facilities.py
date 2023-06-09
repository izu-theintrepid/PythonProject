import streamlit as st

st.set_page_config(page_title='Facilities', page_icon=':raised_hands:', layout='wide')
st.title('Facilities :raised_hands:')

col1, col2 = st.columns(2)

with col1:
    st.header('Room Cleaning :broom:')
    time = st.time_input('Availability Time')
    if st.button('Book Cleaning :broom:'):
        st.success('Booked successfully!')

with col2:
    st.header('Mess Food Service :knife_fork_plate:')
    reason = st.text_input('Reason', '')
    if st.button('Book Food Service :knife_fork_plate:'):
        st.success('Booked successfully!')

st.header('Services/Suggestions	:receipt:')
services_suggestions = st.text_area('Enter your services/suggestions here', '')
if st.button('Submit'):
    st.success('Submitted successfully!')