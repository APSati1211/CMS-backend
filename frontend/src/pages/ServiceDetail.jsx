import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { getServiceBySlug } from "../api";
import { ArrowLeft } from "lucide-react";
import { motion } from "framer-motion";

export default function ServiceDetail() {
  const { slug } = useParams();
  const [service, setService] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    getServiceBySlug(slug)
      .then((res) => {
        setService(res.data);
        setLoading(false);
      })
      .catch(() => {
        setLoading(false);
      });
  }, [slug]);

  if (loading) return <div className="text-center py-20 text-lg">Loading details...</div>;
  if (!service) return <div className="text-center py-20 text-red-500 text-lg">Service not found.</div>;

  return (
    <div className="min-h-screen bg-white">
      <div className="bg-primary text-white py-16 px-6 text-center">
        <Link to="/services" className="inline-flex items-center text-white/80 hover:text-white hover:underline mb-6 transition">
          <ArrowLeft size={20} className="mr-2" /> Back to Services
        </Link>
        <h1 className="text-4xl md:text-5xl font-extrabold drop-shadow-lg">{service.title}</h1>
      </div>

      <div className="max-w-4xl mx-auto px-6 py-16">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="prose prose-lg max-w-none text-gray-700 leading-relaxed"
          dangerouslySetInnerHTML={{ __html: service.full_description }} 
        />

        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          className="mt-16 p-10 bg-gray-50 rounded-2xl border border-gray-200 text-center shadow-sm"
        >
          <h3 className="text-2xl font-bold text-gray-800 mb-4">Need expert help with {service.title}?</h3>
          <Link to="/contact" className="inline-block bg-secondary text-white px-8 py-4 rounded-xl font-bold shadow-lg hover:bg-orange-600 transition">
            Get a Custom Quote
          </Link>
        </motion.div>
      </div>
    </div>
  );
}