import threading
import subprocess
import os
from fastapi_app import app as fastapi_app
import uvicorn
import app  # Your Flask app

def run_flask():
    os.environ["FLASK_APP"] = "app"
    os.environ["FLASK_ENV"] = "development"
    subprocess.run(["flask", "run", "--port", "5000"])

def run_fastapi():
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000, log_level="info")

def main():
    # Start Flask app
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Start FastAPI app
    fastapi_thread = threading.Thread(target=run_fastapi)
    fastapi_thread.start()

    flask_thread.join()
    fastapi_thread.join()

    # Here you can also add code to interact with BentoML, boto3, and requests

if __name__ == "__main__":
    main()
