import { useState, useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import AuthContext from "../context/AuthContext";

const Login = () => {
  // State
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  // Context & Navigation
  const { login } = useContext(AuthContext);
  const navigate = useNavigate();

  // Handlers
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    const success = await login(email, password);

    if (success) {
      navigate("/");
    } else {
      setError("Invalid credentials. Please try again.");
    }
  };

  // Render
  return (
    <div className="min-h-screen flex items-center justify-center relative overflow-hidden bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-600">
      {/* Animated Floating Orbs Background */}
      <div className="floating-orb from-indigo-400 to-blue-500 w-96 h-96 -top-48 -left-48" />
      <div className="floating-orb from-purple-400 to-pink-500 w-80 h-80 -bottom-40 -right-40" />
      <div className="floating-orb from-pink-400 to-indigo-500 w-72 h-72 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2" />

      {/* Glassmorphic Login Card */}
      <div className="glass-card p-12 w-full max-w-md relative z-10">
        <h2 className="text-4xl font-bold text-center text-white mb-10 drop-shadow-lg">
          Welcome Back
        </h2>

        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Email Field */}
          <div>
            <label
              htmlFor="email"
              className="block text-white/90 font-medium mb-2"
            >
              Email
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="input-field"
              placeholder="you@example.com"
              required
              autoComplete="email"
            />
          </div>

          {/* Password Field */}
          <div>
            <label
              htmlFor="password"
              className="block text-white/90 font-medium mb-2"
            >
              Password
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="input-field"
              placeholder="••••••••"
              required
              autoComplete="current-password"
            />
          </div>

          {/* Error Message */}
          {error && (
            <div className="bg-red-500/20 border border-red-400/50 text-red-200 px-4 py-3 rounded-xl text-sm text-center">
              {error}
            </div>
          )}

          {/* Submit Button */}
          <button type="submit" className="btn-primary">
            Sign In
          </button>
        </form>

        {/* Register Link */}
        <p className="text-center mt-8 text-white/80">
          Don't have an account?{" "}
          <Link
            to="/register"
            className="text-white font-bold hover:underline transition-underline"
          >
            Register here
          </Link>
        </p>
      </div>
    </div>
  );
};

export default Login;
