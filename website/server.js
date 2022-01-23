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
let passNum;
// function to return the add event page
app.post('/send_password', function (req, res) {
    const dire = './images';
    fs.readdir(dire, (err, files) => {
        counter = files.length;
        let password = req.body.password;
        let username = req.body.name_user;
        //console.log(username);
        const python = spawn('python3', ['generateImage.py', password, (counter + 1)]);
        python.stdout.on('data', function (data) {
            // console.log('Pipe data from python script ...');

            dataToSend = data.toString();
            console.log(dataToSend);
        });

            fs.readFile('score.txt', function (err, data1) {
                if (err) {
                    throw err;
                }
                passNum = data1;
                console.log("Here is the data: " + passNum);
            });

            fs.readFile('client/data.json', function (err, jsonData) {
                if (err) {
                    throw err;
                }
                //  Parse the schedule.json file and
                //  the post request with
                let jsonFileData = JSON.parse(jsonData);
                let newJsonContent = {
                    user: username, counter: (counter + 1), strength: passNum.toString(), likes: 0
                };
                console.log(newJsonContent)
                jsonFileData.posts.push(newJsonContent);

                fs.writeFile("client/data.json", JSON.stringify(jsonFileData, null, 3), function (err) {
                    if (err) {
                        throw err;
                    }
                });
            });
    });

    res.redirect("/gallery");
});

app.post('/updateLike', function (req, res) {

    fs.readFile('client/data.json', function (err, jsonData) {
        if (err) {
            throw err;
        }
        //  Parse the schedule.json file and
        //  the post request with
        let jsonFileData = JSON.parse(jsonData);
        jsonFileData.posts[req.body.item-1].likes++;

        fs.writeFile("client/data.json", JSON.stringify(jsonFileData, null, 3), function (err) {
            if (err) {
                throw err;
            }
        });
        
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