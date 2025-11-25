from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    gender: Mapped[str] = mapped_column(String(120), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(120), nullable=False)
    eye_color: Mapped[str] = mapped_column(String(120), nullable=False)
    skin_color: Mapped[str] = mapped_column(String(120), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color,
            "birth_year": self.birth_year,
        }

class FavoritePeople(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey('user.id'), primary_key=True)
    people_id: Mapped[str] = mapped_column(ForeignKey('people.id'), primary_key=True)

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    climate: Mapped[str] = mapped_column(String(120), nullable=False)
    gravity: Mapped[str] = mapped_column(String(120), nullable=False)
    population: Mapped[str] = mapped_column(String(120), nullable=False)
    terrain: Mapped[str] = mapped_column(String(120), nullable=False)
    orbital_period: Mapped[str] = mapped_column(String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "gravity": self.gravity,
            "population": self.population,
            "terrain": self.terrain,
            "orbital_period": self.orbital_period,
        }

class FavoritePlanet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey('user.id'), primary_key=True)
    planet_id: Mapped[str] = mapped_column(ForeignKey('planet.id'), primary_key=True)

class Vehicle(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    passengers: Mapped[str] = mapped_column(String(120), nullable=False)
    manufacturer: Mapped[str] = mapped_column(String(120), nullable=False)
    model: Mapped[str] = mapped_column(String(120), nullable=False)
    crew: Mapped[str] = mapped_column(String(120), nullable=False)
    cost_in_credits: Mapped[str] = mapped_column(String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "passengers": self.passengers,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "crew": self.crew,
            "cost_in_credits": self.cost_in_credits,
        }

class FavoriteVehicle(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey('user.id'), primary_key=True)
    vehicle: Mapped[str] = mapped_column(ForeignKey('vehicle.id'), primary_key=True)

