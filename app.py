from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

# Route to get all books

@app.route('/')
def home():
    return """Welcome to the book store
    <br>
    <a href="/books">Books</a>
    """
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route to get a book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    return jsonify(book)

# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

# Route to update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'message': 'Book not found'}), 404
    data = request.get_json()
    book.update(data)
    return jsonify(book)

# Route to delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
