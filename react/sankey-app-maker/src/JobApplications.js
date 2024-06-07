import React, { useState } from 'react';

const JobApplications = () => {
    const [applications, setApplications] = useState([]);
    const [loading, setLoading] = useState(false);

    const fetchApplications = async () => {
        setLoading(true);
        try {
            console.log('idiot!!!')
            const response = await fetch('http://localhost:8000/list-applications/');
            const data = await response.json();
            console.log('Fetched data:', data); 
            setApplications(data);
        } catch (error) {
            console.error('cannot fetch applications:', error);
        }
        setLoading(false);
    };

    return (
        <div>
            <button onClick={fetchApplications} disabled={loading}>
                {loading ? 'Loading...' : 'Fetch Applications'}
            </button>
            <ul>
                {applications.map((app, index) => (
                    <li key={index}>{app}</li>
                ))}
            </ul>
        </div>
    );
};

export default JobApplications;