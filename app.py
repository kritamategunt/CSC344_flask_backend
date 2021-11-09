from flask import Flask, render_template, url_for, jsonify, request

app = Flask(__name__)

post = [
    {
        'author': 'Kritamate Kamheang',
        'title': 'post 1',
        'content': 'First test',
        'date' : 'jun 4,2021'
    },
    {
        'author': 'Matetaki gnaehmak',
        'title': 'post 2',
        'content': 'second test',
        'date' : 'april 6,2021'
    },
]


@app.route("/")

@app.route("/home")
def home():
    return render_template('homepage.html',posts = post,)

@app.route("/about")
def about():
    return render_template('about.html',title = 'About' )
 
@app.route('/test', methods = ['GET','POST'])
def test():
    if request.method == 'GET':
        return jsonify({'res':'200 Ok ><'})
    elif request.method == 'POST':
        req_Json = request.json
        input = req_Json['name']
        return jsonify({'res': 'Hi, ' + input})
        


if __name__ == '__main__':
    app.run(debug=True)
