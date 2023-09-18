from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "book_name": "Book1", "author": "Author1", "publisher": "Publisher1"},
    {"id": 2, "book_name": "Book2", "author": "Author2", "publisher": "Publisher2"},
    {"id": 3, "book_name": "Book3", "author": "Author3", "publisher": "Publisher3"},
]

# Read all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Read single book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

# Create book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if data:
        new_book = {
            "id": len(books) + 1,
            "book_name": data["book_name"],
            "author": data["author"],
            "publisher": data["publisher"],
        }
        books.append(new_book)
        return jsonify(new_book), 201
    else:
        return jsonify({"message": "Invalid request"}), 400

# Update book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((b for b in books if b["id"] == book_id), None)
    if book and data:
        book["book_name"] = data.get("book_name", book["book_name"])
        book["author"] = data.get("author", book["author"])
        book["publisher"] = data.get("publisher", book["publisher"])
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

# Delete book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message": "Book deleted"})

if __name__ == '__main__':
    app.run(debug=True)
