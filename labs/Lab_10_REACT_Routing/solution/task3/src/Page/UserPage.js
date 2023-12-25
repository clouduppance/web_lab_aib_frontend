// UserPage.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function UserPage() {
  const { id } = useParams();
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`https://rickandmortyapi.com/api/character/${id}`);
        if (!response.ok) {
          throw new Error('Error: ');
        }
        const data = await response.json();
        setUserData(data);
      } catch (error) {
        console.error('Error: ', error);
      }
    };

    fetchData();
  }, [id]);

  return (
    <div>
      <h2>User Page</h2>
      {userData ? (
        <div>
          <p>Name: {userData.name}</p>
          <p>Status: {userData.status}</p>
          <p>Species: {userData.species}</p>
          <p>Gender: {userData.gender}</p>
          <p>Origin: {userData.origin.name}</p>
          <img src={userData.image} alt={`${userData.name} avatar`} />
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default UserPage;
