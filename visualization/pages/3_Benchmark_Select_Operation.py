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

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title="Select Operation", page_icon="📊")

st.markdown("# Benchmark Select Operation")
repeatition = st.number_input("Number of times to repeat the operation", min_value=10, max_value=10000, value=10)
sparql_query = st.text_area(label="Please provide the SPARQL query to benchmark the select operation.", height=500)
plot_title = st.text_input("Please provide the title for the plot, i.e., benchmark results.")
if st.button("Benchmark"):
    if "database_connection" in st.session_state:
        if len(sparql_query) < 50:
            st.write("Check your SPARQL query", icon="⚠️")
        else:

            if len(plot_title)<10:
                st.write("Check your plot title", icon="⚠️")
            else:

                st.write("Benchmarking the select operation...")
                if os.path.exists("result.json"):
                    os.remove("result.json")
                # for i in range(repeatition+1):
                _fetch_data_gdb(st.session_state.database_connection, sparql_query, repeatition)

                    # execution_times_lst.append(result.get("execution_time"))
                while True:
                    if os.path.exists("result.json"):
                        st.write("Benchmarking completed! Plotting the results...")
                        with open("result.json", "r") as json_file:
                            data = json.load(json_file)
                        plot(data["execution_time"], plot_title, repeatition)


                        break  # Exit the loop if the file exists
                    else:
                        print("File does not exist. Waiting...")
                        time.sleep(2)  # Wait for 1 second before checking again

                #

    else:
        st.error("Please configure the connection first.")
