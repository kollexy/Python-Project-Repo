from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (in-memory database)
movies = []


# Create a movie
@app.route('/movies', methods=['POST'])
def create_movie():
    data = request.get_json()
    movies.append(data)
    return jsonify(data), 201


# Read all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)


# Read a specific movie
@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = next((movie for movie in movies if movie.get('id') == movie_id), None)
    if movie:
        return jsonify(movie)
    return jsonify({'message': 'Movie not found'}), 404


# Update a movie
@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    data = request.get_json()
    movie = next((movie for movie in movies if movie.get('id') == movie_id), None)
    if movie:
        movie.update(data)
        return jsonify(movie)
    return jsonify({'message': 'Movie not found'}), 404


# Delete a movie
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    global movies
    movies = [movie for movie in movies if movie.get('id') != movie_id]
    return jsonify({'message': 'Movie deleted'})


if __name__ == '__main__':
    app.run(debug=True)
