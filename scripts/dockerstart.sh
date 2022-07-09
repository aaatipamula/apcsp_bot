#!/bin/sh

if [ -f ./scripts/Dockerfile ]
then 

        echo 'Building main docker container image...'
        sudo docker build -t bot -f ./scripts/Dockerfile . 

        echo 'Starting containers...'
        sudo docker run -it --name bot -d bot
    
else
    echo 'Please navigate to the home directory of this project'
    exit

fi