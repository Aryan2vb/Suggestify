
📝 Suggestify Backend

Suggestify is a powerful backend API built with Flask and Trie data structure. It allows users to insert words and get autocomplete suggestions based on prefixes. The backend is deployed on Render and serves as the core logic of the Suggestify platform.

🚀 Tech Stack

	•	Backend Framework: Flask
	•	Data Structure: Trie (for efficient autocomplete functionality)
	•	Database: Mysql (or your preferred database)
	•	Deployment: Render (Cloud Platform)
	•	API Testing: Postman / cURL
	•	CORS Handling: Flask-CORS
	•	Python Version: 3.11+
	•	Environment: Production, Development

🏗️ API Endpoints

1. Insert Word

POST /insert
	•	Description: Adds a word to the trie data structure.
	•	Request Body:

```
{
  "word": "example"
}
```


•	Response:
```
{
  "message": "Word 'example' added successfully!"
}
```


•	Error Response:
```
{
  "error": "Word is required"
}
```

	•	Status Codes:
	•	201 (Created) - Word added successfully.
	•	400 (Bad Request) - No word provided in the request.

2. Search Suggestions

GET /search
	•	Description: Retrieves autocomplete suggestions for the given prefix.
	•	Query Parameters:
	•	prefix (string): Prefix to search for in the trie.
	•	Example Request:

GET /search?prefix=exa


•	Response:

```
{
  "results": ["example", "examine", "exalted"]
}
```

	•	Status Codes:
	•	200 (OK) - Suggestions returned successfully.
	•	400 (Bad Request) - No prefix provided.

⚙️ Getting Started

Prerequisites

	1.	Python 3.x (Recommended: Python 3.8+)
	2.	Flask: Lightweight web framework for building APIs.
	3.	Flask-CORS: For Cross-Origin Resource Sharing (CORS).
	4.	Werkzeug: Python WSGI utilities and routing.

Installation

	1.	Clone the repository:

git clone https://github.com/your-repo/suggestify-backend.git
cd suggestify-backend


	2.	Create a virtual environment:

python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
.\venv\Scripts\activate  # For Windows


	3.	Install dependencies:

pip install -r requirements.txt

🌍 Environment Variables

Make sure to set the following environment variables for your app to work:
	•	DATABASE_URL: Your database connection URL (e.g., PostgreSQL).
	•	FLASK_ENV: Set to development for local development and production for production.

You can create a .env file in the root directory to store your environment variables:

DATABASE_URL=your-database-url
FLASK_ENV=development

🏃 Running the Server Locally

	1.	Start the Flask server:

python main.py


	2.	The backend server will be available at http://127.0.0.1:5000.
	3.	You can now interact with the following API endpoints:
	•	POST /insert
	•	GET /search

🌐 Deploying to Render

To deploy the Suggestify backend on Render:
	1.	Create a Render account: Sign up at Render.
	2.	Create a new Web Service:
	•	Connect your GitHub repository to Render.
	•	Select Python as the environment.
	•	Set the port to 5000 (default for Flask).
	•	Add necessary environment variables like DATABASE_URL and FLASK_ENV.
	3.	Deploy: Render will build and deploy your Flask application automatically.

🧪 Testing the API

Use Postman, cURL, or your frontend to test the API.

Example cURL Requests:

Insert Word:

curl -X POST https://suggestify-2.onrender.com/insert \
    -H "Content-Type: application/json" \
    -d '{"word": "example"}'

Search Prefix:

```
curl "https://suggestify-2.onrender.com/search?prefix=exa"

```
⚠️ Troubleshooting

	•	CORS Errors: If you’re running a frontend on a different domain, ensure CORS is properly configured. Flask-CORS is already included in the project.
	•	Environment Variables: Ensure all necessary environment variables are configured in both local and production environments.
	•	Missing Dependencies: Ensure your requirements.txt is up to date. If you encounter any issues, you can install any missing dependencies manually.
