#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error('Error: No Movie ID provided');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  const printCharacterNames = (index) => {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], (error, response, body) => {
      if (error) {
        console.error(`Error: ${error}`);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
      printCharacterNames(index + 1);
    });
  };

  printCharacterNames(0);
});
