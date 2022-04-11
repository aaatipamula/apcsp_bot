#!/bin/sh

if [ -f ./scripts/Dockerfile_apcsp_bot ]
then 

    if [ -f ./scripts/Dockerfile_mysql ]
        then
            echo 'Building main docker container image...'
            sudo docker build -t bot -f ./scripts/Dockerfile_apcsp_bot . 

            echo 'Building MySQL container image...'
            sudo docker build -t bot-mysql -f ./scripts/Dockerfile_mysql .

            echo 'Creating network...'
            sudo docker network create bot-net

            echo 'Starting containers...'
            sudo docker run -it --name bot-mysql --network bot-net -d bot-mysql
            sudo docker run -it --name bot --network bot-net -d bot
            sudo docker cp ./src/data.json bot:/home/bot/apcsp_bot/src/
    fi

fi