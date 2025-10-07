import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Dashboard from './Dashboard';
import DutyRoster from './components/DutyRoster';

const AppPages = ({ onLogout }) => {
  return (
    <Router>
      <div>
        <nav className="navbar navbar-expand navbar-light bg-light">
          <a className="navbar-brand" href="/">Hospital Duty Roster</a>
          <div className="navbar-nav ms-auto">
            <button className="btn btn-outline-danger" onClick={onLogout}>Logout</button>
          </div>
        </nav>
        <div className="container mt-4">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/roster" element={<DutyRoster />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default AppPages;
