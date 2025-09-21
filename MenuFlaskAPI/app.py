from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurant.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Chef(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    speciality = db.Column(db.String(80), nullable=False)

@app.route("/menu", methods=["GET"])
def get_menu():
    items = Menu.query.all()
    return jsonify([{"id": i.id, "name": i.name, "price": i.price} for i in items])


@app.route("/menu/<int:item_id>", methods=["GET"])
def get_menu_item(item_id):
    item = Menu.query.get(item_id)
    if not item:
        return {"error": "Not found"}, 404
    return {"id": item.id, "name": item.name, "price": item.price}


@app.route("/menu", methods=["POST"])
def create_menu_item():
    data = request.json
    item = Menu(name=data["name"], price=data["price"])
    db.session.add(item)
    db.session.commit()
    return {"message": "Menu item created", "id": item.id}, 201


@app.route("/menu/<int:item_id>", methods=["PUT"])
def update_menu_item(item_id):
    item = Menu.query.get(item_id)
    if not item:
        return {"error": "Not found"}, 404
    data = request.json
    item.name = data.get("name", item.name)
    item.price = data.get("price", item.price)
    db.session.commit()
    return {"message": "Menu item updated"}


@app.route("/menu/<int:item_id>", methods=["DELETE"])
def delete_menu_item(item_id):
    item = Menu.query.get(item_id)
    if not item:
        return {"error": "Not found"}, 404
    db.session.delete(item)
    db.session.commit()
    return {"message": "Menu item deleted"}


@app.route("/chefs", methods=["GET"])
def get_chefs():
    chefs = Chef.query.all()
    return jsonify([{"id": c.id, "name": c.name, "speciality": c.speciality} for c in chefs])


@app.route("/chefs/<int:chef_id>", methods=["GET"])
def get_chef(chef_id):
    chef = Chef.query.get(chef_id)
    if not chef:
        return {"error": "Not found"}, 404
    return {"id": chef.id, "name": chef.name, "speciality": chef.speciality}


@app.route("/chefs", methods=["POST"])
def create_chef():
    data = request.json
    chef = Chef(name=data["name"], speciality=data.get("speciality"))
    db.session.add(chef)
    db.session.commit()
    return {"message": "Chef created", "id": chef.id}, 201


@app.route("/chefs/<int:chef_id>", methods=["PUT"])
def update_chef(chef_id):
    chef = Chef.query.get(chef_id)
    if not chef:
        return {"error": "Not found"}, 404
    data = request.json
    chef.name = data.get("name", chef.name)
    chef.speciality = data.get("speciality", chef.speciality)
    db.session.commit()
    return {"message": "Chef updated"}


@app.route("/chefs/<int:chef_id>", methods=["DELETE"])
def delete_chef(chef_id):
    chef = Chef.query.get(chef_id)
    if not chef:
        return {"error": "Not found"}, 404
    db.session.delete(chef)
    db.session.commit()
    return {"message": "Chef deleted"}


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
