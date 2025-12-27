import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";

const FormContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #ff00ff, #00ffff, #ffff00);
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
  background: rgba(255, 255, 255, 0.2);
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 0 20px rgba(255, 0, 255, 0.5);
  width: 300px;
  text-align: center;
  animation: pulse 2s infinite;
  @keyframes pulse {
    0% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.05);
    }
    100% {
      transform: scale(1);
    }
  }
`;

const Input = styled.input`
  width: 100%;
  margin: 10px 0;
  padding: 10px;
  border: 2px solid #ff00ff;
  border-radius: 10px;
  background: transparent;
  color: #fff;
  font-size: 16px;
  &::placeholder {
    color: #00ffff;
  }
  animation: borderGlow 1.5s infinite alternate;
  @keyframes borderGlow {
    from {
      border-color: #ff00ff;
    }
    to {
      border-color: #00ffff;
    }
  }
`;

const Button = styled.button`
  width: 100%;
  padding: 10px;
  background: linear-gradient(45deg, #00ff00, #ff0000);
  border: none;
  border-radius: 10px;
  color: #fff;
  font-size: 18px;
  cursor: pointer;
  margin-top: 20px;
  animation: rotateHue 3s linear infinite;
  @keyframes rotateHue {
    0% {
      filter: hue-rotate(0deg);
    }
    100% {
      filter: hue-rotate(360deg);
    }
  }
`;

const LinkText = styled.p`
  margin-top: 10px;
  color: #ffff00;
  cursor: pointer;
  text-decoration: underline;
  animation: blink 1s infinite;
  @keyframes blink {
    50% {
      opacity: 0;
    }
  }
`;

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const url = `http://localhost:8000/trenlly/auth/register?email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}&is_active=true&is_superuser=false&is_verified=false`;
      await axios.post(url, {}, { headers: { accept: "application/json" } });
      alert("Registration successful! Proceed to login.");
      navigate("/login");
    } catch (error) {
      console.error(error);
      alert("Registration failed.");
    }
  };

  return (
    <FormContainer>
      <Form onSubmit={handleSubmit}>
        <h2 style={{ color: "#ff00ff", textShadow: "0 0 10px #00ffff" }}>
          Register
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
        <Button type="submit">Register</Button>
        <LinkText onClick={() => navigate("/login")}>
          Already have an account? Login
        </LinkText>
      </Form>
    </FormContainer>
  );
};

export default Register;
