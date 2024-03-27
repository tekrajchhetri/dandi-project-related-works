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
import json
from src.gdb_connection_manager import _connect_gdb, check_sparql_connection


st.set_page_config(page_title="Configure Connection", page_icon="🌍")

import streamlit as st

st.markdown("# Configure Connection")
st.write("Please provide the configuration details to connect to the database.")
st.sidebar.header("Mapping Demo")
st.write('*: Required fields')
txt_area_value = None
database_connection_type_option = st.selectbox(
    'Select the database that you want to Benchmark*',
    ('Single Database', 'Multiple Databases',))
default_database_option = ('GraphDB', 'Blazegraph', 'StarDog')
if database_connection_type_option == 'Single Database':
    st.write("Single Database")
    if "database_connection_parameters" in st.session_state:
        hostname = st.text_input('Hostname*', value=st.session_state["database_connection_parameters"]["hostname"])
        username = st.text_input('Username', value=st.session_state["database_connection_parameters"]["username"])
        password = st.text_input('Password', value=st.session_state["database_connection_parameters"]["password"])
        repository = st.text_input('Repository name (Needed for certain database, e.g. GraphDB)',
                                   value=st.session_state["database_connection_parameters"]["repository"])
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
        username = st.text_input('Username')
        password = st.text_input('Password')
        repository = st.text_input('Repository name (Needed for certain database, e.g. GraphDB)')
        database_option = st.selectbox(
            'Select the database that you want to Benchmark*',
            default_database_option)
else:
    if "database_connection_parameters" in st.session_state:
        multiple_db_parameters_placeholder = st.session_state.get("database_connection_parameters")
    else:
        multiple_db_parameters_placeholder = {
                "GraphDB": {
                    "hostname": "",
                    "username": "",
                    "password": "",
                    "repository": "",
                    "database_option": "GraphDB",
                },
                "Blazegraph": {
                    "hostname": "",
                    "username": "",
                    "password": "",
                    "database_option": "Blazegraph",
                },
            }


    json_data = json.dumps(multiple_db_parameters_placeholder, indent=6)
    num_lines = json_data.count('\n') + 1
    txt_area_value_conn = st.text_area("Multiple Databases",
                                  json_data,
                                  placeholder=json_data, height=num_lines * 40,
                                  key="text_area_dbconn", )


    st.write("This feature is not supported yet.")

if st.button("Validate Connection", type="primary"):
    if database_connection_type_option == 'Single Database':
        show_warning = hostname == ""
        if show_warning:
            st.warning('Required fields are missing', icon="⚠️")
        else:
            connection_details = {
                "hostname": hostname,
                "username": username,
                "password": password,
                "repository": repository,
                "database_option": database_option,
            }

            try:
                if database_option in ["GraphDB", "Blazegraph"]:
                    conn = _connect_gdb(connection_details=connection_details,
                                        request_type="get",
                                        connecting_database=database_option)
                else:
                    st.error('Database not supported yet.')
                    conn = None
                if conn is not None and check_sparql_connection(conn):
                    st.session_state.database_connection_parameters = connection_details
                    st.session_state.sessionstate_database_connection = [{database_option: conn}]
                    st.success('Connected to the graph database successfully.')
                else:
                    st.error('Failed to connect to the graph database. Check your connection details.')
            except ConnectionError as e:
                st.error(f'Failed to connect to the graph database: {str(e)}')

    else:
        connection_data = json.loads(txt_area_value_conn)
        database_options = list(connection_data.keys())
        database_options = list(connection_data.keys())

        db_data = [connection_data.get(db).get("hostname") == "" for db in database_options]
        show_warning = True in db_data
        if show_warning:
            st.warning('Required fields are missing, e.g., hostname, repository', icon="⚠️")
        else:
            gdb_connection_inst = [{connection_data.get(db).get("database_option"):_connect_gdb(connection_details=connection_data.get(db),
                                                                 request_type="get",
                                                                 connecting_database=connection_data.get(db).get("database_option"))}  for db in database_options]
            gdb_conn_test = [check_sparql_connection(list(conn.values())[0]) for conn in gdb_connection_inst]

            if not False in gdb_conn_test:
                st.session_state.database_connection_parameters = connection_data
                st.session_state.sessionstate_database_connection = gdb_connection_inst
                st.success('Connected to the graph database successfully.')
            else:
                st.error('Failed to connect to the graph database. Check your connection details/database.')




