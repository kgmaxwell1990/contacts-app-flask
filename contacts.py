from flask import Flask, request
from flask import render_template

app = Flask(__name__)

contacts={
    "Katie": {"name": "Katie", "email": "katie@gmail.com", "phone": "1234"},
    "Richard": {"name": "Richard", "email": "richard@gmail.com", "phone": "5678"},
    "Jessye": {"name": "Jessye", "email": "jessye@gmail.com", "phone": "910112"},
    }

@app.route("/")
def get_index():
    return render_template("index.html")

@app.route("/contacts")
def get_contacts():
    return render_template("contacts.html", contacts=contacts.values())
    
@app.route("/addcontact", methods=["POST"])
def add_contact():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    
    contacts[name] = {"name": name, "email": email, "phone": phone}
    
    return render_template("contacts.html", contacts=contacts.values())
    
@app.route("/deletecontact", methods=["POST"])
def delete_contact():
    name_to_delete = request.form.get("contact_to_delete")
    del(contacts[name_to_delete])
    return render_template("contacts.html", contacts=contacts.values())
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)