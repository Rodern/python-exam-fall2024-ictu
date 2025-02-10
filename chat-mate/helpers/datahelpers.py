import uuid
import os
import json
from flet import *

def read_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        return None

# Define the app storage directory and file path
app_storage_dir = os.path.join(os.getenv('APPDATA'), 'MyApp')
file_path = 'db/user_data.json' #os.path.join(app_storage_dir, 'user_data.json')

def GetLogin(page: Page):
    user_data = read_json(file_path)
    if user_data and 'userId' in user_data and user_data['userId']: 
        page.user_id = user_data['userId']
        page.user_logged_in = True
        page.update()
        return True
    else:
        page.user_logged_in = False
        page.update()
        return False

def SaveSignin(userId):
    # Define the JSON data
    data = {
        "userId": f"{userId}"
    }

    # Define the app storage directory (this example uses AppData for Windows)
    app_storage_dir = os.path.join(os.getenv('APPDATA'), 'stack')

    # Ensure the directory exists
    os.makedirs(app_storage_dir, exist_ok=True)

    # Define the path to the JSON file
    file_path = 'db/user_data.json' #os.path.join(app_storage_dir, 'user_data.json')

    # Write the JSON data to the file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)



def generateGuid():
    return str(uuid.uuid4())
