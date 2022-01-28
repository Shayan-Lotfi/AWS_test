

import streamlit as st
import pandas as pd
import os

columns = st.columns((2,1))
with columns[0]:
    st.title('Zenobe Energy EV Bus Billing Model Demo')
   # st.header('Streamlit demo for bus billing model!')
with columns[1]:
    st.header('Built by CAN team')
st.markdown('---')

sites = ['Abellio Walworth','Abellio Brixton']
zone = ['11 South East', '15 South West']
GSP = ['Medway-132','Medway-582']

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader('Non-commodity Parameters')
    site_select = st.selectbox('Select site from the following list',(sites))
    gsp_select = st.selectbox('Select GSP from the following list',(GSP))

    number_input = st.number_input('Enter grid connection size in MW', min_value=0, max_value=500, step=1)
    with st.sidebar.expander("See Further details on the grid size range"):
        st.write('The grid size connection above has been limited only take values between 0-500MW. Try inserting a value outside this range')

    number_input1 = st.number_input('Enter grid 1 connection size in MW', min_value=0, max_value=500, step=1)
    number_input2 = st.number_input('Enter grid 2 connection size in MW', min_value=0, max_value=500, step=1)
    number_input3 = st.number_input('Enter grid 3 connection size in MW', min_value=0, max_value=500, step=1)
    number_input4 = st.number_input('Enter grid 4 connection size in MW', min_value=0, max_value=500, step=1)
    number_input5 = st.number_input('Enter grid 5 connection size in MW', min_value=0, max_value=500, step=1)
    number_input6 = st.number_input('Enter grid 6 connection size in MW', min_value=0, max_value=500, step=1)
    number_input7 = st.number_input('Enter grid 7 connection size in MW', min_value=0, max_value=500, step=1)
    number_input8 = st.number_input('Enter grid 8 connection size in MW', min_value=0, max_value=500, step=1)
    number_input9= st.number_input('Enter grid 9 connection size in MW', min_value=0, max_value=500, step=1)
    number_input11 = st.number_input('Enter grid 10 connection size in MW', min_value=0, max_value=500, step=1)
    number_input22 = st.number_input('Enter grid 11 connection size in MW', min_value=0, max_value=500, step=1)
    number_input33 = st.number_input('Enter grid 12 connection size in MW', min_value=0, max_value=500, step=1)
    
    

with col2:
    st.subheader('Commodity Parameters')
    multi_scenario_status1 = st.checkbox('Check box 2 to enable multi-scenario mode')



with col3:
    st.subheader('Other Parameters')
    multi_scenario_status = st.checkbox('Check box to enable multi-scenario mode')
    start_date = st.date_input('Enter the starting date')
    period = st.slider('Select the number of years required', min_value=1, max_value=5)

#%% sidebar Section
name_input = st.sidebar.text_input('Enter the name of client')
st.sidebar.header('Billing Model for '+ name_input)
st.sidebar.subheader('Summary of selected parameters')
st.sidebar.markdown('* Multi-scenario capabilities: {}'.format(str(multi_scenario_status)))
st.sidebar.markdown('* Site selected: {}'.format(site_select))
st.sidebar.markdown('* Zone: {}'.format(str(zone[sites.index(site_select)])))
st.sidebar.markdown('* GSP region set to {}'.format(gsp_select))
st.sidebar.markdown('* Scenario grid connection size is {} MW'.format(str(number_input)))

# Possible: not to display information on the sidebar until user submits usings a button