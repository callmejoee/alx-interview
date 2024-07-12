#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  const data = JSON.parse(body);
  const characterUrls = data.characters;

  // Fetch all character data and print in order
  const characterPromises = characterUrls.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          reject(charError);
          return;
        }

        if (charResponse.statusCode !== 200) {
          reject(new Error(`Failed to fetch character data. Status code: ${charResponse.statusCode}`));

          return;
        }

        const characterData = JSON.parse(charBody);
        resolve(characterData.name);
      });
    });
  });

  Promise.all(characterPromises)
    .then((characterNames) => {
      characterNames.forEach((name) => console.log(name));
    })
    .catch((err) => {
      console.error('Error:', err);
    });
});
