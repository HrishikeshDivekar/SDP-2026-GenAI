''' streamlit run app.py '''

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title("My First Streamlit App")
st.write(":streamlit: Hello World")
st.text("Lets Start")

name = st.text_input("Enter name:")
if st.button("Greet"):
    st.success(f"Hello {name}")

df = pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)

st.sidebar.title("Navigation")
st.image("https://tse3.mm.bing.net/th/id/OIP.evXBSnb7zI3wPeHoHbARDgHaHa?cb=defcachec2&rs=1&pid=ImgDetMain&o=7&rm=3",caption="Sample Image")
st.video("https://youtu.be/ly6YKz9UfQ4")

upload_file = st.file_uploader("upload a csv",type="csv")
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.title("abc Text and Markdown Demo")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**, *Italic*, `Code`, [Link](https://streamlit.io)")
st.code("for i in range(5): print(i)", language="python")

st.text_input("Enter name?")
st.text_area("Enter address")
st.number_input("Pick a number", min_value=0, max_value=1)
st.slider("B Count", 0, 100)
st.selectbox("Select correct fruit", ["Strawberry", "Berrystraw", "Brawsterry"])
st.multiselect("Choose toppings", ["Pineapple", "Apple", "Banana"])
st.radio("Pick one", ["1", "2"])
st.checkbox("I agree to the terms")
if st.checkbox("Bonus"):
    st.info("We need to talk")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")
if submitted:
    st.success(f"Welcome, {username}!, your password is {password}")


col1, col2 = st.columns(2)

with col1:
    st.button("Press me in Column 1")
with col2:
    st.button("Press me in Column 2")

with st.expander("See Explanation"):
    st.write("Here is a hidden message inside the expander.")

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
st.pyplot(fig)

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)