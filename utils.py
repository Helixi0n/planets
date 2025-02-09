import sqlite3

def get_planets():
    connection = sqlite3.connect('static/planets.db')
    query = connection.execute("SELECT name FROM planets")
    data = query.fetchall()
    data = [item[0] for item in data]
    return data

