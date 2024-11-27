import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [query, setQuery] = useState('');
  const [suggestions, setSuggestions] = useState([]);
  const [word, setWord] = useState('');

  // GET request for searching suggestions
  const handleSearch = async () => {
    try {
      const response = await axios.get('https://suggestify-2.onrender.com/search', {
        params: { prefix: query },
      });
      setSuggestions(response.data.results);
    } catch (error) {
      console.error('Error fetching suggestions:', error);
    }
  };

  // POST request for inserting a word
  const handleInsert = async () => {
    if (!word) return alert('Please enter a word to insert');
    try {
      const response = await axios.post('https://suggestify-2.onrender.com/insert', {
        word: word,
      });
      alert(response.data.message);
      setWord(''); // Reset input after insertion
    } catch (error) {
      console.error('Error inserting word:', error);
    }
  };

  return (
    <div className="App">
      <h1>Trie Search and Insert</h1>

      {/* Search Bar */}
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search words"
      />
      <button onClick={handleSearch}>Search</button>

      {/* Display Suggestions */}
      <ul>
        {suggestions.map((suggestion, index) => (
          <li key={index}>{suggestion}</li>
        ))}
      </ul>

      {/* Insert Word */}
      <input
        type="text"
        value={word}
        onChange={(e) => setWord(e.target.value)}
        placeholder="Insert a word"
      />
      <button onClick={handleInsert}>Insert Word</button>
    </div>
  );
}

export default App;