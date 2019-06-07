from flask import Flask, request
# from Entities.person import Person
import json

app = Flask(__name__)

@app.route("/property", methods=['GET'])
def PropertyGet():
    return "Hello Property"

@app.route("/zone", methods=['GET'])
def ZoneGet():
    return "Hello Zone!"

@app.route("/room", methods=['GET'])
def roomGet():
    return "Hello Room!"

# @app.route("/person", methods=['GET'])
# def personGet():
#     x = Person()
#     return x.get()

# @app.route("/person", methods=['POST'])
# def personCreate():
#     x = Person()
#     x.name = request.json['name']
#     x.save()
#     test = json.dumps(request.json, indent=4, sort_keys=True)
#     print(test)
#     return x.name

@app.route("/project", methods=['GET'])
def projectGet():
    return "Hello Project!"


if __name__ == "__main__":
    app.run()