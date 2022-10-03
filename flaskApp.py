from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [
    {
        "id":1,
        "name":"",
        "contact":0,
        "done":""

    }
]

@app.route("/add_data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data",

        }, 400)
    
    contact = {
        "id": tasks[-1]["id"]+1,
        "name": request.json["Name"],
        "contact": request.json["Contact", ""],
        "done": False
    }

    contact.append(contact)
    return jsonify({
        "status":"success",
        "message":"Contact added successfully"
    })

@app.route("/get_data")
def getTask():
    return jsonify({
        "data": tasks
    })

if(__name__ == '__main__'):
    app.run(debug = True)