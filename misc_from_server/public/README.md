# A Simple Server for POC
Runs on Nodejs and processes get, post and put requests. Displays a simple HTML login page, and logs the requests.

## My Setup:
* Digital ocean server running Ubuntu LTS v. 14.04
* 20Gb storage, 512mb ram, 1 core.
* 

## Steps: 
0. Install Dependencies: 
  0. ``sudo apt-get install nodejs nodejs-dev npm``
  1. Make the working directory a node project. ``npm init``. 
  2. You will be guided through the process of creating the basic config file. 
  3. Finally save the folder in the dependencies list: ``npm install express --save``
1. Create the nodejs server, and have it listen on port 8080.
2. Not all browsers will want to connect to port 8080, so use IP tables to map 8080 to 80. ``sudo iptables -t nat -A PREROUTING -t nat -p tcp --dport 80 -j REDIR --to-port 8080``
3. Buy a domain name and point it at the servers your hosting provider is on. [Point your domain name to your IP address](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-host-name-with-digitalocean)
4. Install TLS/SSL [EFF Certbot](https://certbot.eff.org/#ubuntutrusty-other)
