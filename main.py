from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Route for Home Page
@app.route('/')
def index():
    return render_template('index.html')


countries = [
    {'Id': 10, 'Name': 'Austria', 'Capital': 'Vienna', 'Population': '9M', 'Area': '83,879 km2', 'Dialing_code': '+43'},
    {'Id': 20, 'Name': 'Germany', 'Capital': 'Berlin', 'Population': '84M', 'Area': '357,592 km2',
     'Dialing code': '+49'},
    {'Id': 30, 'Name': 'France', 'Capital': 'Paris', 'Population': '67M', 'Area': '551,695 km2', 'Dialing_code': '+33'},
    {'Id': 40, 'Name': 'Italy', 'Capital': 'Rome', 'Population': '58M', 'Area': '301,230 km2', 'Dialing_code': '+39'},
    {'Id': 50, 'Name': 'Spain', 'Capital': 'Madrid', 'Population': '47M', 'Area': '505,990 km2', 'Dialing_code': '+34'},
    {'Id': 60, 'Name': 'England', 'capital': 'London', 'Population': '56M', 'Area': '130,279 km2',
     'Dialing_code': '+44'},
]


def search(ct_id, ls):
    result = [element for element in ls if element['Id'] == ct_id]
    if len(result) > 0:
        return result[0]
    return None


# Route to handle AJAX POST request
@app.route('/process_data', methods=['POST'])
def process_data():
    # Get JSON data from request
    data = request.get_json()

    country_id = data.get('countryId')
    country_detail = search(int(country_id), countries)
    print("Found country detail: ", country_detail)

    # Send a JSON response back to the client
    return jsonify({
        'status': 'success',
        'country_detail': country_detail
    })


if __name__ == '__main__':
    app.run(debug=True)
