eimport streamlit as st
import sqlite3
import pandas as pd

#database connection
conn = sqlite3.connect("emp.db", check_same_thread=False)
cursor= conn.cursor()

#create table
cursor.execute("""CREATE TABLE IF NOT EXISTS employee
(id integer,name text,sal integer)""")
conn.commit ()

menu=["INSERT","VIEW"]
choice=st.sidebar.selectbox("MENU",menu)
if choice=="INSERT":
    eid=st.number_input("ID")
    name=st.text_input("NAME")
    sal=st.number_input("salary")
    if st.button("SAVE"):
        cursor.execute("""INSERT INTO employee(id,name,sal
)VALUES(?,?,?)""",(eid,name,sal))
        conn.commit()
        st.success("EMPLOYEE ADDED SUCCESSFULLY")
        st.balloons()
################################################################
if choice=="VIEW":
   data=cursor.execute("SELECT * FROM employee")
   st.dataframe(data)

