#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request (url, function (error, response, body) {
  if(err) {
    console.error(err);
  }
  console.log({'status code'})
});

