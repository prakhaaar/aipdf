import { Link } from "react-router-dom";
import aiLogo from "../assets/ai.svg";
import { Plus } from "lucide-react";

export default function Navbar() {
  return (
    <nav
      className="shadow px-6 py-3 flex items-center justify-between"
      style={{ backgroundColor: "#003145" }}
    >
      {/* Logo + Tagline */}
      <div className="flex items-center space-x-2">
        <img
          src={aiLogo}
          alt="AI Planet Logo"
          className="h-auto max-h-10 w-auto object-contain"
        />
        <div className="flex flex-col leading-tight text-white"></div>
      </div>

      {/* Upload Button */}
      <Link
        to="/upload"
        className="border border-white hover:border-green-400 text-white px-4 py-2 rounded flex items-center gap-2 transition"
      >
        <Plus size={16} />
        Upload PDF
      </Link>
    </nav>
  );
}
