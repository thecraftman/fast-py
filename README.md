# Send Traces using Python from FastAPI, Requests, Otel Exporter

This project demonstrates how to send traces from FastAPI, Requests, and an exporter using Python. It integrates a Flask application with a PostgreSQL database, using OpenTelemetry for trace data export.


## Prerequisites

Before you get started, ensure you have the following:
- Python `3.x` installed on your local machine. 
- A dataset and API token for trace data export. You will need to add these to the `exporter.py` file.
- PostgreSQL installed and running locally.




## Installation

Clone the Repository:

```
git clone https://github.com/thecraftman/fast-py.git
cd fast-py
```

Install Dependencies:

Install the required Python packages using the following command:

```
pip install -r requirements.txt
```

## Configuration

- In the `exporter.py` file, replace the placeholder values for `SERVICE_NAME`, `Authorization token`, and the `X-Axiom-Dataset` with your actual service name, API token, and dataset.
- Modify the `DATABASE_URL` in `app.py` to match your local PostgreSQL credentials.

## Running the Application

To run the application, execute the following command:

```
python main.py
```

## Using the Application

Access the Application:

- Use the following `curl` command to create a post:

```
curl -X POST http://127.0.0.1:5000/create_post \
     -H "Content-Type: application/json" \
     -d '{"title": "Sample Post", "content": "This is a test post."}'
```

- Access `http://127.0.0.1:5000/get_posts` to view blog posts.

You can change the ports in the `main.py` to the ports you want

View Traces: 
- Traces will start showing up in your configured dataset.


## Ports

- Flask App (http://127.0.0.1:5000/): This is your Flask application running on the default localhost address (127.0.0.1) on port 5000. Flask is being run in a separate thread within your main.py. `http://127.0.0.1:5000/get_posts`

- FastAPI App (http://0.0.0.0:8000): This is your FastAPI application, which is being served by Uvicorn. It's running on all available IP addresses (0.0.0.0) on port 8000. Uvicorn is also being run in a separate thread within main.py. `http://0.0.0.0:8000/`

## Modifying the Code

The code is structured as follows: 

- `app.py`: Contains the Flask application with `create_post` and `get_posts` functions for blog post interactions.
- `exporter.py`: Configures OpenTelemetry tracing, including the trace exporter.
- `fastapi_app.py`: Contains the FastAPI application.
- `main.py`: Entry point to run both Flask and FastAPI applications.

## Major Files Description

- `app.py`: Uses a blog post model with get_posts, and create_post functions. It is connected to a local PostgreSQL database for data persistence.
- `exporter.py`: Sets up the OpenTelemetry tracing configuration, important for exporting trace data.
- `fastapi_app.py`: Defines the FastAPI application with its own set of endpoints.
- `main.py`: Orchestrates the running of both Flask and FastAPI applications.



## License

MIT LICENSE
