import React, { useEffect, useState } from 'react';
import { NavLink } from 'react-router-dom';

export default function Navbar() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (token) {
      setIsLoggedIn(true);
    } else {
      setIsLoggedIn(false);
    }
  }, []);

  return (
    <>
      <nav
        className="navbar navbar-expand-lg navbar-light"
        style={{
          backgroundColor: '#6B46C1',
          padding: '1rem 1rem',
        }}
      >
        <div className="container-fluid">
          <NavLink className="navbar-brand" to="product/" style={{ color: 'white' }}>ADD PRODUCTS</NavLink>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <NavLink className="nav-link active" aria-current="page" to="/" style={{ color: 'white' }}>Home</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/show" style={{ color: 'white' }}>SHOW PRODUCTS</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="#" style={{ color: 'white' }}>Pricing</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link disabled" to="#" tabIndex="-1" aria-disabled="true" style={{ color: 'white' }}>Disabled</NavLink>
              </li>
            </ul>
            <ul className="navbar-nav ms-auto">
              {isLoggedIn ? (
                <li className="nav-item">
                  <NavLink className="nav-link" to="/logout" style={{ color: 'white' }}>Logout</NavLink>
                </li>
              ) : (
                <>
                  <li className="nav-item">
                    <NavLink className="nav-link" to="/login" style={{ color: 'white' }}>Login</NavLink>
                  </li>
                  <li className="nav-item">
                    <NavLink className="nav-link" to="/signup" style={{ color: 'white' }}>Signup</NavLink>
                  </li>
                </>
              )}
            </ul>
          </div>
        </div>
      </nav>

      {/* Footer */}
      <footer
        className="footer mt-auto"
        style={{
          backgroundColor: '#6B46C1',
          padding: '1rem 1rem',
          textAlign: 'center',
          color: 'white',
          position: 'fixed',
          width: '100%',
          bottom: 0,
        }}
      >
        <div className="container">
          <span>© Develop BY Rohit B</span>
        </div>
      </footer>
    </>
  );
}
