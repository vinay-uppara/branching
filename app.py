from flask import Flask, jsonify, request

app = Flask(__vinay uppara__)

# Home route
@app.route("/")
def home():
    return "Welcome to the Flask Application!"

# About route
@app.route("/about")
def about():
    return "This is a basic Flask application."

# API route that returns JSON
@app.route("/api/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")
    return jsonify({"message": f"Hello, {name}!"})

# Entry point
if __name__ == "__main__":
    app.run(debug=True)
