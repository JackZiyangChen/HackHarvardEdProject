import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home/Home';
import Landing from './pages/Landing/Landing';
import Login from './pages/Login/Login';
import Colleges from './pages/Colleges/Colleges';
import Essay from './pages/Essay/Essay';
import './App.css';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/home" element={<Home/>} />
        <Route path="/login" element={<Login />} />
        <Route path="/colleges" element={<Colleges />} />
        <Route path="/essay" element={<Essay />} />
      </Routes>
    </div>
  );
}

export default App;
