import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''



@app.route('/api/v1/addnum', methods=['GET'])
def api_id():
       	i = request.args['n1']
       	j = request.args['n2']
       	k=int(i)+int(j)
       	k1=str(k)
       	return k1

app.run()
#http://127.0.0.1:5000/api/v1/addnum?n1=5&n2=6
#command to run : python add.py
# prereq: flask and virtual env should be inslated

