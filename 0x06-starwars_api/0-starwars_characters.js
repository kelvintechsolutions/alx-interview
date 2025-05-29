const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode}`);
    return;
  }

  try {
    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;
    const characterNames = [];
    
    let index = 0;
    const fetchNextCharacter = () => {
      if (index >= characterUrls.length) {
        characterNames.forEach(name => console.log(name));
        return;
      }
      
      request(characterUrls[index], (err, res, charBody) => {
        if (err) {
          console.error('Error:', err);
          return;
        }
        
        if (res.statusCode !== 200) {
          console.error(`Error: Received status code ${res.statusCode} for ${characterUrls[index]}`);
          return;
        }
        
        try {
          const characterData = JSON.parse(charBody);
          characterNames.push(characterData.name);
          index++;
          fetchNextCharacter();
        } catch (parseError) {
          console.error('Error parsing character data:', parseError);
        }
      });
    };
    
    fetchNextCharacter();
  } catch (parseError) {
    console.error('Error parsing film data:', parseError);
  }
});
