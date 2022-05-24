import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title("My Parents New Healthy Dinner")

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruites_selected = streamlit.multiselect("Pick some fruits : ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruites_to_show = my_fruit_list.loc[fruites_selected]
streamlit.dataframe(fruites_to_show)

streamlit.header('FruityVice Fruit Advice')

user_input = streamlit.text_input('Choose a fruit ?', 'Kiwi')
resp = requests.get('https://www.fruityvice.com/api/fruit/' + user_input)

resp_norm = pandas.json_normalize(resp.json())
streamlit.dataframe(resp_norm)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

my_cur = my_cnx.cursor()

my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

my_data_row = my_cur.fetchone()

streamlit.text("Hello from Snowflake:")

streamlit.text(my_data_row)
