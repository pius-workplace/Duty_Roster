import React, { useState, useEffect } from 'react';
import AppPages from './AppPages';
import Login from './Login';

function App() {
  const [token, setToken] = useState(localStorage.getItem('token'));

  const handleLogin = (newToken) => {
    setToken(newToken);
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    setToken(null);
  };

  useEffect(() => {
    // Optionally, verify token validity here
  }, [token]);

  if (!token) {
    return <Login onLogin={handleLogin} />;
  }

  return <AppPages onLogout={handleLogout} />;
}

export default App;
