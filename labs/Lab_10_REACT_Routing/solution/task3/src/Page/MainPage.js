// MainPage.js
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function MainPage() {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    const fetchCharacters = async () => {
      try {
        let allCharacters = [];

        let response = await fetch('https://rickandmortyapi.com/api/character');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        let data = await response.json();
        allCharacters = [...allCharacters, ...data.results];

        for (let page = 2; page <= data.info.pages; page++) {
          response = await fetch(`https://rickandmortyapi.com/api/character?page=${page}`);
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          data = await response.json();
          allCharacters = [...allCharacters, ...data.results];
        }

        setCharacters(allCharacters);
      } catch (error) {
        console.error('Error: ', error);
      }
    };

    fetchCharacters();
  }, []);

  return (
    <div>
      <h2>Main Page - Users</h2>
      <ul>
        {characters.map((character) => (
          <li key={character.id}>
            <Link to={`/users/${character.id}`}>{character.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MainPage;
