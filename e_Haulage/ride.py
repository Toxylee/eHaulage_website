from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/new_order/<pick>/<dest>', strict_slashes=False)
def test_flask(pick, dest):
    """Post pick up address and destination address to a file"""

    """Create file storage called pickup_data.json"""
    filename = "Pickup_Data.json"

    """Create request using the url arguments passed from the client"""
    new_dict = {"pick_address": pick, "dest_address": dest}

    """If file exist and contains data, convert to obj, if not, create empty array"""
    file_storage = []
    try:
        with open(filename, 'r', encoding="utf-8") as fp:
            file_storage = json.load(fp)
    except FileNotFoundError:
        file_storage = []

    """Append customer info to the dictionary and write back to the file"""
    file_storage.append(new_dict)

    """Save customer info to the file storage"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(file_storage, f)

    return "From {} to {}".format(pick, dest)

if __name__ == "__main__":
    app.run()
