from forms import UserInfoForm
from flask import Flask, render_template, flash, request,url_for,redirect
import algo
app=Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '945a61eeffcee883e3b261a47b31ae47'

@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
	form=UserInfoForm()
	if form.validate_on_submit():
		if request.method=='POST':
			name=request.form['name']
			weight=float(request.form['weight'])
			height=float(request.form['height'])
			age=int(request.form['age'])
			gender=request.form['gender']
			phys_act=request.form['physical_activity']

			tdee=algo.calc_tdee(name,weight,height,age,gender,phys_act)
			return redirect(url_for('result',tdee=tdee))

	return render_template('home.html',title="Diet App",form=form)

@app.route('/result',methods=['GET','POST'])
def result():
	tdee=request.args.get('tdee')
	if tdee is None:
		return render_template('error.html',title="Error Page")
	
	tdee=float(tdee)
	breakfast= algo.bfcalc(tdee)
	snack1=algo.s1calc(tdee)
	lunch=algo.lcalc(tdee)
	snack2=algo.s2calc(tdee)
	dinner=algo.dcalc(tdee)
	snack3=algo.s3calc(tdee)
	return render_template('result.html',title="Result",breakfast=breakfast,snack1=snack1,lunch=lunch,snack2=snack2,dinner=dinner,snack3=snack3)

if __name__ == '__main__':
    app.run(debug=True)
