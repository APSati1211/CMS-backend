import { motion } from "framer-motion";
import usePageContent from "../hooks/usePageContent";
import { Star } from "lucide-react";

export default function Features() {
  const { getField, loading } = usePageContent("features");

  if (loading) return <div className="text-center py-20">Loading...</div>;

  // Generate 6 cards dynamically
  const featuresList = Array.from({ length: 6 }).map((_, i) => ({
    title: getField(`feature_card_${i+1}_title`, "title") || `Feature ${i+1}`,
    desc: getField(`feature_card_${i+1}_desc`) || "Advanced capabilities to power your business.",
  }));

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="bg-slate-900 text-white py-24 text-center px-6">
        <h1 className="text-4xl font-bold mb-4">{getField("hero_title", "title") || "Core Features"}</h1>
        <p className="text-slate-400 max-w-2xl mx-auto">{getField("hero_text") || "Explore the tools that drive your success."}</p>
      </div>

      <div className="max-w-7xl mx-auto px-6 py-20 grid md:grid-cols-3 gap-8">
        {featuresList.map((feat, i) => (
          <motion.div 
            key={i}
            initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} transition={{ delay: i * 0.1 }}
            className="bg-white p-8 rounded-2xl shadow-md hover:shadow-xl transition border border-slate-100"
          >
            <div className="bg-yellow-100 w-12 h-12 rounded-lg flex items-center justify-center text-yellow-600 mb-6">
              <Star size={24} />
            </div>
            <h3 className="text-xl font-bold text-slate-800 mb-3">{feat.title}</h3>
            <p className="text-slate-600">{feat.desc}</p>
          </motion.div>
        ))}
      </div>
    </div>
  );
}