#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error('Error: No movie ID provided');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    if (data.title) {
      console.log(data.title);
    } else {
      console.error('Error: Movie not found');
    }
  }
});
