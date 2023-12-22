import React from 'react';
import { useParams } from 'react-router-dom';

function UserPage() {
  const { id } = useParams();

  const userInfo = {
    id,
    name: `User ${id}`,
  };

  return (
    <div>
      <h2>User Page</h2>
      <p>Name: {userInfo.name}</p>
    </div>
  );
}

export default UserPage;
