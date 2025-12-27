import { useState, useContext } from "react";
import { useNavigate, Link } from "react-router-dom";
import AuthContext from "../context/AuthContext";

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const { register } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    const success = await register(email, password);
    if (success) {
      navigate("/login");
    } else {
      setError("Registration failed. Try again.");
    }
  };

  // ... same logic

  return (
    <div className="min-h-screen flex items-center justify-center relative overflow-hidden bg-gradient-to-br from-purple-700 via-pink-600 to-indigo-700">
      <div className="floating-orb from-purple-500 to-indigo-600 w-96 h-96 -top-32 -left-32" />
      <div className="floating-orb from-pink-500 to-purple-600 w-80 h-80 bottom-0 right-0" />
      <div className="floating-orb from-indigo-500 to-pink-600 w-96 h-96 top-1/3 right-1/4" />

      <div className="glass-card p-12 w-full max-w-md relative z-10">
        <h2 className="text-4xl font-bold text-center text-white mb-10 drop-shadow-lg">
          Create Account
        </h2>

        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Same input-field and btn-primary classes as Login */}
          <div>
            <label className="block text-white/90 font-medium mb-2">
              Email
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="input-field"
              placeholder="you@example.com"
              required
            />
          </div>
          <div>
            <label className="block text-white/90 font-medium mb-2">
              Password
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="input-field"
              placeholder="Choose strong password"
              required
            />
          </div>

          {error && (
            <div className="bg-red-500/20 border border-red-400/50 text-red-200 px-4 py-3 rounded-xl text-sm">
              {error}
            </div>
          )}

          <button
            type="submit"
            className="btn-primary from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700"
          >
            Create Account
          </button>
        </form>

        <p className="text-center mt-8 text-white/80">
          Already have an account?{" "}
          <Link to="/login" className="text-white font-bold hover:underline">
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
};

export default Register;
