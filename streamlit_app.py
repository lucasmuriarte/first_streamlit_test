import requests
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


streamlit.header("Fruityvice Fruit Advice!")
choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', choice)

api_response = requests.get(f'https://fruityvice.com/api/fruit/{choice}')
json_text = api_response.json()
streamlit.text(json_text)
streamlit.dataframe(pd.json_normalize(json_text))
