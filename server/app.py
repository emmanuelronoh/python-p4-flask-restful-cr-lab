#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Plants(Resource):
    def get(self):
        """Retrieve a list of all plants."""
        plants = Plant.query.all()
        return jsonify([plant.to_dict() for plant in plants])  # Ensure this is a list of dicts

    def post(self):
        """Create a new plant."""
        data = request.get_json()
        new_plant = Plant(name=data['name'], image=data['image'], price=data['price'])
        db.session.add(new_plant)
        db.session.commit()
        return jsonify(new_plant.to_dict()), 201

class PlantByID(Resource):
    def get(self, id):
        """Retrieve a plant by its ID."""
        plant = Plant.query.get_or_404(id)  # This will automatically return a 404 if not found
        return jsonify(plant.to_dict())  # Ensure this returns the plant as a dict

api.add_resource(Plants, '/plants')
api.add_resource(PlantByID, '/plants/<int:id>')

@app.before_first_request
def create_tables():
    """Create database tables if they don't exist."""
    db.create_all()

if __name__ == '__main__':
    app.run(port=5555, debug=True)
