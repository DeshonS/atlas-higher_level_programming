#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const wedgeId = '18';
request.get(apiUrl, (error, response, body) => {
if (error) {
  console.log(error)
}
  try {
    const films = JSON.parse(body).results;
    const wedgeMovies = films.filter(film =>
      film.characters.some(characterUrl => characterUrl.includes(`/people/${wedgeId}/`))
    );
    console.log(wedgeMovies.length);
  } catch (parseError) {
    console.log(parseError);
  }
});
