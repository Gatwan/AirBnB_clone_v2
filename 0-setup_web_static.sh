#!/usr/bin/env bash
#Sets up web servers for the deployment of web_static
sudo apt -y update
sudo apt -y install nginx
sudo service nginx start

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo -e "Hey I Found You!" | sudo tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '95i\\tlocation /hbnb_static/ {n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
