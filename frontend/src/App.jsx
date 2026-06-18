import "./App.css";
import { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";

function App() {
  const [file, setFile] = useState(null);
  const [analysis, setAnalysis] = useState("");
  const [ats, setAts] = useState("");
  const [match, setMatch] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeResume = async () => {
    if (!file) {
      alert("Please upload a resume");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      // Reset state values before running a fresh analysis
      setAnalysis("");
      setAts("");
      setMatch(null);

      // Execute all 3 API calls concurrently over the network
      const [analysisRes, atsRes, matchRes] = await Promise.all([
        axios.post("http://127.0.0.1:8000/analyze-resume", formData),
        axios.post("http://127.0.0.1:8000/ats-score", formData),
        axios.post("http://127.0.0.1:8000/resume-match", formData)
      ]);

      setAnalysis(analysisRes.data.analysis);
      setAts(atsRes.data.ats);
      setMatch(matchRes.data);
      console.log(matchRes.data);
       // Stores your backend's match payload

    } catch (error) {
      console.error("Analysis failed:", error);
      alert("Error analyzing resume. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="hero">
        <h1 className="title">🚀 AI Career Copilot</h1>

        <div className="upload-box">
          <input
            type="file"
            accept=".pdf"
            onChange={(e) => setFile(e.target.files[0])}
          />

          <button
            onClick={analyzeResume}
            disabled={loading}
            className="submit-btn"
          >
            {loading ? "Analyzing..." : "Analyze Resume"}
          </button>

          {loading && (
            <p className="loading-text">
              Processing your resume through AI agents...
            </p>
          )}
        </div>

        {/* --- Resume Analysis Render Card --- */}
        {analysis && (
          <div className="card">
            <h2>Resume Analysis</h2>
            <div className="analysis-content">
              <ReactMarkdown>{analysis}</ReactMarkdown>
            </div>
          </div>
        )}

        {/* --- ATS Score Scoreboard & Evaluation --- */}
        {ats && (
          <>
            <div className="ats-score-card">
              <h3>ATS SCORE</h3>
              <div className="score-number">
                {ats.match(/\d+/)?.[0] || "85"}/100
              </div>
            </div>

            <div className="card">
              <h2>ATS Analysis</h2>
              <div className="analysis-content">
                <ReactMarkdown>{ats}</ReactMarkdown>
              </div>
            </div>
          </>
        )}

        {/* --- Resume Match Score and Skill Lists --- */}
        {match && (
          <div className="card">
            <h2>Resume Match</h2>

            <div className="match-score">
              {match.score}%
            </div>

            {/* Added match-grid to split lists side-by-side */}
            <div className="match-grid">
              <div className="match-section">
                <h3>Matched Skills</h3>
                <ul>
                  {match.matched?.map((skill, index) => (
                    <li key={index}>✅ {skill}</li>
                  ))}
                </ul>
              </div>

              <div className="match-section">
                <h3>Missing Skills</h3>
                <ul>
                  {match.missing?.map((skill, index) => (
                    <li key={index}>❌ {skill}</li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        )}

      </div>
    </div>
  );
}

export default App;