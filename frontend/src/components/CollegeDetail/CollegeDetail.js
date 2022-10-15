import React, { useState } from 'react';
import './CollegeDetail.css'

const CollegeDetail = () => {
  const [isExpanded, setIsExpanded] = useState(false);
  return (
    <div className="CollegeDetail">
      <h2>Harvard University</h2>
      <div className="CollegeDetail-Spacing">
        <p>Admission: Regular Decision</p>
        <p>Deadline: January 1, 2023</p>
      </div>
      <div className="CollegeDetail-Spacing gap">
        <p>Progression: </p>
        <progress className="AppProgress-Bar"value="32" max="100"></progress>
      </div>
      {isExpanded ?
        <>
          <div className="CollegeDetail-Spacing">
            <div className="CollegeDetail-Wrapper">
              <h3>Must be Completed</h3>
              <ul>
                <li>Supplemental Essay</li>
                <li>Main Essay</li>
              </ul>
            </div>
            <div className="CollegeDetail-Wrapper">
              <h3>In Progress</h3>
              <ul>
                <li>Recommendation Letter 1</li>
                <li>Recommendation Letter 2</li>
              </ul>
            </div>
            <div className="CollegeDetail-Wrapper">
              <h3>Completed</h3>
              <ul>
                <li>Transcript</li>
              </ul>
            </div>
          </div>
          <button className="CollegeDetail-Extend-Button" onClick={() => setIsExpanded(isExpanded => !isExpanded)}>↑</button>
        </>:
        <button className="CollegeDetail-Extend-Button" onClick={() => setIsExpanded(isExpanded => !isExpanded)}>↓</button>
      }
      
    </div>
  )
}

export default CollegeDetail;