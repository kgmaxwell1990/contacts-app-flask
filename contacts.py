from flask import Flask, request
from flask import render_template
import json

app = Flask(__name__)

contacts={
    1: {"id": 1, "name": "Katie", "email": "katie@gmail.com", "phone": "1234"},
    2: {"id": 2, "name": "Richard", "email": "richard@gmail.com", "phone": "5678"},
    3: {"id": 3, "name": "Jessye", "email": "jessye@gmail.com", "phone": "910112"},
    }
    
next_id = 4

@app.route("/")
def get_index():
    return render_template("index.html")

@app.route("/contacts")
def get_contacts():
    return render_template("contacts.html", contacts=contacts.values())
    
@app.route("/addcontact", methods=["POST"])
def add_contact():
    global next_id
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    contacts[next_id] = {"id": next_id, "name": name, "email": email, "phone": phone}
    next_id += 1
    return render_template("contacts.html", contacts=contacts.values())
    
@app.route("/deletecontact", methods=["POST"])
def delete_contact():
    id_to_delete = int(request.form.get("id_to_delete"))
    print(id_to_delete)
    del(contacts[id_to_delete])
    return render_template("contacts.html", contacts=contacts.values())
    
@app.route("/api/contacts")
def all_contacts_json():
    return json.dumps(contacts)

@app.route("/api/contacts/<int:id>")
def a_contact_json(id):
    return json.dumps(contacts[id])
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)