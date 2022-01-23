
// include the express modules
var express = require("express");

// create an express application
var app = express();
const url = require('url');

// helps in extracting the body portion of an incoming request stream
var bodyparser = require('body-parser');

// fs module - provides an API for interacting with the file system
var fs = require("fs");

// helps in managing user sessions
var session = require('express-session');

// Bcrypt library for comparing password hashes
const bcrypt = require('bcrypt');

// server listens on port 9007 for incoming connections
app.listen(9007, () => console.log('Listening on port 9007!'));

// function to return the welcome page
app.get('/',function(req, res) {
    res.sendFile(__dirname + '/client/index.html');
})
  
// function to return the welcome page
app.get('/index',function(req, res) {
    res.sendFile(__dirname + '/client/index.html');
});

// middle ware to serve static files
app.use('/client', express.static(__dirname + '/client'));

// function to return the 404 message and error to client
app.get('*', function(req, res) {
  // add details
  res.sendStatus(404);
});