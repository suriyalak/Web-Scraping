import streamlit as st
import pandas as pd
import numpy as np

st.write("สวัสดี สุริยาลักษณ์ ")

###############################################
#"""
# My first app
#Here's our first attempt at using data to create a table:
#"""

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df