import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const AdminDashboard = () => {
  const [stats, setStats] = useState({
    totalStaff: 0,
    onDuty: 0,
    absent: 0,
    pendingRequests: 0,
  });

  useEffect(() => {
    // Fetch admin stats from API
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch('/api/staff/', {
        headers: { 'Authorization': `Bearer ${token}` },
      });
      if (response.ok) {
        const staff = await response.json();
        setStats(prev => ({ ...prev, totalStaff: staff.length }));
      }
    } catch (error) {
      console.error('Error fetching stats:', error);
    }
  };

  return (
    <div>
      <h2>Admin Dashboard</h2>
      <div className="row">
        <div className="col-md-3">
          <div className="card text-white bg-primary mb-3">
            <div className="card-body">
              <h5 className="card-title">Total Staff</h5>
              <p className="card-text">{stats.totalStaff}</p>
            </div>
          </div>
        </div>
        <div className="col-md-3">
          <div className="card text-white bg-success mb-3">
            <div className="card-body">
              <h5 className="card-title">On Duty</h5>
              <p className="card-text">{stats.onDuty}</p>
            </div>
          </div>
        </div>
        <div className="col-md-3">
          <div className="card text-white bg-warning mb-3">
            <div className="card-body">
              <h5 className="card-title">Absent</h5>
              <p className="card-text">{stats.absent}</p>
            </div>
          </div>
        </div>
        <div className="col-md-3">
          <div className="card text-white bg-info mb-3">
            <div className="card-body">
              <h5 className="card-title">Pending Requests</h5>
              <p className="card-text">{stats.pendingRequests}</p>
            </div>
          </div>
        </div>
      </div>
      <div className="mt-4">
        <h4>Quick Actions</h4>
        <div className="btn-group" role="group">
          <button className="btn btn-primary">Manage Staff</button>
          <button className="btn btn-secondary">Create Roster</button>
          <button className="btn btn-success">View Reports</button>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
