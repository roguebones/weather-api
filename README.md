# weather-api: Deployable Local Python Weather API
This repo contains code to deploy a vagrant box using Centos that runs a local endpoint to get the current temperature for a provided city and state. The endpoint will return a current temperature value and a value for the time the endpoint was queried. 

## Installing Vagrant and hypervisor dependencies

Visit the Vagrant downloads page and download the respective installer for your given OS: https://www.vagrantup.com/downloads.html

Virtualbox is the hypervisor used by default regardless of host OS. Ensure virtualbox is installed and enabled: https://www.virtualbox.org/

## Launching the Vagrant box

clone repo

cd in to repo folder

vagrant up

## Calling the API

http://127.0.0.1:5000/temperature?city=Portland&state=Oregon
