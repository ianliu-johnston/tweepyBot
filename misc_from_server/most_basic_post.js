#!/usr/bin/env nodejs
var http = require('http');
http.createServer(function (request, response) {
	if (request.method === "GET") {
		response.writeHead(200, {'Content-Type': 'text/plain'});
		response.write("lala\n");
		response.end();
		console.log('Got a GET\n');
	} else if (request.method === "POST"){
		var requestBody = '';
		request.on('data', function(data){
			requestBody += data;
			response.writeHead(200, {'Content-Type': 'text/plain'});
			response.end("Dada\n");
		});
		request.on('end', function(){
			console.log('Got a POST\n');
			console.log(requestBody);
		});
	}
}).listen(8080, '138.68.1.168');
console.log("Server is now running");
