#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

if (!apiUrl) {
  console.error('Error: No API URL provided');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach(film => {
      film.characters.forEach(characterUrl => {
        if (characterUrl.includes(`/api/people/${characterId}/`)) {
          count++;
        }
      });
    });

    console.log(count);
  }
});
