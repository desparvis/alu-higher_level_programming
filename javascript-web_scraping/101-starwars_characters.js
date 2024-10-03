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

    characters.forEach((characterUrl) => {
      request(characterUrl, (err, response, body) => {
        if (err) {
          console.error(err);
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  } else {
    console.log('Movie not found or invalid ID.');
  }
});
