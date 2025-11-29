from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    # RELACIONES
    favorite_people = relationship("FavoritePeople", back_populates="user")
    favorite_planets = relationship("FavoritePlanet", back_populates="user")
    favorite_vehicles = relationship("FavoriteVehicle", back_populates="user")
    favorite_starships = relationship("FavoriteStarship", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }
    

class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    gender: Mapped[str] = mapped_column(String(120), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(120), nullable=False)
    eye_color: Mapped[str] = mapped_column(String(120), nullable=False)
    skin_color: Mapped[str] = mapped_column(String(120), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(120), nullable=False)

    # RELACIÓN
    favorites = relationship("FavoritePeople", back_populates="people")

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
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    people_id: Mapped[int] = mapped_column(ForeignKey('people.id'))

    # RELACIONES
    user = relationship("User", back_populates="favorite_people")
    people = relationship("People", back_populates="favorites")


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    climate: Mapped[str] = mapped_column(String(120), nullable=False)
    gravity: Mapped[str] = mapped_column(String(120), nullable=False)
    population: Mapped[str] = mapped_column(String(120), nullable=False)
    terrain: Mapped[str] = mapped_column(String(120), nullable=False)
    orbital_period: Mapped[str] = mapped_column(String(120), nullable=False)

    favorites = relationship("FavoritePlanet", back_populates="planet")

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
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    planet_id: Mapped[int] = mapped_column(ForeignKey('planet.id'))

    user = relationship("User", back_populates="favorite_planets")
    planet = relationship("Planet", back_populates="favorites")


class Vehicle(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    passengers: Mapped[str] = mapped_column(String(120), nullable=False)
    manufacturer: Mapped[str] = mapped_column(String(120), nullable=False)
    model: Mapped[str] = mapped_column(String(120), nullable=False)
    crew: Mapped[str] = mapped_column(String(120), nullable=False)
    cost_in_credits: Mapped[str] = mapped_column(String(120), nullable=False)

    favorites = relationship("FavoriteVehicle", back_populates="vehicle")

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
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    vehicle_id: Mapped[int] = mapped_column(ForeignKey('vehicle.id'))

    user = relationship("User", back_populates="favorite_vehicles")
    vehicle = relationship("Vehicle", back_populates="favorites")


class Starship(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    passengers: Mapped[str] = mapped_column(String(120), nullable=False)
    manufacturer: Mapped[str] = mapped_column(String(120), nullable=False)
    model: Mapped[str] = mapped_column(String(120), nullable=False)
    crew: Mapped[str] = mapped_column(String(120), nullable=False)
    cost_in_credits: Mapped[str] = mapped_column(String(120), nullable=False)

    favorites = relationship("FavoriteStarship", back_populates="starship")

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


class FavoriteStarship(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    starship_id: Mapped[int] = mapped_column(ForeignKey('starship.id'))

    user = relationship("User", back_populates="favorite_starships")
    starship = relationship("Starship", back_populates="favorites")
