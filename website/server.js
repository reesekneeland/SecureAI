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

//exec libarary
const spawn = require("child_process").spawn;

// Bcrypt library for comparing password hashes
const bcrypt = require('bcrypt');

//const path = require("path/posix");
var path = require('path');

app.use(bodyparser());

app.use(express.static('images'));
app.use(express.static('client'));

// server listens on port 9007 for incoming connections
app.listen(9007, () => console.log('Listening on port 9007!'));

// function to return the index page
app.get('/', function (req, res) {
    res.sendFile(__dirname + '/client/index.html');
})

// function to return the index page
app.get('/index', function (req, res) {
    res.sendFile(__dirname + '/client/index.html');
});

// function to return the gallery page
app.get('/gallery', function (req, res) {
    res.sendFile(__dirname + '/client/gallery.html');
});

// function to return the add Image page
app.get('/addImage', function (req, res) {
    res.sendFile(__dirname + '/client/addImage.html');
});

// function to return the add event page
app.post('/send_password', function (req, res) {

    fs.readdir(dire, (err, files) => {
        counter = files.length;
        let password = req.body.password;
        const python = spawn('python3', ['script.py', password, (counter + 1)]);
    })


    //DELETE THIS AFTER IT JST TRACKS BUFFER FROM PYTHONs
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
        console.log(dataToSend);
    });

    res.redirect("/gallery");
});

app.get('/getImages', function (req, res) {

    counter = 0;
    const dire = './images';
    fs.readdir(dire, (err, files) => {
        counter = files.length;
        res.send({ num: counter });
    })

});

// middle ware to serve static files
app.use('/client', express.static(__dirname + '/client'));

// function to return the 404 message and error to client
app.get('*', function (req, res) {
    // add details
    res.sendStatus(404);
});