import requests
import streamlit
import pandas as pd
import snowflake.connector
from urllib.error import URLError

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

def get_info_from_url(fruit: str): 
    api_response = requests.get(f'https://fruityvice.com/api/fruit/{choice}')
    json_text = api_response.json()
    df = pd.json_normalize(json_text)
    return df

streamlit.header("Fruityvice Fruit Advice!")
try:
    choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
    if choice:
        streamlit.write('The user entered', choice)
        df = get_info_from_url(choice)
        streamlit.dataframe(df)
    else:
        streamlit.error('Please enter a fruit to get information')
except URLLError as error:
    streamlit.error()

streamlit.stop()

def get_info_from_db():
    my_cur = my_cnx.cursor()
    my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
    my_data_row = my_cur.fetchall()
    return data_row

if strealit.button('Get fruit from list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    streamlit.header("The fruit load list contains:")
    my_data_row = get_info_from_db()
    streamlit.dataframe(my_data_row)

streamlit.header("What fruit would you like to add?")
added_fruit = streamlit.text_input('What fruit would you like information about?', 'Jackfruit')
streamlit.write('Thanks for adding', added_fruit)

