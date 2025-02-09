from flask import Flask, url_for
from utils import get_planets

app = Flask(__name__)


@app.route("/") 
@app.route("/home")
def home_page():
    planets = get_planets()
    links_list = []
    for name in planets:
        links_list.append(
            f'<li class="list-group-item"><a href ="/planet/{name}" class="text-decoration-none">{name}</a></li>'
        )
        links_str = " ".join(links_list)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Планеты</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <div class="row mt-5"></div>
        <h1>Планеты солнечной системы</h1>
        <div class="row">
            <div class="col-md-4"></div>
            <ul class="list-group">
                {links_str}
            </ul>
        </div>
    </div>
</body>
</html>'''


@app.route("/planet/<planet_name>")
def planet_info(planet_name):
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
