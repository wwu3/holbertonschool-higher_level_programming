#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const films = JSON.parse(body).results;
  console.log(films);
  const charactersInFilms = films.map((film) => film.characters);
  console.log(charactersInFilms);
  const countId = charactersInFilms.filter((film) => film.filter(
    character => character.includes('/18/')
  ).length > 0).length;
  console.log(countId);
});
