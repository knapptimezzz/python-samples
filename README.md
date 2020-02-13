# Python Demo Apps

This repository contains several Python programming samples for interaction and interfacing with Hitachi Vantara Lumada Edge Intelligence platform. These samples include how to fetch tokens from the platform, how to create applications that determine thresholds, how to throw Lumada Edge Intelligence Alerts, and more.

The following sections outline the different samples included in this repository.

## Python Version

This app conforms with the Python3 standards the team have chosen. The team's standard are to use Python 3.7+. Of course the latest version of Python 3 should work perfectly fine.

## Docker and K8s Examples

For more in-depth understanding of Docker, Docker files, Docker container building, deployment files, and deploying to Kubernetes, please see the [Deduplication Demo Documentation](deduplication_demo/README%20Deduplication%20Demo.md).

## Write and Read to InfluxDB with Tokens

This application communicates with the auth manager for the platform. It provides a sample on how to connect and communicate, fetch a token, and use the Passport API service. Our Passport API service provides a REST endpoint to connect and communicate with all of the databases on the platform using a standard authorization process. It provides three main learning points: fetching an authorization token, using the token to publish data, and using the token to fetch that published data.

[Token Demo Documentation](write_read_influx_token_demo/README%20Token%20Demo.md)

Note: This application is designed to run on your local machine.

## Data Pump App

This demo application is a standalone application that generates a Lumada Edge Intelligence Common Data Model (Protobuf Model) that can be sent through the system. It's a great way to test that data is recieved by the system. Additionally, with minimal modification, you can send your own data through the system as a generator. It should be noted that this is a demo application and should not be used for production without additional modification.

[Data Pump Demo Documentation](data_pump_demo/README%20Data%20Pump%20Demo.md)

Note: This application is designed to run on your local machine.

## Threshold App

A common use case for custom applications would be threshold analysis. This is to say that there are instances in which incoming data should be measured, and compared with preset values indicating that a value is aboved a desired limit. In such a case you may wish to trigger and alert, send a message to another system, or automatically create a repair ticket. This demo will illustrate what it takes to deploy a custom application that reads a stream of data through the Lumada Edge Intelligence platform and runs a comparison on the values and takes a simple action of logging and alert to the platform.

[Threshold Demo Documentation](threshold_demo/README%20Threshold%20Demo.md)

Note: This application is designed to run insided a docker container on the Lumada Edge Intelligence Platform.

## Data Deduplication App

Another common used case is the desire to reduce the amount of data that needs to be saved, especially for incoming data that is repeated for a long period of time. For example, a sensor is measuring the stat of a door where 1 is open and 0 is closed. In most cases, the door will be in one of those states for a long period of time requiring the storage of unecessary data. It is this example, that we have a "deduplication" or "dedupe" app. What this application does is read in current piece of information, if it's the same as the previous value, then it will discard the new value. If the value is different, it will forward on the new value with timestamp to the data base and update its local variable to reflect this. This application is designed to work in conjunction with the data pump. Please set up that application first or if you have an understanding of routes and have your own data, you may tailor this right away to suit your needs.

[Deduplication Demo Documentation](deduplication_demo/README%20Deduplication%20Demo.md)

Note: This application is designed to run insided a docker container on the Lumada Edge Intelligence Platform.

## Read Influx Token Demo

This Influx demo is a simplier version of the Influx demo listed above. It provides the same access to Influx via the Passport API service but this is a simple read / query application. In this sample you will use the Lumada Edge Intelligence auth manager to fetch a token and execute a customizable query again Influx. This will most likely be a faily common task for your applications to query data from Influx and performing some action based on the contents of that data.

[Read Influx Token Demo Documentation](read_influx_token_demo/README%20Read%20Influx%20Token%20Demo.md)

Note: This application is designed to run on your local machine.

## That's It!

Happy Programming!!

Programmed with :heart: by Hitachi Vantara :nerd_face: s
