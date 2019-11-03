import React, { Component } from "react";
import { Link } from "react-router-dom";

class NavBar extends Component {
  state = {
    navLinks: [
      { label: "Home", path: "/home" },
      { label: "My Notebook", path: "/mynotebook" }
    ]
  };

  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <Link className="navbar-brand" to="/" style={{ fontWeight: "bold" }}>
          webnotebook
        </Link>

        {/* Collapse button to show up when screen width is small enough */}
        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarText"
          aria-controls="navbarText"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse main-navbar" id="navbarText">
          <ul className="navbar-nav mr-auto">
            {this.state.navLinks.map(navLink => (
              <li
                key={navLink.label}
                className="nav-item active"
                style={navLink.style}
              >
                <Link className="nav-link" to={navLink.path}>
                  {navLink.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </nav>
    );
  }
}

export default NavBar;
