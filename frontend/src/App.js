import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    customerName: "",
    phone: "",
    courseName: "",
    language: ""
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://localhost:8000/submit", formData);
      alert("Form Submitted Successfully!");

      setFormData({
      customerName: "",
      phone: "",
      courseName: "",
      language: ""
    });

    } catch (error) {
      alert("Error submitting form");
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h2 className="title">Course Registration</h2>

        <form onSubmit={handleSubmit}>
          
          <div className="input-group">
            <input
              type="text"
              name="customerName"
              placeholder="Customer Name"
              value={formData.customerName}
              onChange={handleChange}
              required
            />
          </div>

          <div className="input-group">
            <input
              type="text"
              name="phone"
              placeholder="Phone Number"
              value={formData.phone}
              onChange={handleChange}
              required
            />
          </div>

          <div className="input-group">
            <select
              name="courseName"
              value={formData.courseName}
              onChange={handleChange}
              required
            >
              <option value="">Select Course</option>
              <option value="AI Automation Course">AI Automation Course</option>
              <option value="Full Stack Development">Full Stack Development</option>
              <option value="Python Mastery">Python Mastery</option>
            </select>
          </div>

          <div className="input-group">
            <select
              name="language"
              value={formData.language}
              onChange={handleChange}
              required
            >
              <option value="">Select Language</option>
              <option value="english">English</option>
              <option value="telugu">Telugu</option>
              <option value="tamil">Tamil</option>
            </select>
          </div>

          <button type="submit" className="submit-btn">
            Submit
          </button>

        </form>
      </div>
    </div>
  );
}

export default App;


