from flask import Flask,render_template,url_for,request,redirect

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
	return render_template('main.html')

@app.route('/',methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		user = request.form['name']
		return redirect(url_for('success',name=user))
	else:
		# user = request.args.get('name')
		return render_template('bootstrap.html')

if __name__=="__main__":
	app.run(debug=True)
