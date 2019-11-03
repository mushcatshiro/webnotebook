import React from "react";
import { Route, Switch } from "react-router-dom";
import Home from "./components/home";
import LoginPage from "./components/loginPage";
import NavBar from "./components/navBar";
import TestApi from "./components/testApi";
import "./myStyles.css";

function App() {
  return (
    <div>
      <NavBar />
      <div className="container">
        <Switch>
          <Route path="/testapi" component={TestApi} />
          <Route path="/login">
            <LoginPage />
          </Route>
          <Route exact path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </div>
  );
}

export default App;
