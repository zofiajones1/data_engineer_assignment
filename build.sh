#!/usr/bin/env bash

echo "Build and data download might take some time..."

python3 -m venv ./venv
./venv/bin/python -m pip install pip --upgrade
./venv/bin/python -m pip install -e src

echo -n "Have you downloaded the data?(Y/n):"
read -r reply

echo -n "Do you want to try transmission-cli(Ubuntu)?  You may need to stop the process manually once its finished downloading tar and restart script.(Y/n)"
read -r  transmission

echo "Jpgs will be available in data directory."

if [ $reply == "Y"  ];then
		echo -n "Please paste the directory with downloaded tar file. No (~):"
		read -r datapath

                if [ ! -d data  ];then
                mkdir data
                fi

		file=$datapath"/apod.tar"
		echo $file
		if test -f "$file";then
			echo "Tar file found.  Untarring..."
			tar -xvf $file -C data

		else
			echo "Tar file not found.  Downloading torrent file."
			wget https://academictorrents.com/download/5f755e078ee9195b8ae0b3336710e6ce92ef3251.torrent
			if [ ! -d data  ];then
				mkdir data
			fi
			if [ ! data/apod.tar  ];then
                        if [ $transmission == "Y"   ];then
                        echo "Downloading tar using transmission-cli... You may need to exit manually once complete and restart script."
                        sudo apt install transmission-cli
			stop_script="killall transmission-cli"
			transmission-cli -f $stop_script 5f755e078ee9195b8ae0b3336710e6ce92ef3251.torrent -w data
                        else
                        echo "Please download torrent from https://academictorrents.com/download/5f755e078ee9195b8ae0b3336710e6ce92ef3251.torrent."
                        fi
			fi
			if [ data/apod.tar  ];then
			tar -xvf data/apod.tar -C data
			fi
		fi

elif [  $reply == "n"  ];then
		mkdir data
		datapath="data"
                if [ $transmission == "Y"   ];then
                echo "Downloading tar using transmission-cli... You may need to exit manually once complete and restart script."
                wget https://academictorrents.com/download/5f755e078ee9195b8ae0b3336710e6ce92ef3251.torrent
                sudo apt install transmission-cli
                stop_script="killall transmission-cli"
                nohup transmission-cli 5f755e078ee9195b8ae0b3336710e6ce92ef3251.torrent -w data -f finish.sh  -p 51418
                tar -xvf data/apod.tar -C data
                else
                echo "Please download torrent from https://academictorrents.com/download/5f755e078ee9195b8ae0b3336710e6ce92ef3251.torrent."
                fi

else
	echo "Response not recognised."
	exit 1
fi

echo "Number of jpgs in data directory:"
eval "ls "$datapath"/apod/" | grep jpg | wc -l

echo "Is docker installed?"
docker_check=$(which docker | wc -l)
if [ $docker_check == 0  ];then
echo "Installing docker..."
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo groupadd docker
USER=$(whoami)
sudo gpasswd -a $USER docker
docker run hello
else
echo "Docker is installed."
fi


echo "JPG_DIR="$(pwd)"/data/apod/" >> .env

mkdir xml_files

echo "XML_DIR="$(pwd)"/xml_files/" >> .env

echo "PASSWORD=secretpassword" >> .env
echo "DATABASE=application" >> .env
echo "DB_USER=application" >> .env
