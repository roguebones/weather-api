# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<-'SCRIPT'
    yum update
    sudo yum -y groupinstall "Development Tools"
    sudo yum -y install openssl-devel bzip2-devel libffi-devel
    sudo yum -y install wget
    wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
    tar xvf Python-3.8.2.tgz
    cd Python-3.8*/
    ./configure --enable-optimizations
    sudo make altinstall
    python3.8 -m pip install flask --user
    python3.8 -m pip install requests --user
SCRIPT

Vagrant.configure("2") do |config|

  config.vm.box = "centos/7"

  config.vm.provision "shell", inline: $script
  config.vm.network "forwarded_port", guest: 80, host: 8080



end
