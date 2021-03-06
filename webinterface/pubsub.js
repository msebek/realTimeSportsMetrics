const PORT = 3000;
const HOST = 'localhost';
var express = require('express');

var http = require('http');
var app = express();

app.use(express.static(__dirname + '/public'));

var redis = require('redis');
var client = redis.createClient();

var io = require('socket.io');

if (!module.parent) {

    var appserver = http.createServer(app).listen(PORT, HOST);
    console.log("Express server listening on port %d", PORT)

    var socket  = io.listen(appserver);

    socket.on('connection', function(client) {
        var subscribe = redis.createClient();
        subscribe.subscribe('foo');
        
        subscribe.on("message", function(channel, message) {
            console.info("hello!");
            client.send(message);
        });


        client.on('disconnect', function() {
            subscribe.quit();
        });
    });
}
