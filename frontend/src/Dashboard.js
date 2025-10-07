import React, { useState, useEffect } from 'react';
import AdminDashboard from './AdminDashboard';
import StaffDashboard from './StaffDashboard';

const Dashboard = () => {
  const [userRole, setUserRole] = useState('');

  useEffect(() => {
    fetchUserRole();
  }, []);

  const fetchUserRole = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch('/api/user-info/', {
        headers: { 'Authorization': `Bearer ${token}` },
      });
      if (response.ok) {
        const data = await response.json();
        setUserRole(data.role);
      }
    } catch (error) {
      console.error('Error fetching user role:', error);
    }
  };

  if (userRole === 'Admin' || userRole === 'Manager' || userRole === 'Administrator') {
    return <AdminDashboard />;
  } else {
    return <StaffDashboard />;
  }
};

export default Dashboard;
