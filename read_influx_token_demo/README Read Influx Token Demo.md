# Read Influx Token Demo

This demo works to show a simple example of just fetching a token and reaching data from influx through our Passport API (Passport Service). The passport service is a service that provide token authentication to all of our databases in the system by requiring and validating that each request contain an Authorization token for the user. Then enables security on the databases as well as provides a unified means of accesing the data on all the database.

## Application Overview

After working with this demo, you should have a better understanding of:

1. How to fetch a token from the Keycloak service running on the machine
1. How to make a query using that token to the passport service for Influx

## Running the Application

### Install the Libraries

Next you will need Python libraries.

1. Run the following command

    ```bash
    pip3 install -r requirements.txt
    ```

    This might take a few minutes depending on your internet connection.

### Start the Demo

1. Open a new terminal window (or if you are versed in an IDE, you may open this with your favorite tool)
1. Navigate to where this directory is
1. Run the application by typing the following:

    ```bash
    python3 read_influx_token_demo.py
    ```

1. The application will then prompt for the load balancer IP address or the single node IP address of where the Lumada Edge Intelligence software is running.
1. The application will then prompt for the user name for the admin
1. The application will then prompt for the password for the user
1. Finally the application will prompt for the query that you would like to execute through the Passport service to Influx.
1. Upon successfully entering this information, the application will
    * Fetch a token
    * Execute a simple query to fetch the data that was just entered.

Assuming you have a valid Influx query (more information can be found [here](https://docs.influxdata.com/influxdb/v1.7/guides/querying_data/)), you can fetch data with the following request to the passport service.

```python
response = requests.get("https://" + hostname + ":30223/query?q=" + q, verify=False, headers={'Authorization': "Bearer " + token})
```

Programmed with :heart: by Hitachi Vantara :nerd_face: s