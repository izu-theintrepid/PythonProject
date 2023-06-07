import streamlit as st
import pandas as pd
import mysql.connector

st.set_page_config(page_title='Forum', page_icon=':speech_balloon:', layout='wide')

#connect to mysql
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="forum_db"
)

#create table
create_table_query = """
CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(255),
    post TEXT,
    replies TEXT,
    points INT DEFAULT 0
)
"""
with connection.cursor() as cursor:
    cursor.execute(create_table_query)

#display posts replies
def display_posts(posts):
    for i, post in enumerate(posts):
        st.write(f"Post #{i + 1}: {post['user']} (Points: {post['points']}) - {post['post']}")
        st.write("Replies:")
        replies = post["replies"]
        if replies:
            for reply in replies:
                st.write(reply)
        else:
            st.write("No replies yet.")

#main function
def main():
    st.title("Forum")

    # add post
    st.subheader("Create a new post")
    user = st.text_input("Enter your name")
    new_post = st.text_area("Enter your post")
    if st.button("Submit"):
        if user and new_post:
            insert_post_query = "INSERT INTO posts (user, post) VALUES (%s, %s)"
            with connection.cursor() as cursor:
                cursor.execute(insert_post_query, (user, new_post))
                connection.commit()
            st.success("Post created successfully!")

    #display existing posts
    st.subheader("Existing Posts")
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()
        display_posts(posts)

    #reply func
    st.subheader("Reply to a post")
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()
        if posts:
            post_number = st.number_input("Enter the post number", min_value=1, max_value=len(posts), value=1)
            reply = st.text_area("Enter your reply")
            if st.button("Reply"):
                if reply:
                    if post_number > 0 and post_number <= len(posts):
                        post_id = posts[post_number - 1]["id"]
                        update_reply_query = "UPDATE posts SET replies = CONCAT(IFNULL(replies, ''), %s) WHERE id = %s"
                        with connection.cursor() as cursor:
                            cursor.execute(update_reply_query, (f"\n{reply}\n", post_id))
                            connection.commit()
                        st.success("Reply added successfully!")
                    else:
                        st.warning("Invalid post number!")
                else:
                    st.warning("Reply content is empty!")
            else:
                st.warning("No reply content provided!")
        else:
            st.warning("No posts available!")
