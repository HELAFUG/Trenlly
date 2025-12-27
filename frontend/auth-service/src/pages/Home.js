import React from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";

const Container = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: radial-gradient(circle, #ffff00, #ff00ff, #00ffff);
  animation: radialPulse 4s infinite;
  @keyframes radialPulse {
    0% {
      background-size: 100% 100%;
    }
    50% {
      background-size: 150% 150%;
    }
    100% {
      background-size: 100% 100%;
    }
  }
`;

const Title = styled.h1`
  color: #ff0000;
  text-shadow: 0 0 15px #00ff00;
  animation: glitch 1s infinite;
  @keyframes glitch {
    0% {
      transform: translate(0);
    }
    20% {
      transform: translate(-5px, 5px);
    }
    40% {
      transform: translate(-5px, -5px);
    }
    60% {
      transform: translate(5px, 5px);
    }
    80% {
      transform: translate(5px, -5px);
    }
    100% {
      transform: translate(0);
    }
  }
`;

const TokenDisplay = styled.p`
  color: #00ffff;
  font-size: 18px;
  margin: 20px 0;
  padding: 10px 20px;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 10px;
  max-width: 80%;
  word-break: break-all;
  animation: fadeIn 2s ease-in;
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
`;

const LogoutButton = styled.button`
  padding: 10px 20px;
  background: linear-gradient(90deg, #ff0000, #0000ff);
  border: none;
  border-radius: 15px;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
  animation: shake 0.5s infinite;
  @keyframes shake {
    0% {
      transform: translate(1px, 1px) rotate(0deg);
    }
    10% {
      transform: translate(-1px, -2px) rotate(-1deg);
    }
    20% {
      transform: translate(-3px, 0px) rotate(1deg);
    }
    30% {
      transform: translate(3px, 2px) rotate(0deg);
    }
    40% {
      transform: translate(1px, -1px) rotate(1deg);
    }
    50% {
      transform: translate(-1px, 2px) rotate(-1deg);
    }
    60% {
      transform: translate(-3px, 1px) rotate(0deg);
    }
    70% {
      transform: translate(3px, 1px) rotate(-1deg);
    }
    80% {
      transform: translate(-1px, -1px) rotate(1deg);
    }
    90% {
      transform: translate(1px, 2px) rotate(0deg);
    }
    100% {
      transform: translate(1px, -2px) rotate(-1deg);
    }
  }
`;

const Home = () => {
  const { token, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <Container>
      <Title>Welcome to the Crazy Zone!</Title>
      <TokenDisplay>Your Bearer Token: {token}</TokenDisplay>
      <LogoutButton onClick={handleLogout}>Logout</LogoutButton>
    </Container>
  );
};

export default Home;
