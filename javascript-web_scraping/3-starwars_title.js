#!/usr/bin/node
const requestURL = 'https://swapi-api.hbtn.io/api/films/:id';
const request = require('request');
const id = process.argv[2];
request(requestURL.replace(':id', id), (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
