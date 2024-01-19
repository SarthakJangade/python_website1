import streamlit as st
st.title ("Welcome to Sarthak Blog")
st.header("My name")
st.subheader("I am a developer")
st.markdown("I love python")
st.code("""for i in range:
        print(i)""")
import pandas as pd

dataset =pd.read_csv("bald_people.csv")
st.dataframe(dataset)

data1=st.text_input("Enter your name: ")
fname = st.text_input("Enter your email")
adr=st.text_area("Enter your Text: ")
classdata=st.selectbox("Enter your Class: ",(1,2,3,4,5))
button = st.button("Done")
if button :
    st.markdown(f"""
                Name : {data1},
                Email : {fname},
                Address : {adr},
                Class:{classdata}""")
