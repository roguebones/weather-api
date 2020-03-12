# weather-api: Deployable Local Python Weather API
This repo contains code to deploy a vagrant box using Centos that runs a local endpoint to get the current temperature for a provided city and state. The endpoint will return a current temperature value and a value for the time the endpoint was queried. 

# Installing Vagrant and hypervisor dependencies

install vagrant

# Launching the Vagrant box

clone repo

cd in to repo folder

vagrant up

# Calling the API

http://127.0.0.1:5000/temperature?city=Portland&state=Oregon
