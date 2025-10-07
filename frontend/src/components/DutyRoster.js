import React, { useEffect, useState } from 'react';

const DutyRoster = () => {
  const [roster, setRoster] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/rosters/')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch roster data');
        }
        return response.json();
      })
      .then((data) => {
        setRoster(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading duty roster...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h2>Duty Roster</h2>
      <table border="1" cellPadding="5" cellSpacing="0">
        <thead>
          <tr>
            <th>Unit</th>
            <th>Consultant</th>
            <th>Phone</th>
            <th>Shift</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {roster.map((entry) => (
            <tr key={entry.id}>
              <td>{entry.shift.department.name}</td>
              <td>{entry.staff.user.first_name} {entry.staff.user.last_name}</td>
              <td>{entry.staff.phone}</td>
              <td>{entry.shift.name} ({entry.shift.shift_type})</td>
              <td>{entry.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DutyRoster;
