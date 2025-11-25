// src/components/Chatbot.jsx

import React, { useState, useEffect, useRef } from 'react';
import { Bot, User, Send, MessageSquare, Loader } from 'lucide-react';
import axios from 'axios'; 
import useThemeSettings from '../hooks/useThemeSettings'; 

// --- DUMMY AXIOS INSTANCE (Replace with your actual configured instance) ---
const api = axios.create({
    baseURL: '/api', 
});
// --------------------------------------------------------------------------

const Chatbot = () => {
    // Get configurable welcome message from ThemeSetting
    const { settings, loading: settingsLoading } = useThemeSettings(); 
    // Default fallback if settings are still loading or not found
    const welcomeMessage = settings?.chatbot_welcome_message || "Welcome to XpertAI. To help you better, I need a few details. Shall we start?";

    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState([]);
    const [inputValue, setInputValue] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    
    // currentField holds the Lead model field the bot expects an answer for ('name', 'email', etc.)
    const [currentField, setCurrentField] = useState(null); 
    const messagesEndRef = useRef(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    // Function to start or continue the flow
    const startFlow = async (isRestart = false) => {
        setIsLoading(true);
        try {
            // Send null to signal the start of a new flow, or restart
            const response = await api.post('/chatbot-flow/', {
                current_field: null, 
                answer: null
            });
            const data = response.data;

            const initialMessages = [
                { sender: 'bot', text: isRestart ? "Starting a fresh chat. Let's begin!" : welcomeMessage },
                { sender: 'bot', text: data.next_question }
            ];

            setMessages(initialMessages);
            setCurrentField(data.next_field);
        } catch (error) {
            console.error("Error starting chatbot flow:", error);
            setMessages([
                { sender: 'bot', text: 'I am experiencing connection issues. Please try again later.' }
            ]);
        } finally {
            setIsLoading(false);
        }
    };

    // Send answer and get next question
    const handleSend = async (answer = inputValue.trim()) => {
        if (!answer || currentField === null) return; 

        // 1. Display user message
        setMessages(prev => [...prev, { sender: 'user', text: answer }]);
        setInputValue('');
        setIsLoading(true);

        try {
            // 2. Send answer to the flow handler
            const response = await api.post('/chatbot-flow/', {
                current_field: currentField, // The field we just answered
                answer: answer
            });
            const data = response.data;
            
            // 3. Update state based on response
            setMessages(prev => [...prev, { sender: 'bot', text: data.next_question }]);
            setCurrentField(data.next_field); 

            if (data.is_complete) {
                // Lead captured successfully (Task 3)
                console.log("Lead captured:", data.action);
                setCurrentField(null); // Stop conversation
            }

            if (data.error) {
                 // Handle errors (e.g., system error and restart)
                setMessages(prev => [...prev, { sender: 'bot', text: data.error }]);
                setCurrentField(data.next_field); 
            }

        } catch (error) {
            console.error("Error handling flow step:", error);
            // Fallback for network issues or unhandled server errors
            setMessages(prev => [...prev, { sender: 'bot', text: 'A network error occurred. Please try sending your message again.' }]);
            
        } finally {
            setIsLoading(false);
        }
    };

    // Initial flow start on open
    useEffect(() => {
        if (isOpen && messages.length === 0 && !settingsLoading) {
            startFlow();
        }
    }, [isOpen, settingsLoading]);

    // Scroll to the bottom on new message
    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleKeyDown = (e) => {
        if (e.key === 'Enter' && inputValue.trim() && !isLoading && currentField !== null) {
            handleSend();
        }
    };

    const handleRestart = () => {
        setMessages([]);
        setCurrentField(null);
        startFlow(true);
    };

    return (
        <>
            {/* Chat button */}
            <button
                className="fixed bottom-6 right-6 bg-blue-600 text-white p-4 rounded-full shadow-xl hover:bg-blue-700 transition z-50"
                onClick={() => setIsOpen(!isOpen)}
                aria-label="Open Chatbot"
            >
                <MessageSquare size={24} />
            </button>

            {/* Chat Window */}
            {isOpen && (
                <div className="fixed bottom-20 right-6 w-80 h-96 bg-white border border-gray-300 rounded-lg shadow-2xl flex flex-col z-50">
                    
                    {/* Header */}
                    <div className="bg-slate-800 text-white p-3 rounded-t-lg flex justify-between items-center">
                        <h3 className="font-semibold text-lg">XpertAI Assistant</h3>
                        <div className="flex items-center space-x-2">
                             <button onClick={handleRestart} className="text-sm text-gray-400 hover:text-white" title="Restart Chat">Restart</button>
                             <button onClick={() => setIsOpen(false)} className="text-gray-400 hover:text-white">&times;</button>
                        </div>
                    </div>

                    {/* Messages Container */}
                    <div className="flex-1 overflow-y-auto p-3 space-y-3">
                        {messages.map((msg, index) => (
                            <div key={index} className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
                                <div className={`max-w-xs p-2 rounded-lg text-sm shadow-md ${
                                    msg.sender === 'user' 
                                    ? 'bg-blue-500 text-white' 
                                    : 'bg-gray-100 text-gray-800 border'
                                }`}>
                                    {msg.sender === 'bot' && <Bot size={14} className="inline mr-1" />}
                                    {msg.sender === 'user' && <User size={14} className="inline mr-1" />}
                                    {msg.text}
                                </div>
                            </div>
                        ))}
                        {isLoading && (
                            <div className="flex justify-start">
                                <div className="max-w-xs p-2 rounded-lg text-sm bg-gray-100 text-gray-800 border flex items-center">
                                    <Loader size={14} className="animate-spin mr-2" />
                                    Typing...
                                </div>
                            </div>
                        )}
                        <div ref={messagesEndRef} />
                    </div>

                    {/* Input Area */}
                    <div className="p-3 border-t">
                        <div className="flex">
                            <input
                                type="text"
                                className="flex-1 p-2 border border-gray-300 rounded-l-lg focus:outline-none"
                                placeholder={currentField ? `Enter your ${currentField}...` : "Chat is complete. Click Restart."}
                                value={inputValue}
                                onChange={(e) => setInputValue(e.target.value)}
                                onKeyDown={handleKeyDown}
                                disabled={isLoading || currentField === null}
                            />
                            <button
                                className={`p-2 rounded-r-lg text-white transition ${
                                    currentField !== null && !isLoading ? 'bg-blue-600 hover:bg-blue-700' : 'bg-gray-400 cursor-not-allowed'
                                }`}
                                onClick={() => handleSend()}
                                disabled={!inputValue.trim() || isLoading || currentField === null}
                            >
                                <Send size={20} />
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </>
    );
};

export default Chatbot;