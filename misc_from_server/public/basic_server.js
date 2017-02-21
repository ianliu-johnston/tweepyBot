#!/usr/bin/env nodejs
var http = require("http")
	url = require("url")
	fs = require("fs");
const express = require('express');
const favicon = require('express-favicon');
const app = express();

app.use(favicon(__dirname + "/favicon.ico"));
function get_info(request, response)
{
	var getpath = url.parse(request.url).pathname;
	var datetime = new Date();
	console.log("---BEGIN---");
	console.log("\t" + datetime);
	console.log("\tNew Connection " + request.connection.remoteAddress + " -> " + request.headers['host']);
	console.log("\tUser Agent: " + request.headers['user-agent']);
	console.log("\tRequested Resource: " + request.url);
	console.log("\tRequest Method: " + request.method);
	console.log("\tAccept: " + request.headers['accept']);
	console.log("\tContent Type: " + request.headers['content-type']);
	console.log("\tContent Length: " + request.headers['content-length']);
}
/*
	response.setHeader('Content-Encoding', "gzip");
	response.setHeader('Content-Type', "text/html; charset=utf-8");
	response.setHeader('Cache-Control', "max-age=0, private, must-revalidate");
	response.setHeader('X-Content-Type-Options', "nosniff");
	response.setHeader('X-XSS-Protection', "1; mode=block");
	response.setHeader('X-Frame-Options', "SAMEORIGIN");
 */
http.createServer(function (request, response) {
	var getpath = url.parse(request.url).pathname;
	var full_path = __dirname + getpath;
	var requestBody = '';
	response.setHeader('Host', "intranet.hbtn.io");
	response.setHeader('Server', "nginx/1.8.0");
	response.setHeader('Connection', "keep-alive");
	if (request.method === "POST")
	{
		get_info(request, response);
		request.on('data', function(data){
			response.writeHead(200, {'Content-Type': "text/html; charset=utf-8"});
			requestBody += data;
			fs.readFile(__dirname + "/auth/sign_in", "binary", function(err, home){
				response.end(home, "binary");
			})
		});
		request.on('end', function(){
			console.log("\tRequest Body:");
			console.log(requestBody);
		});
	}
	else if (request.method === "PUT")
	{
		get_info(request, response);
		request.on('data', function(data){
			requestBody += data;
			response.writeHead(200, {'Content-Type': 'text/plain'});
			response.end("Dada\n");
		});
		request.on('end', function(){
			console.log("\tRequest Body:");
			console.log(requestBody);
		});
	}
		else if (request.method === "GET")
		{
			if (full_path === __dirname + '/' || full_path === __dirname + "/auth/sign_in")
			{
				get_info(request, response);
				fs.readFile(__dirname + "/auth/sign_in", "binary", function(err, file){
						response.write(file, "binary");
						response.end();
				})
			}
			else
			{
				fs.readFile(full_path, "binary", function(err, file){
					if(err){
						fs.readFile(__dirname + "/404", "binary", function(err, fourofour){
							response.writeHead(404, {'Content-Type': 'text/html'});
							response.write(fourofour, "binary");
							response.end();
						})
					}
					else
					{
						response.write(file, "binary");
						response.end();
					} 
				})
			}
	}
}).listen(8080, '172.31.19.207');
console.log("Server is now running");
process.on('uncaughtException', function(err){ console.log(err);})
