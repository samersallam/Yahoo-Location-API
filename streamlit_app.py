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

streamlit.header('What fruit would you like to add?')

user_input = streamlit.text_input('Choose a fruit ?', 'Jackfruit')

my_cur.execute("SELECT * from fruit_load_list")

my_data_rows = my_cur.fetchall()

streamlit.text("The fruit list contains")

streamlit.dataframe(my_data_rows)
