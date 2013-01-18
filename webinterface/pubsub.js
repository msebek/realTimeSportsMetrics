const PORT = 3000;
const HOST = 'localhost';
var express = require('express');

// Apps are no longer servers.
//var app = module.exports = express.createServer();
var http = require('http');
var app = express();

// Changed from staticProvider to static.
//  https://github.com/visionmedia/express/issues/589
app.use(express.static(__dirname + '/public'));

var redis = require('redis');
var client = redis.createClient();

var io = require('socket.io');

if (!module.parent) {
    //app.listen(PORT, HOST);

    // See below for changes.
    var appserver = http.createServer(app).listen(PORT, HOST);
    //appserver.address()

    // After express version X, apps are no longer servers.
    // https://github.com/visionmedia/express/issues/1136
    //console.log("Express server listening on port %d", app.address().port)
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
