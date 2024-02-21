#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    response = JSON.parse(response.body);
    console.log(response.films.length);
  }
});
