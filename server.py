from flask import Flask,render_template,request,Response,jsonify
from flask_cors import CORS
import re
import shop

app = Flask(__name__)
CORS(app)

@app.route('/')
def getClothes():
    return jsonify(shop.clothesCollection)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post ' + str(post_id)

@app.route('/hello/<name>')
def hello(name=None):
    namearray = re.split(' +',name)
    firstname = namearray[0]
    lastname = namearray[1]
    return render_template('hello.html', firstname=firstname,lastname=lastname)

@app.route('/events', methods=['POST'])
def events():
    event_data = request.get_json()
    clothType = event_data['clothType']
    sliderValue = event_data['sliderValue']
    results = shop.clothesCollection[clothType]
    filteredResults = list(filter(lambda record: record["price"]<=int(sliderValue),results))
    return jsonify(filteredResults)


