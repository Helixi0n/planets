import sqlite3

def get_planets():
    connection = sqlite3.connect('static/planets.db')
    query = connection.execute("SELECT name FROM planets")
    data = query.fetchall()
    data = [item[0] for item in data]
    return data

def get_planet_info_by_name(name):
    connection = sqlite3.connect('static/planets.db')
    query = connection.execute("SELECT * FROM planets WHERE name = {name}")
    data = query.fetchall()
    return data