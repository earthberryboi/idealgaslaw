import streamlit as st

st.write("# Ideal gas law calculator")

st.write("Welcome to the ideal gas law calculator. This is a small streamlit demo to show the power of prototyping in streamlit." \
"Most text formatting can be down with markdown or latex syntax for equations."

" We will be calculating the amount of moles of a perfect gas mixture as describe by the following equation:")

st.write(r'''
         $$
         n = \frac{PV}{RT}
         $$
         ''')


st.write("The subsequent code beneath here is a grand total of 5 lines to handle everything from input to calculations.")

temperature = st.number_input("Select the temperature of the gas", 1, 1000, step = 20, key = "temperature")

col = st.columns(2)

with col[0]: volume = st.slider("Select the volume of the gas", 0, 100, 10, key = "volume")

with col[1]: pressure = st.slider("Select the pressure of the gas", 1,100000, 10000, key = "pressure")

st.write(f'The number of moles are: {pressure*volume/(8.314*temperature)}')