from flask import Flask,render_template,request,Response,jsonify
import re
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

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
    print('json data',event_data['name'])
    return jsonify(event_data)