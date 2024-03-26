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
# @File    : gdb_connection_manager.py
# @Software: PyCharm
from SPARQLWrapper import SPARQLWrapper, BASIC, GET, JSON, POST
def _connect_gdb(connection_details, request_type="get"):
    """
    Connects to a graph database using the provided connection details.

    Parameters:
    - connection_details (dict): A dictionary containing connection details.
      Expected keys: 'username', 'password', 'hostname', 'repository'.
    - request_type (str): The type of request ('get' or 'post').

    Returns:
    - SPARQLWrapper: An instance of SPARQLWrapper configured for the specified request type.
    """
    print(connection_details)
    print("*"*100)
    username = connection_details.get("username")
    password = connection_details.get("password")
    hostname = connection_details.get("hostname")
    repository = connection_details.get("repository")

    if not (username and password and hostname and repository):
        raise ValueError("Connection parameters missing.")

    if request_type == "get":
        endpoint = f"{hostname}/repositories/{repository}"
    elif request_type == "post":
        endpoint = f"{hostname}/repositories/{repository}/statements"
    else:
        raise ValueError("Invalid request type. Use 'get' or 'post'.")

    try:
        sparql = SPARQLWrapper(endpoint)
        sparql.setHTTPAuth(BASIC)
        sparql.setCredentials(username, password)
        return sparql
    except Exception as e:
        raise ConnectionError(f"Failed to connect to the graph database: {str(e)}")

def check_sparql_connection(sparql):
    try:
        sparql.setQuery('SELECT * WHERE {?s ?p ?o} LIMIT 1')
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        if len(results["results"]["bindings"]) > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error:{e}")
        return False