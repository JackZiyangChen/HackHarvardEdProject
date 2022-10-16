import React, { useState } from 'react';
import './CollegeDetail.css'

const CollegeDetail = (props) => {
  const [isExpanded, setIsExpanded] = useState(false);
  return (
    <div className="CollegeDetail">
      <h2>{props.name}</h2>
      <div className="CollegeDetail-Spacing">
        <p>Admission: {props.admission}</p>
        <p>Deadline: {props.deadline}</p>
      </div>
      <div className="CollegeDetail-Spacing gap">
        <p>Progression: </p>
        <progress className="AppProgress-Bar"value={props.value} max="100"></progress>
      </div>
      {isExpanded ?
        <>
          <div className="CollegeDetail-Spacing">
            <div className="CollegeDetail-Wrapper">
              <h3>Must be Completed</h3>
              <ul>
                {props.todos ? props.todos.map((todo) => (
                  <li>{todo}</li>
                )) : null}
              </ul>
            </div>
            <div className="CollegeDetail-Wrapper">
              <h3>In Progress</h3>
              <ul>
                {props.progresses ? props.progresses.map((progress) => (
                  <li>{progress}</li>
                )) : null}
              </ul>
            </div>
            <div className="CollegeDetail-Wrapper">
              <h3>Completed</h3>
              <ul>
                {props.completes ? props.completes.map((complete) => (
                  <li>{complete}</li>
                )) : null}
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