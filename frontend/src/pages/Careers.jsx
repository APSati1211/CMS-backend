import { useEffect, useState } from "react";
import { getJobs, applyForJob } from "../api";
import { motion, AnimatePresence } from "framer-motion";
import { MapPin, Clock, Briefcase, X, CheckCircle, Loader2 } from "lucide-react";
import usePageContent from "../hooks/usePageContent";

export default function Careers() {
  const { getField } = usePageContent("careers");
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedJob, setSelectedJob] = useState(null); // For Modal

  useEffect(() => {
    getJobs().then((res) => { setJobs(res.data); setLoading(false); });
  }, []);

  return (
    <div className="min-h-screen bg-slate-50 pb-20">
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-24 text-center px-6">
        <h1 className="text-5xl font-bold mb-4">{getField("hero_title", "title") || "Join Our Team"}</h1>
        <p className="text-xl opacity-90 max-w-2xl mx-auto">{getField("hero_text") || "Build the future of financial intelligence with us."}</p>
      </div>

      <div className="max-w-5xl mx-auto px-6 mt-16">
        <h2 className="text-3xl font-bold text-slate-800 mb-8">{getField("openings_title", "title") || "Current Openings"}</h2>
        {loading ? <p className="text-center text-gray-500">Loading openings...</p> : (
          <div className="space-y-6">
            {jobs.map((job) => (
              <motion.div 
                key={job.id} initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }}
                className="bg-white p-8 rounded-2xl shadow-sm hover:shadow-md transition border border-slate-100 flex flex-col md:flex-row justify-between items-start md:items-center gap-6"
              >
                <div>
                  <h3 className="text-2xl font-bold text-slate-800 mb-2">{job.title}</h3>
                  <div className="flex flex-wrap gap-4 text-slate-500 text-sm">
                    <span className="flex items-center gap-1"><Briefcase size={16} /> {job.department}</span>
                    <span className="flex items-center gap-1"><MapPin size={16} /> {job.location}</span>
                    <span className="flex items-center gap-1"><Clock size={16} /> {job.type}</span>
                  </div>
                </div>
                <button 
                  onClick={() => setSelectedJob(job)} 
                  className="bg-slate-900 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-600 transition"
                >
                  Apply Now
                </button>
              </motion.div>
            ))}
          </div>
        )}
      </div>

      {/* APPLICATION MODAL */}
      <ApplicationModal job={selectedJob} onClose={() => setSelectedJob(null)} />
    </div>
  );
}

function ApplicationModal({ job, onClose }) {
  const [form, setForm] = useState({ applicant_name: "", email: "", resume_link: "", cover_letter: "" });
  const [status, setStatus] = useState("idle"); // idle, sending, success, error

  if (!job) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus("sending");
    try {
      await applyForJob({ ...form, job: job.id });
      setStatus("success");
      setTimeout(() => { onClose(); setStatus("idle"); setForm({ applicant_name: "", email: "", resume_link: "", cover_letter: "" }); }, 2000);
    } catch (error) {
      console.error(error);
      setStatus("error");
    }
  };

  return (
    <AnimatePresence>
      <motion.div 
        initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
        className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4"
      >
        <motion.div 
          initial={{ scale: 0.9, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} exit={{ scale: 0.9, opacity: 0 }}
          className="bg-white rounded-2xl shadow-2xl w-full max-w-lg overflow-hidden"
        >
          <div className="bg-slate-900 text-white p-6 flex justify-between items-center">
            <h3 className="text-xl font-bold">Apply for {job.title}</h3>
            <button onClick={onClose} className="hover:bg-white/10 p-1 rounded"><X size={20} /></button>
          </div>
          
          <div className="p-8">
            {status === "success" ? (
              <div className="text-center py-10">
                <CheckCircle size={64} className="text-green-500 mx-auto mb-4" />
                <h3 className="text-2xl font-bold text-slate-800">Application Sent!</h3>
                <p className="text-slate-500">Best of luck! We'll review it shortly.</p>
              </div>
            ) : (
              <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Full Name</label>
                  <input required type="text" className="w-full p-3 border rounded-lg bg-slate-50 focus:ring-2 focus:ring-blue-500 outline-none"
                    value={form.applicant_name} onChange={e => setForm({...form, applicant_name: e.target.value})} />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Email Address</label>
                  <input required type="email" className="w-full p-3 border rounded-lg bg-slate-50 focus:ring-2 focus:ring-blue-500 outline-none"
                    value={form.email} onChange={e => setForm({...form, email: e.target.value})} />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Resume Link (Google Drive/LinkedIn)</label>
                  <input required type="url" className="w-full p-3 border rounded-lg bg-slate-50 focus:ring-2 focus:ring-blue-500 outline-none"
                    value={form.resume_link} onChange={e => setForm({...form, resume_link: e.target.value})} placeholder="https://..." />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Cover Letter (Optional)</label>
                  <textarea rows="3" className="w-full p-3 border rounded-lg bg-slate-50 focus:ring-2 focus:ring-blue-500 outline-none"
                    value={form.cover_letter} onChange={e => setForm({...form, cover_letter: e.target.value})}></textarea>
                </div>
                
                {status === "error" && <p className="text-red-500 text-sm">Something went wrong. Please try again.</p>}
                
                <button type="submit" disabled={status === "sending"} className="w-full bg-blue-600 text-white py-3 rounded-lg font-bold hover:bg-blue-700 transition flex justify-center items-center gap-2">
                  {status === "sending" ? <><Loader2 className="animate-spin" /> Sending...</> : "Submit Application"}
                </button>
              </form>
            )}
          </div>
        </motion.div>
      </motion.div>
    </AnimatePresence>
  );
}