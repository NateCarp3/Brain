import os
from flask import Flask
from dotenv import load_dotenv

# Load variables from a local .env file if one exists (for local development).
# In production, set these as real environment variables on the host instead.
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")