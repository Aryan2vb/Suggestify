import os

import mysql

from flask import Flask, request, jsonify
from trie import Trie
from db_config import get_connection

app = Flask(__name__)
trie = Trie()

# Preload the Trie from MySQL
def load_words_into_trie():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT word FROM words")
    for (word,) in cursor.fetchall():
        trie.insert(word)
    cursor.close()
    connection.close()

load_words_into_trie()


@app.route('/', methods=['GET'])
def g():
    return jsonify({
        "message": "Welcome to the Suggestify API!",
        "endpoints": {
            "/insert": {
                "method": "POST",
                "description": "Insert a single word.",
                "request": {"word": "string"}
            },
            "/bulk-insert": {
                "method": "POST",
                "description": "Insert multiple words.",
                "request": {"words": ["string1", "string2", ...]}
            },
            "/search": {
                "method": "GET",
                "description": "Search for words matching a prefix.",
                "parameters": {"prefix": "string"}
            }
        },
        "For more info": {  # Added this line
            "message": "Welcome to the Suggestify API!",
            "documentation": "https://github.com/Aryan2vb/Suggestify-Backend/blob/main/README.md"
        }  # Added this line
    })


@app.route('/insert', methods=['POST'])
def insert_word():
    word = request.json.get('word')
    if not word:
        return jsonify({"error": "Word is required"}), 400

    # Insert into MySQL
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO words (word) VALUES (%s)", (word,))
        connection.commit()
        trie.insert(word)  # Insert into Trie
        message = {"message": f"Word '{word}' added successfully!"}
    except mysql.connector.IntegrityError:
        message = {"error": f"Word '{word}' already exists."}
    finally:
        cursor.close()
        connection.close()

    return jsonify(message)

@app.route('/search', methods=['GET'])
def search_prefix():
    prefix = request.args.get('prefix', '')
    results = trie.search(prefix)
    return jsonify({"results": results})

@app.route('/bulk-insert', methods=['POST'])
def bulk_insert():
    """Insert bulk data into Trie and MySQL."""
    data = request.json  # Expecting a JSON array of strings
    if not isinstance(data, list):
        return jsonify({"error": "Invalid input format. Expected a list of strings."}), 400

    connection = get_connection()
    cursor = connection.cursor()
    try:
        # Bulk insert into MySQL
        cursor.executemany("INSERT IGNORE INTO words (word) VALUES (%s)", [(word,) for word in data])
        connection.commit()

        # Bulk insert into Trie
        for word in data:
            for i in range(len(word)):
                st = ""
                for j in range(i,len(word)):
                    st += word[j]
                    trie.insert(st)

        return jsonify({"message": f"Successfully inserted {len(data)} words."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 3001)))
