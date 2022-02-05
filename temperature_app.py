from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
app.debug = True


@app.route('/')
def name():
    return jsonify({"firstname": "Burcu",
                    "lastname": "Koculu"
                    })

@app.route('/temperature', methods=['GET'])

def search_city():

    api_key = 'eed5959717c94775779be2803bbda0d1'  # initializing key
    city = request.args.get('city')  # city name passed as argument

    # call weather API and convert response into Python dictionary
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}'
    response = requests.get(url).json()

    # error like unknown city name, inavalid api key
    if response.get('cod') != 200:
        message = response.get('message', '')
        return f'Error getting temperature for {city.title()}. Error message = {message}'

    # get current temperature and convert it into Celsius
    current_temperature = response.get('main', {}).get('temp')
    if current_temperature:
        current_temperature_celsius = round(current_temperature - 273.15, 2)
        return jsonify({"temperature": current_temperature_celsius})
    else:
        return f'Error getting temperature for {city.title()}'


if __name__ == '__main__':
    app.run(debug=True, port=8080)