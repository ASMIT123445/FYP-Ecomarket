// src/components/TestBackend.jsx
// import React, { useEffect, useState } from "react";
// import axios from "axios";

// function TestBackend() {
//   const [response, setResponse] = useState("");

//   useEffect(() => {
//     axios.get("http://127.0.0.1:8000/api/test/")
//       .then(res => {
//         setResponse(res.data.message); // show the message from Django
//       })
//       .catch(err => {
//         console.error("Error connecting to backend:", err);
//         setResponse("Error connecting to backend");
//       });
//   }, []);

//   return (
//     <div>
//       <h2>Backend Test:</h2>
//       <p>{response}</p>
//     </div>
//   );
// }

// export default TestBackend;
