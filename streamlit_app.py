import streamlit
import pandas as pd

streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
df = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
df.set_index('Fruit', inplace=True)
fruits = streamlit.multiselect('Pick some fruits', list(df.index), ['Avocado','Strawberries'])
fruits_show = df.loc[fruits]
streamlit.dataframe(fruits_show)
