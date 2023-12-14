# Import necessary libraries
from flask import Flask, render_template, request, jsonify

# Create a Flask application
app = flask(__name__)

# Sample data for museum exhibits (you would typically use a database)
exhibits = [
    {
        "id": 1,
        "name": "Ancient Artifacts",
        "description": "Explore ancient artifacts from around the world.",
        "artifacts": [
            {"id": 101, "name": "Egyptian Mummy", "description": "A well-preserved mummy."},
            {"id": 102, "name": "Roman Statue", "description": "A marble statue from ancient Rome."},
        ],
    },
    {
        "id": 2,
        "name": "Modern Art",
        "description": "Experience contemporary art pieces.",
        "artifacts": [
            {"id": 201, "name": "Abstract Painting", "description": "A vibrant abstract painting."},
            {"id": 202, "name": "Sculpture", "description": "A modern sculpture made of metal."},
        ],
    },
]

# Define routes and views
@app.route("/")
def index():
    return render_template("index.html", exhibits=exhibits)

@app.route("/exhibit/<int:exhibit_id>")
def exhibit(exhibit_id):
    for exhibit in exhibits:
        if exhibit["id"] == exhibit_id:
            return render_template("exhibit.html", exhibit=exhibit)
    return "Exhibit not found", 404

# API endpoint to retrieve artifact details
@app.route("/api/artifact/<int:artifact_id>")
def get_artifact(artifact_id):
    for exhibit in exhibits:
        for artifact in exhibit["artifacts"]:
            if artifact["id"] == artifact_id:
                return jsonify(artifact)
    return "Artifact not found", 404

if __name__ == "__main__":
    app.run(debug=True)
