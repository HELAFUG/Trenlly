import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import styled from "styled-components";

const FormContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #00ff00, #ff0000, #0000ff);
  animation: gradientShift 5s ease infinite;
  @keyframes gradientShift {
    0% {
      background-position: 0% 50%;
    }
    50% {
      background-position: 100% 50%;
    }
    100% {
      background-position: 0% 50%;
    }
  }
`;

const Form = styled.form`
  background: rgba(0, 0, 0, 0.3);
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);
  width: 300px;
  text-align: center;
  animation: spin 10s linear infinite;
  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
`;

const Input = styled.input`
  width: 100%;
  margin: 10px 0;
  padding: 10px;
  border: 2px solid #00ff00;
  border-radius: 10px;
  background: transparent;
  color: #fff;
  font-size: 16px;
  &::placeholder {
    color: #ff0000;
  }
  animation: borderGlow 1.5s infinite alternate;
  @keyframes borderGlow {
    from {
      border-color: #00ff00;
    }
    to {
      border-color: #ff0000;
    }
  }
`;

const Button = styled.button`
  width: 100%;
  padding: 10px;
  background: linear-gradient(45deg, #ff00ff, #00ffff);
  border: none;
  border-radius: 10px;
  color: #000;
  font-size: 18px;
  cursor: pointer;
  margin-top: 20px;
  animation: bounce 1s infinite;
  @keyframes bounce {
    0%,
    100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-10px);
    }
  }
`;

const LinkText = styled.p`
  margin-top: 10px;
  color: #00ffff;
  cursor: pointer;
  text-decoration: underline;
  animation: wave 2s infinite;
  @keyframes wave {
    0% {
      transform: skew(0deg);
    }
    50% {
      transform: skew(10deg);
    }
    100% {
      transform: skew(0deg);
    }
  }
`;

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const url = `http://localhost:8000/trenlly/auth/login?email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}&is_active=true&is_superuser=false&is_verified=false`;
      const response = await axios.post(
        url,
        {},
        { headers: { accept: "application/json" } },
      );
      const token = response.data.access_token; // Assuming the token is in { access_token: '...' }
      login(token);
      navigate("/");
    } catch (error) {
      console.error(error);
      alert("Login failed.");
    }
  };

  return (
    <FormContainer>
      <Form onSubmit={handleSubmit}>
        <h2 style={{ color: "#00ff00", textShadow: "0 0 10px #ff0000" }}>
          Login
        </h2>
        <Input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <Input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <Button type="submit">Login</Button>
        <LinkText onClick={() => navigate("/register")}>
          No account? Register
        </LinkText>
      </Form>
    </FormContainer>
  );
};

export default Login;
