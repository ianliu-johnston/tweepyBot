# A Simple Server for POC
Runs on Nodejs and processes get, post and put requests. Displays a simple HTML login page, and logs the requests.

## Steps: 
1. Create the nodejs server, and have it listen on port 8080.
2. Not all browsers will want to connect to port 8080, so use IP tables to map 8080 to 80. ``sudo iptables -t nat -A PREROUTING -t nat -p tcp --dport 80 -j REDIR --to-port 8080``
3. Buy a domain name and point it at the servers your hosting provider is on.
