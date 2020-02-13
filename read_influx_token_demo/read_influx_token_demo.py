import getpass
import random
import time
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakAuthenticationError


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


# A method for quering the database with the given token
def querydata(token, hostname, query):
    
    # An example of a query
    # q = "SELECT * FROM acea_test_db WHERE time > now() - 15s&db=acea_test_db"

    response = requests.get("https://" + hostname + ":30223/query?q=" + query,
                            verify=False,
                            headers={'Authorization': "Bearer " + token})

    # For this demo, simply log out the data to the terminal. Though it's reasonable to assume you would want to use this data for something
    if response.status_code >= 300:
        print("Error in fetching data. Server says " + response.text)
        exit(1)
    print(response.text)


# Main method for the application
if __name__ == "__main__":

    # Prompt the user for their credentials. This user should have at least 'read' privledges.
    hostname = input("Please provide the hostname for Lumada Appliance (eg. 10.76.56.106): ")
    username = input("Please provide a username: ")
    pwd = getpass.getpass(prompt='Please enter the password for the user: ', stream=None)
    query = input("Please provide your Influx query: ")

    # Fetch the token
    token = gettoken(hostname=hostname, username=username, password=pwd)

    # Parse out Access Token
    access_token = token["access_token"]

    # Make sure the token isn't invalid
    if token is None:
        print("Unable to fetch token.")
        exit(1)
        
    # Make a query to fetch the data that was just published
    querydata(access_token, hostname, query)