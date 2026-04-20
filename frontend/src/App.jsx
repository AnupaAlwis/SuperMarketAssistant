import { useState } from 'react'
import './App.css'
import ChatWindow from './components/ChatWindow'
import InputBox from './components/InputBox'
import { sendMessage } from './services/api'

function App() {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSendMessage = async (text) => {
    // Add user message
    const newMessage = { text, sender: 'user' };
    setMessages((prev) => [...prev, newMessage]);
    setIsLoading(true);
    setError(null);

    try {
      const data = await sendMessage(text);
      setMessages((prev) => [...prev, { text: data.response, sender: 'bot' }]);
    } catch (err) {
      setError('Sorry, I failed to connect to the assistant. Please make sure the backend is running.');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="header-content">
          <h1>🛒 Supermarket AI Assistant</h1>
          <div className="status-badge">
            <span className="dot"></span> Online
          </div>
        </div>
      </header>
      
      <main className="chat-container">
        {error && (
          <div className="error-banner">
            {error}
          </div>
        )}
        <ChatWindow messages={messages} isLoading={isLoading} />
        <InputBox onSendMessage={handleSendMessage} disabled={isLoading} />
      </main>
    </div>
  )
}

export default App
