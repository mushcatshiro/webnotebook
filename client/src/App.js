import React from "react";
import { Route, Switch } from "react-router-dom";
import Home from "./components/home";
import LoginPage from "./components/loginPage";
import NavBar from "./components/navBar";
import "./myStyles.css";

function App() {
  return (
    <div>
      <NavBar />
      <Switch>
        <div className="container">
          <Route path="/login">
            <LoginPage />
          </Route>
          <Route exact path="/">
            <Home />
          </Route>
        </div>
      </Switch>
    </div>
  );
}

export default App;
