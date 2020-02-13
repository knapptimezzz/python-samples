# InfluxDB Data Publish and Read (with tokens)

This documentation will cover how to use the sample to test our Passport API's with tokens. The following script is intended to be run from a local machine. Though it's possible to modify it for deployment in a container or it can be used in other Python applications running in a webserver for example.

## Application Overview

After working with this demo, you should have a better understanding of:

1. Fetching a token from the Lumada Edge Intelligence Platform
1. Use a token to interface with InfluxDB
    * Create a database if it doesn't exist
    * Access the database
1. Add data to the database by generating sample data
1. Make a query to InfluxDB (with time boxed parameters). (This is a sample query and can be modified to meet the data you have.)

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
    python3 write_read_influx_token_demo.py
    ```

1. The application will then prompt for the load balancer IP address or the single node IP address of where the Lumada Edge Intelligence software is running.
1. The application will then prompt for the user name for the admin
1. The application will then prompt for the password for the user
1. Upon successfully entering this information, the application will
    * Fetch a token
    * Create a simple set of data to post to Influx
    * Execute a simple query to fetch the data that was just entered.

Assuming you have a valid Influx Line Protocol query (more information about ILP can be found [here](https://docs.influxdata.com/influxdb/v1.7/write_protocols/line_protocol_tutorial/)), the following code will publish data to Influx using the passport service.

```python
response = requests.post("https://" + hostname + ":30223/write", verify=False, params={'db': 'acea_test_db'}, headers={'Authorization': "Bearer " + token}, data=data)
```

Again, assuming you have a valid Influx query (more information can be found [here](https://docs.influxdata.com/influxdb/v1.7/guides/querying_data/)), you can fetch data with the following request to the passport service.

```python
response = requests.get("https://" + hostname + ":30223/query?q=" + q, verify=False, headers={'Authorization': "Bearer " + token})
```

Programmed with :heart: by Hitachi Vantara :nerd_face: s
