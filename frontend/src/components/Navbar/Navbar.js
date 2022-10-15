import React from 'react';
import './Navbar.css';

const Navbar = () => {
  return (
    <div className="Navbar">
      <div className="Navbar-Img">
        <img src="https://www.adaptivewfs.com/wp-content/uploads/2020/07/logo-placeholder-image.png" alt="logo" width="75"/>
      </div>
      <div className="Navbar-Links">
        <button className="Navbar-Link">My Profile</button>
        <button className="Navbar-Link">Colleges</button>
        <button className="Navbar-Link">Essays</button>
      </div>
    </div>
  )
}

export default Navbar;