import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import './Login.css';
import apiClient from '../../service/apiClient';


const authentification = (user, password) => {
  const raw = apiClient.request(`/db/get?user=${user}`, 'GET', {})
  if (raw.status === 200 && raw.data.password === password) {
    return true;
  }else{
    alert("Wrong username or password")
    return false;
  } 
}

const Login = () => {
  const navigate = useNavigate();
  const [loginForm, setLoginForm] = useState({ email: '', password: '' });
  const handleChange = (e) => {
    let name = e.target.name;
    let value = e.target.value;
    setLoginForm({ ...loginForm, [name]: value });
  };
  return (
    <div className="Login">
      <div className="Login-Wrapper">
        <img src="./LogoDark.svg" height="40" alt="logo"/>
        <h1>Login</h1>
        <div className="Login-Spacing">
          <p>Email:</p>
          <input type="email" name="email" onChange={handleChange} value={loginForm.email} className="Login-Input" />
        </div>
        <div className="Login-Spacing">
          <p>Password:</p>
          <input type="password" name="password" onChange={handleChange} value={loginForm.password} className="Login-Input" />
        </div>
        <button id="login" className="Login-Button" onClick={() => {
          const user = loginForm.email;
          const password = loginForm.password;
          if (authentification(user, password)) {
            navigate('/dashboard');
          }
        }}>Login</button>
      </div>
    </div>
  )
}

export default Login;