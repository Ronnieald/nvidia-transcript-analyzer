import React, { useEffect, useState } from 'react';

const App = () => {
  const [chunks, setChunks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/chunks')
      .then(res => res.json())
      .then(data => {
        setChunks(data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error:', err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="container">
      <h1>NVIDIA Q1 2025 Earnings Call Analysis</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        chunks.map((chunk, idx) => (
          <div key={idx} className="chunk-card">
            <h2>{chunk.file}</h2>
            <h3>Tone</h3>
            <p>{chunk.tone}</p>
            <h3>Strategic Insights</h3>
            <ul>
              {chunk.insights.map((insight, i) => (
                <li key={i}>{insight}</li>
              ))}
            </ul>
            <hr />
          </div>
        ))
      )}
    </div>
  );
};

export default App;
