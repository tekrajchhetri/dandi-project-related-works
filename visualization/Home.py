# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# DISCLAIMER: This software is provided "as is" without any warranty,
# express or implied, including but not limited to the warranties of
# merchantability, fitness for a particular purpose, and non-infringement.
#
# In no event shall the authors or copyright holders be liable for any
# claim, damages, or other liability, whether in an action of contract,
# tort, or otherwise, arising from, out of, or in connection with the
# software or the use or other dealings in the software.
# -----------------------------------------------------------------------------

# @Author  : Tek Raj Chhetri
# @Email   : tekraj@mit.edu
# @Web     : https://tekrajchhetri.com/
# @File    : Home.py
# @Software: PyCharm

import streamlit as st


st.set_page_config(
    page_title="Benchmarking Me",
    page_icon="🏋️‍♂️", #
)

st.write("# Welcome to Benchmarking Me! 👋🏋️‍♂️")


st.markdown(
    """
    Benchmarking Me is a tool for benchmarking Graph Database. This tool allows you to benchmark the insert operations and select operations.
    
    ### What features this tool provides?
    - Benchmarking Graph Database 
    - Generating Benchmark Reports (i.e., Plots) 
    ### Currently supported Graph Databases
    - GraphDB  
    ### Requirements
    - To benchmark the insert operations, the RDF files in Turtle format are required.
    - To benchmark the select operations, the SPARQL query is required.
    ### How to use this tool?
    - **Provide the configuration details.**
    - **👈 Select a demo from the sidebar**
        - Upload the data file in Turtle format in the case of benchmarking insert operations.
        - Provide the SPARQL query in the case of benchmarking select operations.
    - Click on the **"Submit"** button to benchmark the operation.
"""
)

# import streamlit as st
# from src.helper import validate_uploaded_file
#
# st.title('Benchmarking Tool')
#
# # Define a function to store session state
# def initialize_session():
#     if 'step' not in st.session_state:
#         st.session_state.step = 1
#
# # Step 1: Configuration Details
# def configuration_details():
#     st.title('Step 1: Provide the Configuration Details')
#     st.write('*: Required fields')
#     hostname = st.text_input('Hostname*')
#     username = st.text_input('Username*')
#     password = st.text_input('Password*')
#     repository = st.text_input('Repository name*')
#     database_option = st.selectbox(
#         'Select the database that you want to Benchmark*',
#         ('GraphDB', 'StarDog', 'Blazegraph'))
#     if st.button('Next'):
#         show_warning = hostname == '' or username == '' or password == '' or repository == ''
#         if show_warning:
#             st.warning('All fields are required', icon="⚠️")
#         else:
#             st.session_state.step += 1
#             st.write(f'Configuration Details:{st.session_state.step}')
#
# # Step 2: File Information
# def upload_turtle_file():
#     st.title('Step 2: Upload the Data File in Turtle Format')
#     data_ttl = st.file_uploader('Select the file(s) to upload',accept_multiple_files=True)
#     if st.button('Previous'):
#         st.session_state.step -= 1
#     if st.button('Next'):
#         if data_ttl is None:
#             st.warning('Please upload a file', icon="⚠️")
#         elif validate_uploaded_file(data_ttl) is False:
#             st.warning('Please upload a file in Turtle format', icon="⚠️")
#         else:
#             st.session_state.step += 1
#
# # Step 3: Additional Information
# def additional_info():
#     st.title('Step 3: Sparql Query')
#     address = st.text_area('Provide the SPARQL Query*')
#     if st.button('Previous'):
#         st.session_state.step -= 1
#     if st.button('Submit'):
#         # Do something with collected data
#         st.success('Form Submitted Successfully!')
#         st.write('Name:', st.session_state.name)
#         st.write('Age:', st.session_state.age)
#         st.write('Email:', st.session_state.email)
#         st.write('Phone:', st.session_state.phone)
#         st.write('Address:', st.session_state.address)
#
# # Main function
# def main():
#     initialize_session()
#
#     if st.session_state.step == 1:
#         configuration_details()
#     elif st.session_state.step == 2:
#         st.write(f'In Configuration Details:{st.session_state.step}')
#         upload_turtle_file()
#     elif st.session_state.step == 3:
#         additional_info()
#
# if __name__ == "__main__":
#     main()
