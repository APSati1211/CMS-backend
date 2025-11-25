import { Link } from "react-router-dom";
import { Facebook, Twitter, Linkedin, Instagram, ArrowUpRight, Mail, MapPin, Phone } from "lucide-react";

// Props mein 'logo' receive kiya
export default function Footer({ logo }) {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-slate-950 text-slate-300 border-t border-white/5 relative overflow-hidden">
      
      {/* Background Decorative Elements */}
      <div className="absolute top-0 left-1/4 w-96 h-96 bg-blue-900/20 rounded-full blur-3xl -translate-y-1/2 pointer-events-none"></div>
      <div className="absolute bottom-0 right-0 w-64 h-64 bg-purple-900/10 rounded-full blur-3xl pointer-events-none"></div>

      <div className="max-w-7xl mx-auto px-6 py-20 relative z-10">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
          
          {/* Column 1: Brand Info */}
          <div className="space-y-6">
            
            {/* DYNAMIC LOGO HERE */}
            {logo ? (
              <img src={logo} alt="XpertAI Global" className="h-12 mb-4 object-contain" />
            ) : (
              <h2 className="text-3xl font-extrabold text-white tracking-tight">
                XpertAI <span className="text-blue-500">Global</span>
              </h2>
            )}

            <p className="text-slate-400 leading-relaxed text-sm">
              Empowering global enterprises with next-gen financial intelligence, automated auditing, and strategic foresight using AI.
            </p>
            <div className="flex gap-4">
              {[Facebook, Twitter, Linkedin, Instagram].map((Icon, i) => (
                <a key={i} href="#" className="bg-white/5 hover:bg-blue-600 p-2.5 rounded-full text-white transition-all duration-300 hover:-translate-y-1">
                  <Icon size={18} />
                </a>
              ))}
            </div>
          </div>

          {/* Column 2: Quick Links */}
          <div>
            <h3 className="text-white font-bold text-lg mb-6">Company</h3>
            <ul className="space-y-4">
              {['About Us', 'Careers', 'Blog', 'Privacy Policy', 'Terms of Service'].map((item) => (
                <li key={item}>
                  <Link to="/" className="hover:text-blue-400 transition-colors flex items-center gap-1 group text-sm">
                    <ArrowUpRight size={14} className="opacity-0 group-hover:opacity-100 transition-opacity" />
                    {item}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Column 3: Services */}
          <div>
            <h3 className="text-white font-bold text-lg mb-6">Services</h3>
            <ul className="space-y-4 text-sm">
              <li><Link to="/services/virtual-cfo" className="hover:text-blue-400 transition">Virtual CFO</Link></li>
              <li><Link to="/services/audit-assurance" className="hover:text-blue-400 transition">Audit & Assurance</Link></li>
              <li><Link to="/services/taxation-services" className="hover:text-blue-400 transition">Taxation Services</Link></li>
              <li><Link to="/services" className="hover:text-blue-400 transition">Financial Analytics</Link></li>
              <li><Link to="/services" className="hover:text-blue-400 transition">Risk Management</Link></li>
            </ul>
          </div>

          {/* Column 4: Contact & Newsletter */}
          <div>
            <h3 className="text-white font-bold text-lg mb-6">Contact Us</h3>
            <div className="space-y-4 text-sm text-slate-400">
              <div className="flex items-start gap-3">
                <MapPin size={18} className="text-blue-500 shrink-0 mt-1" />
                <p>123 Corporate Avenue,<br />Tech Park, Mumbai, India</p>
              </div>
              <div className="flex items-center gap-3">
                <Mail size={18} className="text-blue-500 shrink-0" />
                <a href="mailto:support@xpertai.global" className="hover:text-white transition">support@xpertai.global</a>
              </div>
              <div className="flex items-center gap-3">
                <Phone size={18} className="text-blue-500 shrink-0" />
                <p>+91 98765 43210</p>
              </div>
            </div>

            {/* Mini Newsletter */}
            <div className="mt-8">
              <p className="text-xs text-slate-500 mb-2 uppercase font-bold tracking-wider">Subscribe to Updates</p>
              <div className="flex">
                <input 
                  type="email" 
                  placeholder="Enter email" 
                  className="bg-white/5 border border-white/10 rounded-l-lg px-4 py-2 text-sm text-white w-full focus:outline-none focus:border-blue-500"
                />
                <button className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-r-lg text-white transition">
                  <ArrowUpRight size={18} />
                </button>
              </div>
            </div>
          </div>

        </div>

        {/* Bottom Strip - UPDATED HERE */}
        <div className="mt-20 pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-slate-500">
          <p>&copy; {currentYear} XpertAI Global. All rights reserved.</p>
          <p>Developed by <span className="text-blue-500 font-bold hover:text-blue-400 transition cursor-pointer">WebArclight</span></p>
        </div>
      </div>
    </footer>
  );
}