import React from 'react';
import './AppProgress.css';

const AppProgress = (props) => {
  return (
    <div className="AppProcess">
      <div className="AppProcess-Header">
        <h2>Harvard University</h2>
        <button className="AppProcess-Button">Complete/Edit Application</button>
      </div>
      <p>Deadline: January 1, 2023</p>
      <progress className="AppProgress-Bar"value="32" max="100"></progress>
    </div>
  )
}

export default AppProgress;