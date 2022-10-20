# 2) Create a Module in VS Code and Import It into jupyter notebook
# Module should have the following capabilities:

# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area

def house_area(length, width):
    """given a length and a width, calculates the area in square feet."""
    return "The area of the house is " + str(int(length) * int(width)) + " square feet."

# 2) Has a function to calculate the circumference of a circle

def circumference(radius):
    """given a radius, calculates and returns the circumference of a circle."""
    return 2 * 3.14159 * radius


# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage