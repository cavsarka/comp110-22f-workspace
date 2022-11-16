"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730615401"


class Point:  
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Finds the distance between two points."""
        side_x = self.x - other.x
        side_y = self.y - other.y
        distance = sqrt(side_x**2 + side_y**2)
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Update the state of the simulation with every tick."""
        self.location = self.location.add(self.direction)

    def contract_disease(self) -> None:
        """Assigns infection to cell."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Checks if a cell is vulnerable."""
        return self.sickness == constants.VULNERABLE
    
    def is_infected(self) -> bool:
        """Checks if a cell is infected."""
        return self.sickness >= constants.INFECTED
    
    def immunize(self) -> None:
        """Immunizes a cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> None:
        """Returns true if a given cell is immunized."""
        return self.sickness == constants.IMMUNE

    def color(self) -> str:
        """Changes color if a cell is infected."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "orange"

    def contact_with(self, other: Cell) -> None:
        """Finds if two cells are touching."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        elif self.is_vulnerable() and other.is_infected():
            self.contract_disease()


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, starting_infected: int, starting_immune: int = 1):
        """Initialize the cells with random locations and directions."""
        if starting_infected <= 0 or starting_infected >= cells:
            raise ValueError("You cannot have 0 cells starting infected.")
        if starting_immune <= 0 or starting_immune > cells:
            raise ValueError("You cannot have 0 cells starting infected.")
        self.population = []
        for num in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if num < starting_infected:
                cell.contract_disease()
            elif num >= starting_infected and num < starting_immune + starting_infected:
                cell.immunize()
            self.population.append(cell)
            
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population: 
            cell.tick()
            self.enforce_bounds(cell)
            if cell.is_infected():
                cell.sickness += 1
                if cell.sickness > constants.RECOVERY_PERIOD:
                    cell.immunize()
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X or cell.location.x < constants.MIN_X:
            cell.direction.x *= -1
        if cell.location.y > constants.MAX_Y or cell.location.y < constants.MIN_Y:
            cell.direction.y *= -1
        ...
    
    def check_contacts(self) -> None:
        """Check if two cells touch each other."""
        for cell in self.population:
            for other_cell in self.population[self.population.index(cell):]:
                if cell.location.distance(other_cell.location) < constants.CELL_RADIUS:
                    cell.contact_with(other_cell)

    def is_complete(self) -> bool:
        """Check if there are no more infected cells."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True