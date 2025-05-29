#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error) return console.error(error);

  const film = JSON.parse(body);
  const characters = film.characters;

  printCharactersInOrder(characters, 0);
});

function printCharactersInOrder(characters, index) {
  if (index >= characters.length) return;

  request(characters[index], (err, res, body) => {
    if (!err) {
      const character = JSON.parse(body);
      console.log(character.name);
      printCharactersInOrder(characters, index + 1);
    } else {
      console.error(err);
    }
  });
}
