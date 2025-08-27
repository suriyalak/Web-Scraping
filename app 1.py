import streamlit as st
import pandas as pd
import numpy as np
import pickle


st.write("สวัสดี สุริยาลักษณ์")

x = np.array([5, 15, 25, 35, 45, 55, 22, 30]).reshape((-1, 1))    #เปลี่ยนข้อมูล 1 มิติ เป็น 2 มิติ
y = np.array([5, 20, 14, 32, 22, 38, 11, 15])

file_name = "price_model.ml"
loaded_model = pickle.load(open(file_name, 'rb'))
r2 = loaded_model.score(x, y)

# print(f'coefficient of determination: {r2}')
st.write(r2)



# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })

# df

# #################################################

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)

# #################################################

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

################################################

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

# ################################################

# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# ################################################

# st.text_input("Your name", key="name")

# # You can access the value at any point with:
# st.session_state.name       #มี id 

# ################################################

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data

# ################################################

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

# #################################################

# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# #################################################

# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

# #################################################

# import time

# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'

# ##################################################

# @st.cache_data
# def long_running_function(param1, param2):
#     return A

# ##################################################

# if "counter" not in st.session_state:
#     st.session_state.counter = 0

# st.session_state.counter += 1

# st.header(f"This page has run {st.session_state.counter} times.")
# st.button("Run it again")

# #################################################

# conn = st.connection("my_database")
# df = conn.query("select * from my_table")
# st.dataframe(df)