from flask import Flask,render_template,url_for,request,redirect
from main2 import*
import warnings 
warnings.filterwarnings("ignore")
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

common1 = "\n"+"        Maintain Social Distancing and do wear a mask to prevent spreading of the virus."
common2 = "\n"+"        Call the Helpline Number :+91-11-23978046 for any help."

a1 = "You have a high risk of being infected. Please consult your nearest hospital. Don't worry because about 1 out of 5 cases will likely have serious illness. It's a mild infection for young ones. Maintain your cool and be confident."
a2 = "You have a high risk of being infected. Please consult your nearest hospital immedialtely and follow the protocol."

b1 = "Chances of virus residing in you is low but risk of exposure for one is high. We recommend you to self isolate yourself and take good care of your health. Try taking good food to boost your immunity."

c1 = "Chances of you being infected is very little. But take preventive measures as it's more likely for virus to attack on you when your immune system is down. Self-quarantine yourself."

d1 = "You have of low risk of being infected. So yay! for that and self quarantine yourself in your home."
@app.route('/test/#result')
def result(age,symps):
	if(age < 18):
		if (73 in symps) or (56 in symps) or (54 in symps):
			return print_result(a1+common2)
		elif (23 in symps) or (24 in symps) or (28 in symps):
			return print_result(b1+common1)
		elif len(symps) == 3:
			return print_result(b1+common1+common2)
		else:
			return print_result(c1+common1)



	else:
		if (93 in symps) or (71 in symps) or (80 in symps) or (43 in symps) or (61 in symps) or (58 in symps):
			return print_result(a2+common1+common2)
		elif (35 in symps) or (31 in symps):
			return print_result(b1+common1+common2)
		elif (16 in symps) and ((6.9 in symps) or (12 in symps)):
			return print_result(c1+common1)
		else:
			return print_result(d1+common1)

# print(assesment(14,[13,23]))

@app.route('/test/result')
def print_result(txt):
	return render_template('test.html',text=txt)

@app.route("/get")
def get_bot_response():
	msg = request.args.get('msg')
	reply = chat(msg)
	return reply

if __name__=="__main__":
	app.run(debug=True)
