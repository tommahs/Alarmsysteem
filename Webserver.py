from flask import Flask, render_template, request, url_for
import csv, os
app = Flask(__name__)

####
# Index file with buttons
# Button1 points to /codeform
# Button2 points to /blinkform
##
@app.route('/')
def index():
	return render_template('index.html')

####
# HBlinkspeed 
##

####
# HTMl page to input new code with Submit button
##
@app.route('/codeform', methods=['GET', 'POST'])
def codeform():
#	if request.method == 'GET':
#		print(request.form['name'])
	return render_template('codeform.html')
#####
# Submit button to change the security code
##
@app.route('/submitcode', methods=['GET', 'POST'])
def submitcode():
	error = None
	if request.method == 'POST':
		file = 'pincode.csv'
		newcode = [request.form['name']]
		with open(file, 'w') as codefile:
			writer = csv.writer(codefile)
			writer.writerow(newcode)
		codefile.close()
		return render_template('index.html')
	else:
		error = 'Name not found'
	return render_template('index.html', error=error)

####
# HTMl page to change the time before the alarm becomes active, using Submitbutton
##
@app.route('/blinkingformred', methods=['GET', 'POST'])
def blinkingformred():
        return render_template('blinkingformred.html')
#####
# Submit button to change the security code
##
@app.route('/submitblinkred', methods=['GET', 'POST'])
def submitblinkred():
        error = None
        if request.method == 'POST':
                file = 'blink2.csv'
                newcode = [request.form['name']]
                with open(file, 'w') as codefile:
                        writer = csv.writer(codefile)
                        writer.writerow(newcode)
                codefile.close()
        else:
                error = 'Name not found'
        return render_template('index.html', error=error)

@app.route('/blinkingformgreen', methods=['GET', 'POST'])
def blinkingformgreen():
        return render_template('blinkingformgreen.html')

@app.route('/submitblinkgreen', methods=['GET', 'POST'])
def submitblinkgreen():
        error = None
        if request.method == 'POST':
                file = 'blink.csv'
                newcode = [request.form['name']]
                with open(file, 'w') as codefile:
                        writer = csv.writer(codefile)
                        writer.writerow(newcode)
                codefile.close()
        else:
                error = 'Name not found'
        return render_template('index.html', error=error)

@app.route('/reset', methods=['GET','POST'])
def reset():
	import reboot, subprocess
	subprocess.call(['reboot'])
	return 'test'
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
