import { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post('http://127.0.0.1:5000/ask', { question: query });
      setResponse(res.data.answer);
    } catch (error) {
      console.error("Error:", error);
      setResponse("Something went wrong. Please try again.");
    }
  };

  return (
    <div className="container mt-5">
      <h1>Personalized Career & Skills Advisor</h1>
      <form onSubmit={handleSubmit}>
        <input
          className="form-control"
          placeholder="Enter your career question..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button className="btn btn-primary mt-3" type="submit">Get Advice</button>
      </form>
      {response && (
        <div className="alert alert-success mt-4">
          <strong>Advisor:</strong> {response}
        </div>
      )}
    </div>
  );
}
