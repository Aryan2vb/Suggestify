Suggestify Backend

Suggestify is a backend API built with Flask and Trie data structure, deployed on Render. It supports autocomplete functionality, allowing you to insert words into a trie and search for suggestions based on a prefix.

API Endpoints

1. Insert Word

POST /insert
	•	Description: Inserts a word into the trie data structure.
	•	Request Body:

{
  "word": "example"
}


	•	Response:

{
  "message": "Word 'example' added successfully!"
}


	•	Error Response:

{
  "error": "Word is required"
}


	•	Status Codes:
	•	201 (Created) if the word is added successfully.
	•	400 (Bad Request) if no word is provided.

2. Search Suggestions

GET /search
	•	Description: Retrieves a list of suggestions based on a given prefix.
	•	Query Parameters:
	•	prefix (string): The prefix to search for in the trie.
	•	Example Request:

GET /search?prefix=exa


	•	Response:

{
  "results": ["example", "examine", "exalted"]
}


	•	Status Codes:
	•	200 (OK) if the suggestions are found successfully.
	•	400 (Bad Request) if no prefix is provided.

Getting Started

Prerequisites

	1.	Python 3.x (preferably Python 3.8 or higher).
	2.	Flask: Python web framework.
	3.	Flask-CORS: To handle Cross-Origin Resource Sharing (CORS).
	4.	Werkzeug: For WSGI utilities and routing.

Installing

	1.	Clone the repository:

git clone https://github.com/your-repo/suggestify-backend.git
cd suggestify-backend


	2.	Set up a virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
.\venv\Scripts\activate  # For Windows


	3.	Install the required dependencies:

pip install -r requirements.txt



Environment Variables

Make sure to set the following environment variables for your app:
	•	DATABASE_URL: Your database connection string.
	•	FLASK_ENV: The environment (development, production).

You can create a .env file in the root directory with the following content:

DATABASE_URL=your-database-url
FLASK_ENV=development

Running the Server Locally

	1.	Start the Flask server:

python main.py


	2.	The server will be running on http://127.0.0.1:5000. You can make requests to the following endpoints:
	•	POST /insert
	•	GET /search

Deploying to Render

To deploy the backend to Render:
	1.	Create a Render account: If you don’t have one, sign up at Render.
	2.	Create a new web service:
	•	Go to your Render dashboard and create a new web service.
	•	Connect it to your GitHub repository.
	•	Choose Python as the environment.
	•	Set the port to 5000 (default for Flask).
	•	Configure the environment variables (DATABASE_URL, FLASK_ENV) in the Render dashboard.
	3.	Deploy: Render will automatically build and deploy your Flask application.

Testing the API

You can use tools like Postman, curl, or Axios in your frontend to interact with the API.

Example cURL Request:

Insert Word:

curl -X POST https://suggestify-2.onrender.com/insert \
    -H "Content-Type: application/json" \
    -d '{"word": "example"}'

Search Prefix:

curl "https://suggestify-2.onrender.com/search?prefix=exa"

Troubleshooting

	•	CORS Errors: If you’re running a frontend on a different domain, ensure that CORS is configured correctly. Flask-CORS is already included to handle CORS issues.
	•	Missing Environment Variables: Make sure all environment variables are correctly set in both local development and production (Render).