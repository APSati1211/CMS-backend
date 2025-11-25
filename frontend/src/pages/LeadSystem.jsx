import { motion } from "framer-motion";
import usePageContent from "../hooks/usePageContent";
import { BarChart3, Target, Zap } from "lucide-react";
import { Link } from "react-router-dom";

export default function LeadSystem() {
  const { getField, loading } = usePageContent("lead_system");

  if (loading) return <div className="h-screen flex items-center justify-center">Loading...</div>;

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="bg-gradient-to-r from-blue-700 to-blue-900 text-white py-24 text-center px-6">
        <motion.h1 initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-5xl font-bold mb-6">{getField("hero_title", "title") || "Lead Portal"}</motion.h1>
        <p className="text-xl text-blue-100 max-w-3xl mx-auto">{getField("hero_text") || "Track, Manage, and Convert leads."}</p>
      </div>

      <div className="max-w-5xl mx-auto px-6 py-20">
        <div className="grid md:grid-cols-3 gap-8 mb-16">
          {[
            { title: "Track", icon: <Target />, desc: "Real-time tracking." },
            { title: "Manage", icon: <BarChart3 />, desc: "Centralized dashboard." },
            { title: "Convert", icon: <Zap />, desc: "AI insights to close deals." }
          ].map((item, i) => (
            <motion.div key={i} whileHover={{ scale: 1.05 }} className="bg-white p-8 rounded-2xl shadow-md text-center">
              <div className="text-blue-600 mb-4 flex justify-center">{item.icon}</div>
              <h3 className="text-xl font-bold text-slate-800 mb-2">{item.title}</h3>
              <p className="text-slate-600 text-sm">{item.desc}</p>
            </motion.div>
          ))}
        </div>

        <div className="bg-slate-900 text-white p-12 rounded-3xl text-center shadow-2xl relative overflow-hidden">
          <div className="absolute top-0 left-0 w-full h-full bg-blue-600 opacity-10 rounded-3xl"></div>
          <h2 className="text-3xl font-bold mb-4 relative z-10">{getField("cta_title", "title") || "Ready?"}</h2>
          <p className="text-slate-400 mb-8 relative z-10">{getField("cta_text") || "Join the platform."}</p>
          <Link to="/contact" className="bg-blue-500 hover:bg-blue-600 text-white px-8 py-3 rounded-full font-bold transition relative z-10">Get Started</Link>
        </div>
      </div>
    </div>
  );
}