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

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

def get_info_from_db():
    my_cur = my_cnx.cursor()
    my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
    my_data_row = my_cur.fetchall()
    return data_row

if streamlit.button('Get fruit from list'):
    streamlit.header("The fruit load list contains:")
    my_data_row = get_info_from_db()
    streamlit.dataframe(my_data_row)

def insert_fruit_into_snowflake(fruit):
    my_cur = my_cnx.cursor()
    my_cur.execute("INSERT INTO FROM FRUIT_LOAD_LIST values(fruit)")
    return f'Thanks for adding {fruit}'

streamlit.header("What fruit would you like to add?")
added_fruit = streamlit.text_input('What fruit would you like information about?', 'Jackfruit')
if strealit.button('Add a fruit to the list'):
    insert_fruit_into_snowflake(added_fruit)
    streamlit.write('Thanks for adding', added_fruit)

