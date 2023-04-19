#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const films = JSON.parse(body).results;
  const characters = films.map((film) => film.character);
  console.log(characters);
  const countId = characters.filter((character) => character.include('/18/'));
  console.log(countId);
});
