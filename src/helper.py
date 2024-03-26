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
# @File    : helper.py
# @Software: PyCharm
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import json
from SPARQLWrapper import SPARQLWrapper, GET, JSON
import time
def validate_uploaded_file(files):
    """
    Validates the uploaded file.

    Parameters:
    - files (list):  The uploaded files to validate.

    Returns:
    - bool: True if the file is valid, False otherwise.
    """
    for file in files:
        if not file.name.endswith(".ttl"):
            return False
    return True


def plot(data, title, N, nreplablel="N-repetition"):
    sns.set(rc={'figure.figsize': (20, 11)})
    x = range(1, len(data) + 1)
    y = data

    plt.plot(x, data, marker='x', linestyle='--',label=nreplablel, color='b')
    plt.axhline(np.mean(y), color='r', linestyle='--', label='Average')

    # Adding labels and title
    plt.xlabel(f"Repetitions (N={N})", fontsize=30)
    plt.ylabel('Execution time (Seconds)', fontsize=30)
    plt.title(title, fontsize=30)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    # Adding legend
    plt.legend()

    # Display the plot
    st.pyplot()


def _fetch_data_gdb(sparql, sparql_query, N):

    if sparql:
        execution_time_lst = []
        try:
            # Set SPARQL query parameters
            sparql.setMethod(GET)
            sparql.setQuery(sparql_query)
            sparql.setReturnFormat(JSON)

            # Execute the query and measure execution time
            for i in range(N+1):
                start_time = time.time()
                result = sparql.query().convert()
                end_time = time.time()
                execution_time = end_time - start_time
                execution_time_lst.append(execution_time)

            # Return results and execution time
            with open("result.json", "w") as json_file:
                json.dump({"execution_time": execution_time_lst, "result": result}, json_file)
            return True
        except Exception as e:
            # query execution errors
            print(f"Error: {str(e)}")
            return f"Error: {str(e)}"
    else:
        # connection failure
        return "Error: Failed to connect to the graph database."