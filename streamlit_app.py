import streamlit
import pandas

streamlit.title('My parents new healty dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach and Rocket Smoothie')
streamlit.text('Hard-boiled Free-Range Egg')


streamlit.title('Build your own Fruit Smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
