import { useContext } from "react";
import AuthContext from "../context/AuthContext";

const Home = () => {
  const { logout } = useContext(AuthContext);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50">
      <div className="bg-white rounded-3xl shadow-2xl p-16 max-w-2xl w-full text-center">
        <div className="mb-10">
          <div className="w-32 h-32 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-full mx-auto flex items-center justify-center text-white text-6xl font-bold shadow-2xl">
            ✓
          </div>
        </div>

        <h1 className="text-5xl font-bold text-gray-800 mb-6">
          You're Logged In!
        </h1>

        <p className="text-xl text-gray-600 mb-12">
          Welcome to your beautiful modern dashboard. Enjoy the smooth
          experience.
        </p>

        <button
          onClick={logout}
          className="bg-gray-800 hover:bg-gray-900 text-white font-semibold py-4 px-10 rounded-xl transition-all transform hover:scale-105 shadow-xl"
        >
          Logout
        </button>
      </div>
    </div>
  );
};

export default Home;
