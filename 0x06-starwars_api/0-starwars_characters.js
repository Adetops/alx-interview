#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Make API request
request(filmURL + movieId, async (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  try {
    // Parse response body
    const filmData = JSON.parse(body);

    // Extract character URLs
    const charURLList = filmData.characters;

    // Iterate over character URLs and make requests
    for (const charURL of charURLList) {
      await new Promise((resolve, reject) => {
        request(charURL, (err, res, body) => {
          if (err) {
            console.error('Error:', err);
            reject(err);
            return;
          }

          // Parse character data and print name
          const charData = JSON.parse(body);
          console.log(charData.name);
          resolve();
        });
      });
    }
  } catch (error) {
    console.error('Error:', error);
  }
});
