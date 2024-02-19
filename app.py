from flask import Flask,render_template,jsonify    
#print(__name__)
app = Flask(__name__)
JOB=[
  {
  'id':1,
  'title':'Data Analysist',
  'location':'Algiers, Algeria',
  'salary':'Rs. 10,00,000'
  },
  {
    'id':2,
    'title':'devlopper',
    'location':'la, usa',
    'salary':'Rs. 20,00,00'
    },
    {
    'id':2,
    'title':'designer',
    'location':'paris, France'
    }
]
@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOB)
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOB)
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)