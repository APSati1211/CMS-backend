import { useEffect, useState } from "react";
// Assuming getCategories and getBlogs functions are correctly defined in src/api/index.js 
import { getBlogs, getCategories } from "../api"; 
import { motion } from "framer-motion";
import { Calendar, User, List } from "lucide-react"; 
import usePageContent from "../hooks/usePageContent"; 

export default function Blog() {
  const { getField } = usePageContent("blog"); 
  const [posts, setPosts] = useState([]);
  const [categories, setCategories] = useState([]);
  // selectedCategory mein 'null' hone par sabhi blogs dikhenge
  const [selectedCategory, setSelectedCategory] = useState(null); 
  const [loading, setLoading] = useState(true);

  // --- HANDLER FOR CATEGORY CLICKS (Task 4) ---
  const handleCategoryClick = (slug) => {
    // Agar current category par click ho, toh filter hata do (null set kar do)
    setSelectedCategory(currentSlug => currentSlug === slug ? null : slug);
  };

  // --- EFFECT 1: Fetch Categories (Task 4) ---
  useEffect(() => {
    // Backend API endpoint: /api/blog-categories/
    getCategories()
      .then((res) => setCategories(res.data))
      .catch(err => console.error("Error fetching categories:", err));
  }, []);

  // --- EFFECT 2: Fetch Filtered Blog Posts (Task 4) ---
  useEffect(() => {
    setLoading(true);
    // Backend API call: /api/blogs/ ya /api/blogs/?category=slug
    getBlogs(selectedCategory)
      .then((res) => { 
        setPosts(res.data); 
      })
      .catch(err => {
          console.error("Error fetching blogs:", err);
      })
      .finally(() => {
        setLoading(false);
      });
  }, [selectedCategory]); 
  
  // Current active filter ka naam display karne ke liye
  const currentFilterName = categories.find(cat => cat.slug === selectedCategory)?.name;

  return (
    <div className="min-h-screen bg-slate-50 pb-20">
      
      {/* Hero Section */}
      <div className="bg-slate-900 text-white py-24 text-center px-6">
        <h1 className="text-5xl font-bold mb-4">{getField("hero_title", "title") || "Latest Insights"}</h1>
        {/* Filtered by name display */}
        {selectedCategory && <p className="text-blue-400 font-semibold text-lg mb-2">Filtered by: {currentFilterName}</p>}
        <p className="text-slate-400">{getField("hero_text") || "Trends, news, and expert analysis from XpertAI."}</p>
      </div>

      <div className="max-w-7xl mx-auto px-6 mt-16 grid lg:grid-cols-4 gap-12">

        {/* Column 1: Sidebar Filters (Filter UI) */}
        <div className="lg:col-span-1 space-y-8">
          
          {/* --- CATEGORY FILTER WIDGET (Task 4) --- */}
          <div className="bg-white p-6 rounded-xl shadow-lg border border-gray-100">
            <h3 className="text-xl font-bold text-slate-800 mb-4 flex items-center gap-2"><List size={20} className="text-blue-600"/> {getField("category_title", "title") || "Filter Categories"}</h3>
            <ul className="space-y-2">
              
              {/* Show All Button (Filter reset) */}
              <li>
                <button
                  onClick={() => setSelectedCategory(null)}
                  className={`w-full text-left py-2 px-3 rounded-lg text-sm font-medium transition-all ${
                    selectedCategory === null ? 'bg-slate-800 text-white shadow-md' : 'hover:bg-gray-200 text-slate-700'
                  }`}
                >
                  All Articles
                </button>
              </li>

              {/* Dynamic Category Buttons */}
              {categories.map((cat) => (
                <li key={cat.slug}>
                  <button
                    onClick={() => handleCategoryClick(cat.slug)}
                    className={`w-full text-left py-2 px-3 rounded-lg text-sm font-medium transition-all ${
                      selectedCategory === cat.slug ? 'bg-blue-600 text-white shadow-md' : 'hover:bg-gray-200 text-slate-700'
                    }`}
                  >
                    {cat.name}
                  </button>
                </li>
              ))}
            </ul>
          </div>
          
          {/* Search Widget (Placeholder) */}
          <div className="bg-white p-6 rounded-xl shadow-lg border border-gray-100">
              <h4 className="text-xl font-bold text-slate-800 mb-4">{getField("search_placeholder", "title") || "Search Posts"}</h4>
              <input type="text" placeholder="Start typing..." className="w-full p-3 border rounded-lg focus:border-blue-500"/>
          </div>

        </div>

        {/* Column 2: Blog Posts Grid */}
        <div className="lg:col-span-3">
          <h2 className="text-3xl font-bold text-slate-800 mb-8">{getField("latest_posts_title", "title") || "Latest Posts"}</h2>
          
          {loading && <p className="text-center text-2xl text-blue-600 py-10">Loading Posts...</p>}
          
          {!loading && posts.length === 0 ? (
            <p className="text-center text-xl text-gray-500 py-10">
              {selectedCategory ? `No articles found in category "${currentFilterName}".` : "No articles published yet."}
            </p>
          ) : (
            <div className="grid md:grid-cols-2 gap-10">
              {posts.map((blog, i) => (
                <motion.div key={blog.id} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.1 }}
                  whileHover={{ y: -10 }} className="bg-white rounded-2xl shadow-lg overflow-hidden group">
                  {blog.image && <div className="h-48 overflow-hidden"><img src={blog.image} alt={blog.title} className="w-full h-full object-cover group-hover:scale-110 transition duration-500" /></div>}
                  <div className="p-6">
                    {/* Dynamic Category Tag */}
                    {blog.category && <span className="text-xs font-semibold text-blue-600 bg-blue-100 px-3 py-1 rounded-full mb-3 inline-block">{blog.category.name || blog.category}</span>}
                    
                    <h3 className="text-xl font-bold text-slate-800 mb-3 group-hover:text-blue-600 transition">{blog.title}</h3>
                    <p className="text-slate-600 text-sm mb-4 line-clamp-3">{blog.short_description}</p>
                    <div className="flex items-center justify-between text-xs text-slate-400 border-t pt-4">
                      <span className="flex items-center gap-1"><Calendar size={14} /> {new Date(blog.created_at).toLocaleDateString()}</span>
                      {/* Task 2: AUTHOR NAME CHANGE RETAINED */}
                      <span className="flex items-center gap-1"><User size={14} /> XpertAI Global</span> 
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}