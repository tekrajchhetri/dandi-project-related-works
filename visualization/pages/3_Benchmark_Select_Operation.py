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
# @File    : 3_Benchmark_Select_Operation.py
# @Software: PyCharm

import streamlit as st
from src.helper import plot
import os, time, json
from src.helper import _fetch_data_gdb
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)
list_of_files = []
st.set_page_config(page_title="Select Operation", page_icon="📊")
st.write(st.session_state.get("single_database_connection"))
st.markdown("# Benchmark Select Operation")  # Title of the page
repeatition = st.number_input("Number of times to repeat the operation", min_value=10, max_value=10000, value=10)
sparql_query = st.text_area(label="Please provide the SPARQL query to benchmark the select operation.", height=500)
# plot_title = st.text_input("Please provide the title for the plot, i.e., benchmark results.")
if st.button("Benchmark"):
    if "sessionstate_database_connection" in st.session_state:
        if len(sparql_query) < 50:
            st.write("Check your SPARQL query", icon="⚠️")
        else:

            st.write("Benchmarking the select operation...")

            if st.session_state.get("sessionstate_database_connection"):
                dict_item_db = st.session_state.sessionstate_database_connection
            
            else:
                print("No database connection found.")
            for dict_item in dict_item_db:
                for key, value in dict_item.items():
                    filename = f"{key}_result.json"
                    list_of_files.append(key)
                    if os.path.exists(filename):
                        os.remove(filename)

                    _fetch_data_gdb(value, sparql_query, repeatition, filename)

            while True:
                all_results = [os.path.exists(f"{resultfile}_result.json") for resultfile in list_of_files]

                if not False in all_results:
                    st.write("Benchmarking completed! Plotting the results...")
                    result_dict_plot = {}
                    print(result_dict_plot)
                    for file in list_of_files:
                        with open(f"{file}_result.json", "r") as json_file:
                            data = json.load(json_file)
                            result_dict_plot[file] = np.average(data["execution_time"])

                    plot(result_dict_plot, repeatition)

                    break  # Exit the loop if the file exists
                else:
                    print("File does not exist. Waiting...")
                    time.sleep(2)  # Wait for 1 second before checking again

            #

    else:
        st.error("Please configure the connection first.")
