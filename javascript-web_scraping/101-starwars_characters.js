#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const data = JSON.parse(body);

  if (data.title) {
    const characters = data.characters;

    if (characters.length === 0) {
      console.log('Characters not found');
      return;
    }

    let count = 0;
    characters.forEach((characterUrl) => {
      request(characterUrl, (err, response, body) => {
        if (err) {
          console.error(err);
          return;
        }

        count++;
        if (count === characters.length) {
          console.log('OK');
        }
      });
    });
  } else {
    console.log('Movie not found or invalid ID.');
  }
});
