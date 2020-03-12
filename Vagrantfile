# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<-'SCRIPT'
    yum update
    sudo yum install python3 -y
    sudo python3 -m pip install flask
    sudo python3 -m pip install requests
    cd /vagrant/
    python3 app.py
SCRIPT

Vagrant.configure("2") do |config|

  config.vm.box = "centos/7"

  config.vm.provision "shell", inline: $script
  config.vm.network "forwarded_port", guest: 5000, host: 5000

end
