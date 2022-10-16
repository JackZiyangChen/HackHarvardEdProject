import React from 'react';
import { useNavigate } from 'react-router-dom';
import './AppProgress.css';

const AppProgress = (props) => {
  const navigate = useNavigate()
  return (
    <div className="AppProcess">
      <div className="AppProcess-Header">
        <h2>{props.name}</h2>
        <button className="AppProcess-Button" onClick={() => navigate("/manage")}>Complete/Edit Application</button>
      </div>
      <p>Deadline: {props.deadline}</p>
      <progress className="AppProgress-Bar" value={props.value} max="100"></progress>
    </div>
  )
}

export default AppProgress;