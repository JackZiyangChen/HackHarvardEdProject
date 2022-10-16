import React, { useState } from 'react';
import Navbar from '../../components/Navbar/Navbar';
import CollegeDetail from '../../components/CollegeDetail/CollegeDetail';
import SearchResult from '../../components/SearchResult/SearchResult';
import './Portal.css';

const Portal = () => {
  const [searchTerm, setSearchTerm] = useState('')
  const handleChange = (e) => {
    let lowerCase = e.target.value.toLowerCase();
    console.log(searchTerm)
    setSearchTerm(lowerCase);
  }
  return (
    <div className="Colleges">
      <Navbar/>
      <div className="Home-Content">
        <h1>Your Portal</h1>
        <br/>
        <h3>Add College</h3>
        <input type="text" name="name" onChange={handleChange} className="Login-Input"/>
        <SearchResult input={searchTerm} />
        <div className="College-List">
          <CollegeDetail name="Harvard University" admission="Regular Decision" deadline="January 1, 2023" value="90" todos={['Supplement Essay #1', 'Main Essay']} progresses={['Recommendation Letter #1', 'Recommendation Letter #2']} completes={['Transcript']}/>
          <CollegeDetail name="Stanford University" admission="Regular Decision" deadline="January 15, 2023" value="70" todos={['Main Essay']} progresses={['Recommendation Letter #1', 'Recommendation Letter #2']} completes={['Transcript', 'Supplement Essay #1']}/>
          <CollegeDetail name="Massachusetts Institute of Technology" admission="Regular Decision" deadline="January 15, 2023" value="50" todos={['Supplement Essay 1', 'Main Essay']} progresses={['Recommendation Letter #1', 'Recommendation Letter #2']} completes={['Transcript']}/>
          <CollegeDetail name="University of California, Los Angeles" admission="Early Decision" deadline="November 1, 2021" value="50" todos={['Supplement Essay 1', 'Main Essay']} progresses={['Recommendation Letter #1', 'Recommendation Letter #2', 'Transcript']} completes={[]}/>
        </div>
      </div>
    </div>
  )
}

export default Portal;