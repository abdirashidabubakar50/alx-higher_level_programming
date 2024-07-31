#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Error: URL and file path must be provided');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(`Error: ${err}`);
      }
    });
  }
});
