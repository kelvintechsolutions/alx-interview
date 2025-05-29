#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(filmUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode}`);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;
  const characterNames = new Array(characters.length);
  let completedRequests = 0;

  characters.forEach((characterUrl, index) => {
    request(characterUrl, function (err, res, body) {
      if (err) {
        console.error('Error:', err);
        process.exit(1);
      }

      if (res.statusCode !== 200) {
        console.error(`Error: Received status code ${res.statusCode} for ${characterUrl}`);
        process.exit(1);
      }

      const characterData = JSON.parse(body);
      characterNames[index] = characterData.name;
      completedRequests++;

      if (completedRequests === characters.length) {
        characterNames.forEach(name => {
          console.log(name);
        });
      }
    });
  });
});
