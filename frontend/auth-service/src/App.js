import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Home from "./pages/Home";
import { useAuth } from "./context/AuthContext";
import { GlobalStyle } from "./styles/GlobalStyle";

function App() {
  const { token } = useAuth();

  return (
    <>
      <GlobalStyle />
      <Router>
        <Routes>
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/" element={token ? <Home /> : <Login />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
