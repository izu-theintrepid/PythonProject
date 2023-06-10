import streamlit as st
import pandas as pd
import mysql.connector as mycon

st.set_page_config(page_title='Forum', page_icon=':speech_balloon:', layout='wide')

#connect to mysql
con=mycon.connect(host='localhost',user='root',passwd='isradps1234',database='vitalities')

cur=con.cursor()
query = "SELECT * FROM forum"
cur.execute(query)
posts = cur.fetchall()
    
#add post
count=len(posts)+1

#display posts replies
def display_replies(post_number,reply):
    global count
    if reply:
        if post_number > 0 and post_number <= len(posts):
            
            update_reply_query = "UPDATE forum SET replies = CONCAT(IFNULL(replies, ''), %s) WHERE postnum = %s"
    
            cur.execute(update_reply_query, (reply+'\n', post_number))
            con.commit()
            st.success("Reply added successfully!")
        else:
            st.warning("Invalid post number!")
    else:
        st.warning("Reply content is empty!")
    
    st.experimental_rerun()

#main function
def main():
    st.title("Forum")

    # add post
    st.subheader("Create a new post")
    user = st.text_input("Enter your name")
    new_post = st.text_area("Enter your post")

    
    
    
    global count
    if st.button("Submit"):
        if user and new_post:
            query = "INSERT INTO forum (name, post,postnum) VALUES (%s, %s,%s)"
            cur.execute(query, (user, new_post,count))
            con.commit()
            
            st.success("Post created successfully!")
        else:
            st.warning("Please enter your name and post content!")

    #display existing posts
    st.header("Existing Posts")
    col1,col2,col3=st.columns([0.6,0.05,0.35])
    
      
    
    
    
    with col1:
        
        query = "SELECT * FROM forum"
        cur.execute(query)
        posts = cur.fetchall()

        for i in posts:
            col1,col2=st.columns([1,1])
            with col1:
                try:
                    num_replies = i[4].count("\n")
                except:
                    num_replies = 0
                st.subheader(f"Post #{i[3]},{num_replies}")
                st.write(i[1])
            with col2:
                st.subheader("Replies:")
                try:
                    string=i[4].split("\n")
                    for j in string:
                        st.write(j)
                except:
                    st.write("No replies yet!")
                
        
        
        
    with col2:
        st.write(" ")
    with col3:
        post_number = st.number_input("Enter the post number", min_value=1, max_value=len(posts), value=1)
        reply = st.text_area("Enter your reply")
        if st.button("Reply"):
            display_replies(post_number,reply)

    




main()