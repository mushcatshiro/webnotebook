import React, { Component } from "react";
import axios from "axios";

class TestApi extends Component {
  state = {};
  async componentDidMount() {
    const data = await axios.get("http://localhost:5000/api/post/1");
    console.log("data", data);
  }
  render() {
    return <h1>Test API</h1>;
  }
}

export default TestApi;
