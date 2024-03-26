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
# @File    : 1_Configure_Connection.py
# @Software: PyCharm

import streamlit as st
from src.gdb_connection_manager import _connect_gdb, check_sparql_connection

st.set_page_config(page_title="Configure Connection", page_icon="🌍")

import streamlit as st
st.write("database_connection" in st.session_state)

st.markdown("# Configure Connection")
st.write("Please provide the configuration details to connect to the database.")
st.sidebar.header("Mapping Demo")
st.write('*: Required fields')
default_database_option = ('GraphDB', 'StarDog', 'Blazegraph')
if "database_connection_parameters" in st.session_state:
    hostname = st.text_input('Hostname*', value=st.session_state["database_connection_parameters"]["hostname"])
    username = st.text_input('Username*', value=st.session_state["database_connection_parameters"]["username"])
    password = st.text_input('Password*', value=st.session_state["database_connection_parameters"]["password"])
    repository = st.text_input('Repository name*', value=st.session_state["database_connection_parameters"]["repository"])
    selected_db_option = st.session_state["database_connection_parameters"]["database_option"]
    temp = list(default_database_option)
    temp.remove(selected_db_option)
    temp.insert(0, selected_db_option)
    default_database_option = tuple(temp)
    database_option = st.selectbox(
        'Select the database that you want to Benchmark*',
        default_database_option)
else:
    hostname = st.text_input('Hostname*')
    username = st.text_input('Username*')
    password = st.text_input('Password*')
    repository = st.text_input('Repository name*')
    database_option = st.selectbox(
        'Select the database that you want to Benchmark*',
        default_database_option)

if st.button("Validate Connection", type="primary"):
    show_warning = hostname == "" or username == "" or password == "" or repository == ""
    if show_warning:
        st.warning('All fields are required', icon="⚠️")
    else:
        connection_details = {
            "hostname": hostname,
            "username": username,
            "password": password,
            "repository": repository,
            "database_option": database_option
        }
        try:
            if database_option == 'GraphDB':
                conn = _connect_gdb(connection_details)
            else:
                st.error('Database not supported yet.')
                conn = None
            if check_sparql_connection(conn):
                st.session_state.database_connection_parameters = connection_details
                st.session_state.database_connection = conn
                st.success('Connected to the graph database successfully.')
            else:
                st.error('Failed to connect to the graph database. Check your connection details.')
        except ConnectionError as e:
            st.error(f'Failed to connect to the graph database: {str(e)}')
