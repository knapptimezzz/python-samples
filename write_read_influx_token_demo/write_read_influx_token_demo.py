import getpass
import random
import time
from datetime import datetime, timedelta
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakAuthenticationError

influx_passport_port_no = 30223


def gettoken(hostname=None, username=None, password=None):
    url = "https://" + str(hostname) + ":30443/auth/"

    # You'll want to determine ahead of time what your client is and the credentials for that client in order to fetch a token for your user.
    kclient = KeycloakOpenID(server_url=url,
                             client_id="hiota",
                             client_secret_key="Change11me",
                             realm_name="hiota",
                             verify=False)

    try:
        token = kclient.token(username, password)
    except KeycloakAuthenticationError as e:
        print("Error encountered trying to fetch token" + e)
        exit(1)

    return token


# Simple method to publish data to the database so that the sample query can pull some data.
def postinfluxdata(token, hostname=None):

    db_create_response = requests.post("https://" + hostname + ":" + influx_passport_port_no + "/query",
                             verify=False,
                             params={'q': 'CREATE DATABASE "acea_test_db"'},
                             headers={'Authorization': "Bearer " + token})

    # Indicates how many records that need to be created. Increase this number to generate more samples or decrease it to lower the number of samples.
    time_window = 10

    # Generate dummy data
    start_time = time.time_ns()
    for i in range(0, time_window):

        local_time = start_time - (time_window + i) * 1000000000

        # This fake piece of data in Influx Line Protocol format
        data = "acea_test_db sensor_001=" + str(random.randint(0, 1)) + " " + str(local_time)

        response = requests.post("https://" + hostname + ":" + influx_passport_port_no + "/write",
                                 verify=False,
                                 params={'db': 'acea_test_db'},
                                 headers={'Authorization': "Bearer " + token},
                                 data=data)

        print(response)


# A method for quering the database with the given token
def querydata(token, hostname):
    
    # Define your query. For this example, it's tied to access the data that was just generated. You'll want to make sure that your database matches where you're storing your data.
    # Additionally, this query is hard coded to look for a time window of now - 15 seconds. You'll want to modify this time to suit your needs.
    q = "SELECT * FROM acea_test_db WHERE time > now() - 15s&db=acea_test_db"

    response = requests.get("https://" + hostname + ":30223/query?q=" + q,
                            verify=False,
                            headers={'Authorization': "Bearer " + token})

    # For this demo, simply log out the data to the terminal. Though it's reasonable to assume you would want to use this data for something
    print(response.text)


# Main method for the application
if __name__ == "__main__":

    # Prompt the user for their credentials. This user should have at least 'read' privledges.
    hostname = input("Please provide the hostname for Lumada Appliance (eg. 10.76.56.106): ")
    username = input("Please provide a username: ")
    pwd = getpass.getpass(prompt='Please enter the password for the user: ', stream=None)

    # Fetch the token
    token = gettoken(hostname=hostname, username=username, password=pwd)

    # Parse out Access Token
    access_token = token["access_token"]

    # Make sure the token isn't invalid
    if token is not None:
        print("Obtained a valid token.")
    else:
        print("Unable to fetch token.")
        exit(1)

    # Publish sample data to Influx using the API (Passport API) with the token you just returned
    postinfluxdata(access_token, hostname=hostname)

    # Make a query to fetch the data that was just published
    querydata(access_token, hostname)
