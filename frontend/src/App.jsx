import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/jobs/")
      .then(res => setJobs(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Available Jobs</h1>
      {jobs.map(job => (
        <div key={job.id} style={{ marginBottom: "1rem" }}>
          <h2>{job.title}</h2>
          <p>{job.company}</p>
          <p>{job.description}</p>
          <a href={job.url} target="_blank" rel="noopener noreferrer">Apply Here</a>
        </div>
      ))}
    </div>
  );
}

export default App;
