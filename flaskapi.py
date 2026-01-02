from flask import Flask, jsonify, request

app = Flask(__name__)
books = [
    {"id": 0, "title": "A Fire Upon the Deep", "author": "Vernor Vinge"},
    {"id": 1, "title": "The Ones Who Walk Away From Omelas", "author": "Ursula K. Le Guin"}
]

def find_book(id):
    return next((book for book in books if book["id"] == id), None)

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = find_book(id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    return jsonify({"book": book})

@app.route('/books', methods=['POST'])
def create_book():
    new_book = {
        "id": len(books),
        "title": request.json["title"],
        "author": request.json["author"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = find_book(id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    book["title"] = request.json.get("title", book["title"])
    book["author"] = request.json.get("author", book["author"])
    return jsonify({"book": book})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book["id"] != id]
    return jsonify({"message": "Book deleted"})

if __name__ == "__main__":
    app.run(debug=True)
