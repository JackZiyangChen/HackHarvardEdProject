import React from 'react';
import Navbar from '../../components/Navbar/Navbar';
import CollegeDetail from '../../components/CollegeDetail/CollegeDetail';
import './Colleges.css';

const Colleges = () => {
  return (
    <div className="Colleges">
      <Navbar/>
      <div className="Home-Content">
        <h1>Your Colleges</h1>
        <div className="College-List">
          <CollegeDetail/>
          <CollegeDetail/>
          <CollegeDetail/>
          <CollegeDetail/>
        </div>
      </div>
    </div>
  )
}

export default Colleges;