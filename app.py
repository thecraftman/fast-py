from flask import Flask, request, jsonify
from opentelemetry.instrumentation.flask import FlaskInstrumentor
import psycopg2
import exporter  # Importing the OpenTelemetry configuration

app = Flask(__name__)

# Instrument the Flask app with OpenTelemetry
FlaskInstrumentor().instrument_app(app)

# Use the tracer from the OpenTelemetry configuration
tracer = exporter.service1_tracer

# Database connection setup
DATABASE_URL = "postgres://trace:traces@localhost/blog"
conn = psycopg2.connect(DATABASE_URL)

@app.route("/create_post", methods=['POST'])
def create_post():
    title = request.json.get('title')
    content = request.json.get('content')
    with tracer.start_as_current_span("create_post_span"):
        try:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO blog_posts (title, content) VALUES (%s, %s)", (title, content))
                conn.commit()
        except Exception as e:
            conn.rollback()  # Rollback the transaction on error
            return jsonify({"error": str(e)}), 500
        return jsonify({"message": "Post created successfully"}), 201

@app.route("/get_posts", methods=['GET'])
def get_posts():
    with tracer.start_as_current_span("get_posts_span"):
        with conn.cursor() as cur:
            cur.execute("SELECT title, content FROM blog_posts")
            posts = cur.fetchall()
        return jsonify(posts)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
