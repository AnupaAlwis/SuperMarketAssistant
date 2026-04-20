import React, { useEffect, useRef } from 'react';
import MessageBubble from './MessageBubble';
import './ChatWindow.css';

const ChatWindow = ({ messages, isLoading }) => {
  const scrollRef = useRef(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, isLoading]);

  return (
    <div className="chat-window" ref={scrollRef}>
      {messages.length === 0 && (
        <div className="welcome-screen">
          <div className="welcome-icon">🛒</div>
          <h2>Supermarket Assistant</h2>
          <p>Ask me about product prices, stock availability, or get healthy recommendations!</p>
        </div>
      )}
      
      {messages.map((msg, index) => (
        <MessageBubble key={index} message={msg.text} sender={msg.sender} />
      ))}

      {isLoading && (
        <div className="typing-indicator">
          <span></span>
          <span></span>
          <span></span>
          <p>Assistant is typing...</p>
        </div>
      )}
    </div>
  );
};

export default ChatWindow;
