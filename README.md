HTTP requests (GET, POST, PUT, DELETE) using curl with the same endpoint:

1. GET Request
To retrieve all books:
curl -X GET http://127.0.0.1:5000/books


To retrieve a specific book by ID (e.g., id=3):
curl -X GET http://127.0.0.1:5000/books/3


2. POST Request
To add a new book:
curl -X POST -H "Content-Type: application/json" -d "{\"id\": 3, \"title\": \"Brave New World\", \"author\": \"Aldous Huxley\"}" http://127.0.0.1:5000/books
3. PUT Request
To update an existing book (e.g., update the book with id=3):
curl -X PUT -H "Content-Type: application/json" -d "{\"title\": \"Brave New World\", \"author\": \"Aldous Huxley\"}" http://127.0.0.1:5000/books/3
4. DELETE Request
To delete a specific book by ID (e.g., id=3):
curl -X DELETE http://127.0.0.1:5000/books/3


Summary of Commands
GET: Retrieve data.
All books: curl -X GET http://127.0.0.1:5000/books
Specific book: curl -X GET http://127.0.0.1:5000/books/3

POST: Create new data.
Add a new book: curl -X POST -H "Content-Type: application/json" -d "{\"id\": 3, \"title\": \"Brave New World\", \"author\": \"Aldous Huxley\"}" http://127.0.0.1:5000/books

PUT: Update existing data.
Update a book: curl -X PUT -H "Content-Type: application/json" -d "{\"title\": \"Brave New World\", \"author\": \"Aldous Huxley\"}" http://127.0.0.1:5000/books/3

DELETE: Remove data.
Delete a book: curl -X DELETE http://127.0.0.1:5000/books/3
