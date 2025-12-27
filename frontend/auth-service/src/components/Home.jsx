import { useContext } from "react";
import AuthContext from "../context/AuthContext";

const Home = () => {
  const { logout } = useContext(AuthContext);

  return (
    <div className="min-h-screen flex items-center justify-center relative overflow-hidden bg-gradient-to-br from-emerald-500 via-teal-600 to-cyan-700">
      <div className="floating-orb from-emerald-400 to-cyan-400 w-96 h-96 -top-48 left-1/4" />
      <div className="floating-orb from-teal-400 to-emerald-500 w-80 h-80 bottom-20 right-1/3" />

      <div className="glass-card p-20 max-w-2xl w-full text-center relative z-10">
        <div className="mb-12">
          <div className="w-40 h-40 bg-gradient-to-br from-emerald-500 to-cyan-500 rounded-full mx-auto flex items-center justify-center text-white text-8xl font-bold shadow-2xl animate-bounce">
            ✓
          </div>
        </div>

        <h1 className="text-6xl font-bold text-white mb-8 drop-shadow-2xl">
          Success! You're In!
        </h1>

        <p className="text-2xl text-white/90 mb-16">
          Enjoy the premium modern experience.
        </p>

        <button
          onClick={logout}
          className="bg-white/20 backdrop-blur-lg text-white font-bold py-5 px-12 rounded-2xl border border-white/30 hover:bg-white/30 transition-all transform hover:scale-110 shadow-xl"
        >
          Logout
        </button>
      </div>
    </div>
  );
};

export default Home;
