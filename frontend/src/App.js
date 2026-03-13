import React, { useState } from "react";
import axios from "axios";

function App() {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!image) {
      alert("Please select an image first!");
      return;
    }

    const formData = new FormData();
    formData.append("image", image);

    setLoading(true);
    setResult("");

    try {
      // ✅ Replace this URL with your Railway backend URL
      const response = await axios.post(
        "https://<your-railway-backend-url>/predict",
        formData
      );

      // Response example: { disease: "Leaf Blight", confidence: 95 }
      setResult(
        `Disease: ${response.data.disease} | Confidence: ${response.data.confidence}%`
      );
    } catch (error) {
      console.error(error);
      setResult("Error connecting to backend. Try again!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>🌿 Crop Disease Detector</h1>

      <input type="file" onChange={handleImageChange} accept="image/*" />

      <br />
      <br />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Predicting..." : "Predict Disease"}
      </button>

      <h2 style={{ marginTop: "20px" }}>{result}</h2>
    </div>
  );
}

export default App;