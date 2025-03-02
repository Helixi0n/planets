from flask import Flask, url_for, request, render_template

from utils import get_planet_list_names, get_planet_info_by_name, add_planet

app = Flask(__name__)


@app.route("/")
def index():
    planets = get_planet_list_names()

    links_list = []
    for name in planets:
        links_list.append(
            f'<li class="list-group-item"><a href="/planet/{name}" class="text-decoration-none">{name}</a></li>'
        )
    add_link = f'<li class="list-group-item"><a href="/add" class="text-decoration-none">Добавить планету</a></li>'
    links_str = " ".join(links_list) + add_link

    return f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Планеты Солнечной системы</title>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
          <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
        </head>
        <body>
          <div class="container">
              <div class="row mt-5">
                <h1 class="text-center mt-5 mb-5">Планеты Солнечной системы</h1>
                <div class="row justify-content-center">
                  <div class="col-md-4">
                    <ul class="list-group">
                      {links_str}
                    </ul>
                  </div>
                </div>
            </div>
          </div>
        </body>
        </html>
    """


@app.route("/planet/<planet_name>")
def planet_info(planet_name):
    planet_info = get_planet_info_by_name(planet_name)

    name = planet_info[1]
    distance_from_sun = planet_info[2]
    diameter = planet_info[3]
    mass = planet_info[4]
    atmosphere_composition = planet_info[5]
    unique_features = planet_info[6]
    geological_activity = planet_info[7]
    satellites = planet_info[8]
    climate_and_weather = planet_info[9]

    return f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Информация о планете</title>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
          <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
        </head>
        <body>
          <div class="container">
            <div class="row mt-5">
              <div class="col-md-6 offset-md-3">
                <h1 class="text-center mt-5 mb-5">Информация о планете</h1>
                <div class="card">
                  <div class="card-body">
                    <h4 class="card-title"><b>Название планеты:</b> {name}</h4>
                    <p class="card-text"><b>Расстояние от Солнца:</b>  {distance_from_sun}</p>
                    <p class="card-text"><b>Диаметр:</b>  {diameter}</p>
                    <p class="card-text"><b>Масса:</b>  {mass}</p>
                    <p class="card-text"><b>Состав атмосферы:</b>  {atmosphere_composition}</p>
                    <p class="card-text"><b>Уникальные особенности:</b>  {unique_features}</p>
                    <p class="card-text"><b>Геологическая активность:</b>  {geological_activity}</p>
                    <p class="card-text"><b>Спутники:</b>  {satellites}</p>
                    <p class="card-text"><b>Климат и погода:</b>  {climate_and_weather}</p>
                    <a href="/" class="btn btn-light">Назад к списку планет</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </body>
        </html>
    """

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
      return render_template('add.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        distance_from_sun = request.form.get('distance_from_sun')
        diameter = request.form.get('diameter')
        mass = request.form.get('mass')
        atmosphere_composition = request.form.get('atmosphere_composition')
        unique_features = request.form.get('unique_features')
        geological_activity = request.form.get('geological_activity')
        satellites = request.form.get('satellites')
        climate_and_weather = request.form.get('climate_and_weather')
        add_planet([name, 
                    distance_from_sun, 
                    diameter, 
                    mass, 
                    atmosphere_composition, 
                    unique_features, 
                    geological_activity, 
                    satellites, 
                    climate_and_weather])
        return render_template('add2.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
