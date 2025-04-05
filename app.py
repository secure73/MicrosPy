from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from helper.HttpHandler import run
import controller.UserController
import controller.AutoController

# Start the server
if __name__ == '__main__':
    run(port=8001)