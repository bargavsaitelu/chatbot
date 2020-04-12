from flask import Flask,render_template,url_for,request,redirect

app = Flask(__name__)

@app.route('/<name>')
def success(name):
	return render_template('main.html',name=name)

@app.route('/',methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		user = request.form['name']
		return redirect(url_for('success',name=user))
	else:
		return render_template('bootstrap.html')

@app.route('/test',methods=['POST','GET'])
def test():
	if request.method == 'POST':
		symps=[]
		if request.form.get('a'):
			age=17
			if request.form.get('b'):
				symps.append(73)
			if request.form.get('c'):
				symps.append(56)
			if request.form.get('d'):
				symps.append(54)
			if request.form.get('e'):
				symps.append(13)
			if request.form.get('f'):
				symps.append(23)
			if request.form.get('g'):
				symps.append(7.2)
			if request.form.get('h'):
				symps.append(24)
			if request.form.get('i'):
				symps.append(28)
			if request.form.get('j'):
				symps.append(11)
			if request.form.get('k'):
				symps.append(5.8)
			if request.form.get('l'):
				symps.append(13)
			return result(age,symps)
		else:
			age=19
			if request.form.get('b'):
				symps.append(93)
			if request.form.get('c'):
				symps.append(71)
			if request.form.get('d'):
				symps.append(80)
			if request.form.get('e'):
				symps.append(43)
			if request.form.get('f'):
				symps.append(61)
			if request.form.get('g'):
				symps.append(6.9)
			if request.form.get('h'):
				symps.append(35)
			if request.form.get('i'):
				symps.append(58)
			if request.form.get('j'):
				symps.append(16)
			if request.form.get('k'):
				symps.append(12)
			if request.form.get('l'):
				symps.append(31)
			return result(age,symps)
	else:
		return render_template('test.html')


lp = [73,56,54,13,23,7.2,24,28,11,5.8,13]
la = [93,71,80,43,61,6.9,35,58,16,12,31]

a1 = "The chances of having the pandemic is high and I prefer you must consult a doctor"
a2 = " and make sure that you maintain a safe distance from others."

b1 = "The chances of having the pandemic is not so high,so I prefer you to be in home"
b2 = " quarantine for 14 days and if it gets worse in middle,you better consult a doctor."

c1 = "The chances of having the pandemic are low, so take rest for some days and if it"
c2 = " still persists, consult a doctor."

d1 = "The chances of having the pandemic are little, you can take rest for some days"
d2 = " and if it still persists take necessary precautions and diet."

common1 = "\n"+"        PLEASE MAINTAIN SOCIAL DISTANCING AND WEAR A MASK"
common2 = "\n"+"        PLEASE MAINTAIN SOCIAL DISTANCING"

a = a1+a2+common1
b = b1+b2+common1
c = c1+c2+common2
d = d1+d2+common2

@app.route('/test/result')
def result(age,symps):
	if(age < 18):
		if (73 in symps) or (56 in symps) or (54 in symps):
			return print_result(a)
		elif (23 in symps) or (24 in symps) or (28 in symps):
			return print_result(b)
		elif len(symps) == 3:
			return print_result(b)
		else:
			return print_result(c)



	else:
		if (93 in symps) or (71 in symps) or (80 in symps) or (43 in symps) or (61 in symps) or (58 in symps):
			return print_result(a)
		elif (35 in symps) or (31 in symps):
			return print_result(b)
		elif (16 in symps) and ((6.9 in symps) or (12 in symps)):
			return print_result(c)
		else:
			return print_result(d)

# print(assesment(14,[13,23]))

@app.route('/test/result')
def print_result(txt):
	return render_template('test.html',text=txt)

if __name__=="__main__":
	app.run(debug=True)
