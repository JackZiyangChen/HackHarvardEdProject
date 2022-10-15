import React from 'react';
import Navbar from '../../components/Navbar/Navbar';
import AppProcess from '../../components/AppProgress/AppProgress';
import './Home.css';

const Home = () => {
  return (
    <div className="Home">
      <Navbar />
      <div className="Home-Content">
        <h1>Welcome Back, John!</h1>
        <img src="./hero.jpg" alt="college" className="hero"/>
        <hr/>
        <h2>Your Application Progress</h2>
        <div className="progress">
          <AppProcess />
          <AppProcess />
          <AppProcess />
          <AppProcess />
          <AppProcess />
        </div>
      </div>
    </div>
  )
}

export default Home;