import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getServices } from "../api";
import { ArrowRight, Briefcase } from "lucide-react";
import { motion } from "framer-motion";
import usePageContent from "../hooks/usePageContent"; // CMS Content for Hero

export default function Services() {
  const { getField } = usePageContent("services");
  const [services, setServices] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getServices().then((res) => { setServices(res.data); setLoading(false); });
  }, []);

  return (
    <div className="min-h-screen bg-slate-50 pb-20">
      {/* Hero */}
      <div className="bg-gradient-to-br from-blue-900 to-slate-900 text-white py-24 text-center px-6">
        <motion.h1 
          initial={{ opacity: 0, y: -20 }} animate={{ opacity: 1, y: 0 }}
          className="text-5xl font-bold mb-6"
        >
          {getField("hero_title", "title") || "Our Services"}
        </motion.h1>
        <p className="text-xl text-blue-100 max-w-3xl mx-auto">
          {getField("hero_text") || "End-to-end financial solutions tailored for your growth."}
        </p>
      </div>

      {/* Services Grid */}
      <div className="max-w-7xl mx-auto px-6 mt-16">
        {loading ? <p className="text-center">Loading...</p> : (
          <div className="grid md:grid-cols-3 gap-8">
            {services.map((service, index) => (
              <motion.div 
                key={service.id}
                initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} transition={{ delay: index * 0.1 }}
                whileHover={{ y: -10 }}
                className="bg-white p-8 rounded-2xl shadow-lg hover:shadow-2xl transition-all border border-slate-100 group"
              >
                <div className="w-14 h-14 bg-blue-50 rounded-xl flex items-center justify-center text-blue-600 mb-6 group-hover:bg-blue-600 group-hover:text-white transition-colors">
                  <Briefcase size={28} />
                </div>
                <h3 className="text-2xl font-bold text-slate-800 mb-3">{service.title}</h3>
                <p className="text-slate-600 mb-6 line-clamp-3">{service.short_description}</p>
                <Link to={`/services/${service.slug}`} className="inline-flex items-center text-blue-600 font-bold hover:translate-x-2 transition-transform">
                  Read More <ArrowRight size={18} className="ml-2" />
                </Link>
              </motion.div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}