import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <React.Fragment>
      <h1>Home</h1>
      <Link to="/login">Go to login</Link>
    </React.Fragment>
  );
};

export default Home;
