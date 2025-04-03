from helper.HttpHandler import run
from controller.UserController import UserController
from controller.AutoController import AutoController

# Start the server
if __name__ == '__main__':
    run(port=8001)