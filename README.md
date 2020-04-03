# weather-api: Deployable Local Python Weather API

## NOTE: This project is a coding example for a job interview and does not provide any real world functionality. 

This repo contains code to deploy a vagrant box using Centos that runs a local endpoint to get the current temperature for a provided city and state. The endpoint will return a current temperature value and a value for the time the endpoint was queried. 

Data from API queries is stored in a SQLite table called temperature_api_sqlite.db and contains logic to pull the most recent temperature for a city/state if that last call was within the last 5 minutes. If not, it will reach out to OpenWeatherMap and get the current temperature. 

## Installing Vagrant and hypervisor dependencies

Visit the Vagrant downloads page and download the respective installer for your given OS: https://www.vagrantup.com/downloads.html

Virtualbox is the hypervisor used by default regardless of host OS. Ensure virtualbox is installed and enabled: https://www.virtualbox.org/

## Launching the Vagrant box

In terminal, change directory in to desired folder and clone repo

```
git clone https://github.com/roguebones/weather-api.git
```

Change directory in to newly created folder

```
cd weather-api
```

Launch the vagrant box

```
vagrant up
```

## Calling the API

Endpoint runs locally at 127.0.0.1 and port 5000. 

To get the current temperature for a city, reference endpoint "/temperature" and pass a city and state parameter.

### Parameters (required)

city: Accepts a valid valid city name

state: Accepts a valid full state name (not state code)

Note that the city and state must be a real, valid location in the USA.  

### Example GET request
```
http://127.0.0.1:5000/temperature?city=Portland&state=Oregon
```

### Response:

query time: timestamp of request date/time

temperature: current temperature in farenheit of city/state


```
{
 "query_time":"2020-03-12 04:12:00.752685",
 "temperature":"43.41"
}
```
