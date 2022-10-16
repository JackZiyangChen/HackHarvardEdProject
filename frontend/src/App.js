import { Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard/Dashboard';
import Login from './pages/Login/Login';
import Portal from './pages/Portal/Portal';
import './App.css';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" exact element={<Login />} />
        <Route path="/dashboard" element={<Dashboard/>} />
        <Route path="/portal" element={<Portal />} />
      </Routes>
    </div>
  );
}

export default App;
