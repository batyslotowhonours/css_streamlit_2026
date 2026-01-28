# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("CSS 2026 :)")
st.write("Day 3")
st.write("My first streamlit app")

st.header("Number selection")
#to create a number slider:
number = st.slider ("pick a number", 1,100)
st.write(f"you picked {number}")

st.markdown("some text that you can write")