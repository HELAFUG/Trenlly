// src/components/Home.js
import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";

const Home = () => {
  const { logout } = useContext(AuthContext);

  // Example of using the token: make an authenticated request
  // For demo, just show logged in page

  return (
    <div>
      <h2>Welcome to Home</h2>
      <p>You are logged in. Token is being used for authenticated requests.</p>
      <button onClick={logout}>Logout</button>
    </div>
  );
};

export default Home;
