import { motion } from "framer-motion";
import usePageContent from "../hooks/usePageContent";
import { Users, Briefcase, GraduationCap, Globe } from "lucide-react";

export default function Stakeholders() {
  const { getField, loading } = usePageContent("stakeholders");

  if (loading) return <div className="h-screen flex items-center justify-center">Loading...</div>;

  const hero = {
    title: getField("hero_title", "title") || "Our Ecosystem",
    text: getField("hero_text") || "Connecting clients, professionals, and partners in one unified platform.",
  };

  const cards = [
    { title: "Clients", desc: "Businesses seeking financial excellence.", icon: <Users size={32} className="text-blue-500" /> },
    { title: "Professionals", desc: "CA, CPA, and financial experts.", icon: <Briefcase size={32} className="text-purple-500" /> },
    { title: "Freelancers", desc: "Flexible talent for specific projects.", icon: <Globe size={32} className="text-green-500" /> },
    { title: "Trainers", desc: "Mentors shaping the next generation.", icon: <GraduationCap size={32} className="text-orange-500" /> },
  ];

  return (
    <div className="min-h-screen bg-slate-50 pb-20">
      <div className="bg-slate-900 text-white py-24 text-center px-6 relative overflow-hidden">
        <div className="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-20"></div>
        <motion.h1 initial={{ y: -20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} className="text-5xl font-bold mb-4 relative z-10">{hero.title}</motion.h1>
        <p className="text-slate-400 max-w-2xl mx-auto relative z-10">{hero.text}</p>
      </div>

      <div className="max-w-6xl mx-auto px-6 mt-16 grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        {cards.map((card, i) => (
          <motion.div 
            key={i} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.1 }}
            whileHover={{ y: -5 }} className="bg-white p-8 rounded-2xl shadow-lg border-t-4 border-blue-500 text-center"
          >
            <div className="bg-slate-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6">{card.icon}</div>
            <h3 className="text-xl font-bold text-slate-800 mb-2">{card.title}</h3>
            <p className="text-slate-600 text-sm">{card.desc}</p>
          </motion.div>
        ))}
      </div>
    </div>
  );
}