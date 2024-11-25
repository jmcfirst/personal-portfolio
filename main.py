from app import app
import os

if __name__ == "__main__":
    # Use port 80 in production, 5000 in development
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
