#!/usr/bin/env bash
#Sets up web servers for the deployment of web_static
sudo apt -y update
sudo apt -y install nginx
sudo service nginx start

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo -e "Hey I Found You!" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '55i\\tlocation /hbnb_static/ {n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
