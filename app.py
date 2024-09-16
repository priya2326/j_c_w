from flask import Flask, render_template , jsonify

app = Flask(__name__)

Jobs= [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': ' RS.7000000 ' 
  },
  {
  'id': 2,
  'title': 'Machine Learning',
  'location': 'Bengaluru, India',
  'salary': ' Rs.13000000 ' 
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary ': ' Rs.1800000 ' 
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Dallas, US',
    'salary': ' $200k '
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html', 
                         jobs=Jobs ,
                        company_name='Jovian')
@app.route('/api/jobs')
def list_jobs():
  return jsonify(Jobs)
  
if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)
  