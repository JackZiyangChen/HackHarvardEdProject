import React from 'react';
import Navbar from '../../components/Navbar/Navbar';
import AppProcess from '../../components/AppProgress/AppProgress';
import './Dashboard.css';
import apiClient from '../../service/apiClient';

const Dashboard = () => {
  // const data = {}
  // const raw = apiClient.get(`/db/get?user=${'test1'}`,'GET',{})
  // data = raw.data;
  const processes = []
  // for(let i = 0; i < data.length; i++) {
  //   const row = data[i]
  //   processes.push(<AppProcess name={row.name} admission={row.admission} deadline={row.deadline} value={row.value} todos={row.todos} progresses={row.progresses} completes={row.completes} />)
  // }
    

  return (
    <div className="Home">
      <Navbar />
      <div className="Home-Content">
        <h1>Welcome Back, John!</h1>
        <img src="./hero.jpg" alt="college" className="hero"/>
        <hr/>
        <h2>Your Application Progress</h2>
        <div className="progress">
          {processes}
          <AppProcess name="Harvard University" deadline="January 1, 2023" value="90"/>
          <AppProcess name="Stanford University" deadline="January 15, 2023" value="70"/>
          <AppProcess name="Massachusetts Institute of Technology" deadline="January 15, 2023" value="50"/>
          <AppProcess name="University of California, Los Angeles" deadline="November 1, 2021" value="50"/>
        </div>
      </div>
    </div>
  )
}

export default Dashboard;