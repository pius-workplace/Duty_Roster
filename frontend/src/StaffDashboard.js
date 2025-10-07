import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const StaffDashboard = () => {
  const [userInfo, setUserInfo] = useState({});
  const [currentShift, setCurrentShift] = useState(null);

  useEffect(() => {
    fetchUserInfo();
    fetchCurrentShift();
  }, []);

  const fetchUserInfo = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch('/api/user-info/', {
        headers: { 'Authorization': `Bearer ${token}` },
      });
      if (response.ok) {
        const data = await response.json();
        setUserInfo(data);
      }
    } catch (error) {
      console.error('Error fetching user info:', error);
    }
  };

  const fetchCurrentShift = async () => {
    // Fetch current shift logic here
    // For now, placeholder
    setCurrentShift({ shift: 'Morning', department: 'Emergency' });
  };

  const markAttendance = async (status) => {
    try {
      const token = localStorage.getItem('token');
      await fetch('/api/attendances/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ status }),
      });
      alert('Attendance marked successfully');
    } catch (error) {
      console.error('Error marking attendance:', error);
    }
  };

  return (
    <div>
      <h2>Staff Dashboard</h2>
      <div className="row">
        <div className="col-md-6">
          <div className="card mb-3">
            <div className="card-body">
              <h5 className="card-title">Welcome, {userInfo.username}</h5>
              <p className="card-text">Role: {userInfo.role}</p>
              <p className="card-text">Department: {userInfo.department}</p>
            </div>
          </div>
        </div>
        <div className="col-md-6">
          <div className="card mb-3">
            <div className="card-body">
              <h5 className="card-title">Current Shift</h5>
              {currentShift ? (
                <p className="card-text">{currentShift.shift} - {currentShift.department}</p>
              ) : (
                <p className="card-text">No current shift</p>
              )}
            </div>
          </div>
        </div>
      </div>
      <div className="mt-4">
        <h4>Attendance</h4>
        <div className="btn-group" role="group">
          <button className="btn btn-success" onClick={() => markAttendance('present')}>Check In</button>
          <button className="btn btn-warning" onClick={() => markAttendance('late')}>Late</button>
          <button className="btn btn-danger" onClick={() => markAttendance('absent')}>Absent</button>
        </div>
      </div>
      <div className="mt-4">
        <h4>Quick Actions</h4>
        <div className="btn-group" role="group">
          <button className="btn btn-primary">Request Time Off</button>
          <button className="btn btn-secondary">View Schedule</button>
          <button className="btn btn-info">Notifications</button>
        </div>
      </div>
    </div>
  );
};

export default StaffDashboard;
