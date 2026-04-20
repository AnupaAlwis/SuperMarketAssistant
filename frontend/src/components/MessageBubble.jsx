import React from 'react';
import './MessageBubble.css';

const MessageBubble = ({ message, sender }) => {
  const isBot = sender === 'bot';
  
  return (
    <div className={`message-container ${isBot ? 'bot-container' : 'user-container'}`}>
      <div className={`message-bubble ${isBot ? 'bot-bubble' : 'user-bubble'}`}>
        <div className="message-header">
          {isBot ? '🛒 Assistant' : 'You'}
        </div>
        <div className="message-content">
          {message}
        </div>
      </div>
    </div>
  );
};

export default MessageBubble;
