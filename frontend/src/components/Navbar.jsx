import { useState, useEffect } from "react";
import { Link, useLocation } from "react-router-dom";
import { Menu, X, ChevronDown, ChevronRight, ExternalLink } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import axios from "axios";

export default function Navbar({ logo }) {
  const [isOpen, setIsOpen] = useState(false);
  const [hovered, setHovered] = useState(null); // For Dropdown
  const [scrolled, setScrolled] = useState(false);
  const [dynamicPages, setDynamicPages] = useState([]);
  const location = useLocation();

  // --- Scroll & Dynamic Pages Fetching ---
  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 50);
    window.addEventListener("scroll", handleScroll);

    // Fetch extra pages created in CMS
    axios.get("http://127.0.0.1:8000/api/pages/")
      .then(res => setDynamicPages(res.data))
      .catch(err => console.error("Menu fetch error", err));

    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  // --- LINKS CONFIGURATION ---
  const mainLinks = [
    { name: "Home", path: "/" },
    { name: "About", path: "/about" },
    { name: "Services", path: "/services" },
    { name: "Careers", path: "/careers" },
    { name: "Resources", path: "/resources" },
  ];

  // Dropdown Links (Static + Dynamic from CMS)
  const dropdownLinks = [
    { name: "Stakeholders", path: "/stakeholders" },
    { name: "Features", path: "/features" },
    { name: "Blog", path: "/blog" },
    { name: "Lead System", path: "/lead-system" },
    ...dynamicPages.map(page => ({ name: page.title, path: `/${page.slug}` })) // Dynamic pages added here
  ];

  return (
    <motion.nav
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ duration: 0.6, type: "spring" }}
      className={`fixed top-0 w-full z-50 transition-all duration-300 ${
        scrolled 
          ? "bg-slate-900/80 backdrop-blur-xl border-b border-white/10 shadow-2xl py-3" 
          : "bg-transparent py-5"
      }`}
    >
      <div className="max-w-7xl mx-auto px-6 flex justify-between items-center">
        
        {/* 🧊 LOGO SECTION */}
        <Link to="/" className="relative z-50">
          {logo ? (
            <motion.img 
              src={logo} 
              alt="XpertAI Global" 
              whileHover={{ scale: 1.05 }}
              className="h-10 md:h-12 object-contain" 
            />
          ) : (
            <motion.div
              whileHover={{ scale: 1.05 }}
              className="text-2xl font-extrabold tracking-tighter flex items-center gap-2"
            >
              <span className="bg-gradient-to-r from-blue-400 to-purple-500 text-transparent bg-clip-text drop-shadow-lg">
                XpertAI
              </span>
              <span className="text-white">Global</span>
            </motion.div>
          )}
        </Link>

        {/* 🖥️ DESKTOP MENU */}
        <div className="hidden md:flex items-center gap-8">
          {mainLinks.map((link) => (
            <Link 
              key={link.name} 
              to={link.path} 
              className="relative group py-2"
            >
              <span className={`text-sm font-medium transition-colors duration-300 ${
                location.pathname === link.path ? "text-blue-400" : "text-slate-300 group-hover:text-white"
              }`}>
                {link.name}
              </span>
              <span className={`absolute bottom-0 left-0 h-0.5 bg-blue-500 transition-all duration-300 shadow-[0_0_10px_#3b82f6] ${
                location.pathname === link.path ? "w-full" : "w-0 group-hover:w-full"
              }`}></span>
            </Link>
          ))}

          {/* 🔥 SEXY DROPDOWN */}
          <div 
            className="relative group"
            onMouseEnter={() => setHovered(true)}
            onMouseLeave={() => setHovered(false)}
          >
            <button className="flex items-center gap-1 text-sm font-medium text-slate-300 hover:text-white transition-colors py-2">
              More <ChevronDown size={14} className={`transition-transform duration-300 ${hovered ? "rotate-180 text-blue-400" : ""}`} />
            </button>

            <AnimatePresence>
              {hovered && (
                <motion.div
                  initial={{ opacity: 0, y: 15, scale: 0.95 }}
                  animate={{ opacity: 1, y: 0, scale: 1 }}
                  exit={{ opacity: 0, y: 10, scale: 0.95 }}
                  transition={{ duration: 0.2, ease: "easeOut" }}
                  className="absolute top-full right-0 mt-2 w-56 bg-slate-900/90 backdrop-blur-2xl border border-white/10 rounded-2xl shadow-[0_20px_50px_rgba(8,_112,_184,_0.7)] overflow-hidden ring-1 ring-white/20"
                >
                  <div className="p-2 space-y-1">
                    <div className="px-4 py-2 text-xs font-semibold text-slate-500 uppercase tracking-wider">
                      Explore More
                    </div>
                    {dropdownLinks.map((link) => (
                      <Link
                        key={link.name}
                        to={link.path}
                        className="flex items-center justify-between px-4 py-2.5 text-sm text-slate-300 hover:text-white hover:bg-gradient-to-r hover:from-blue-600/20 hover:to-purple-600/10 rounded-xl transition-all group/item"
                      >
                        {link.name}
                        <ChevronRight size={14} className="opacity-0 -translate-x-2 group-hover/item:opacity-100 group-hover/item:translate-x-0 transition-all text-blue-400" />
                      </Link>
                    ))}
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </div>

          {/* CTA BUTTON */}
          <Link to="/contact">
            <motion.button
              whileHover={{ scale: 1.05, boxShadow: "0px 0px 25px rgba(59, 130, 246, 0.6)" }}
              whileTap={{ scale: 0.95 }}
              className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-2.5 rounded-full font-bold text-sm border border-white/20 shadow-lg ml-2"
            >
              Get Started
            </motion.button>
          </Link>
        </div>

        {/* 📱 MOBILE TOGGLE */}
        <button 
          className="md:hidden text-white p-2 z-50 relative"
          onClick={() => setIsOpen(!isOpen)}
        >
          {isOpen ? <X size={28} /> : <Menu size={28} />}
        </button>
      </div>

      {/* 📱 MOBILE MENU (Full Screen) */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, x: "100%" }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: "100%" }}
            transition={{ type: "tween", duration: 0.3 }}
            className="fixed inset-0 bg-slate-900/95 backdrop-blur-xl z-40 md:hidden flex flex-col pt-24 px-6 overflow-y-auto"
          >
            <div className="space-y-2">
              {[...mainLinks, ...dropdownLinks].map((link, idx) => (
                <motion.div
                  key={link.name}
                  initial={{ opacity: 0, x: 50 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: idx * 0.05 }}
                >
                  <Link 
                    to={link.path} 
                    onClick={() => setIsOpen(false)}
                    className={`flex items-center justify-between p-4 rounded-xl text-lg font-medium transition-all ${
                      location.pathname === link.path 
                        ? "bg-blue-600/20 text-blue-400 border border-blue-500/30" 
                        : "text-slate-300 hover:bg-white/5"
                    }`}
                  >
                    {link.name}
                    <ExternalLink size={18} className="opacity-50" />
                  </Link>
                </motion.div>
              ))}
            </div>

            <motion.div 
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4 }}
              className="mt-8"
            >
              <Link 
                to="/contact" 
                onClick={() => setIsOpen(false)}
                className="block w-full bg-gradient-to-r from-blue-600 to-purple-600 text-white text-center py-4 rounded-2xl font-bold text-xl shadow-xl border border-white/20"
              >
                Contact Us Now
              </Link>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.nav>
  );
}