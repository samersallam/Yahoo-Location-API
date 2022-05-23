import streamlit
import pandas

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
