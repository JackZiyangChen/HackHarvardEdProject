import React from 'react';
import { useNavigate } from "react-router-dom";
import './Navbar.css';

const Navbar = () => {
  const navigate = useNavigate()
  return (
    <div className="Navbar">
      <div className="Navbar-Img" onClick={() => navigate("/dashboard")}>
        <img src="./LogoLight.svg" alt="logo" height="40"/>
      </div>
      <div className="Navbar-Links">
        <button className="Navbar-Link" onClick={() => navigate("/dashboard")}>Dashboard</button>
        <button className="Navbar-Link" onClick={() => navigate("/portal")}>My Portal</button>
        <button className="Navbar-Link" onClick={() => navigate("/")}>Sign Out</button>
      </div>
    </div>
  )
}

export default Navbar;