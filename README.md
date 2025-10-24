# Flask REST API – Task 4

A simple Flask-based REST API for managing user data with full CRUD functionality.

## Setup
```bash
pip install -r requirements.txt
python app.py
pip install flask


## Endpoints
Method	Endpoint	Description
GET	/users	Get all users
GET	/users/<id>	Get user by ID
POST	/users	Add a new user
PUT	/users/<id>	Update user by ID
DELETE	/users/<id>	Delete user by ID


## issues faced 
Data resets on server restart

Tested using Postman

Includes error handling for missing fields and unknown IDs
