from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = 'info'

@app.route('/')
def index():
    return render_template("dojo_survey.html")

@app.route('/submited_info', methods=['POST'])
def newUser():
    print(request.form)
    session['forminfo'] = request.form
    return redirect('/showinfo')

@app.route('/showinfo')
def showinfo():
    print(session['forminfo'])
    return  render_template('submited_info.html', forminfo = session['forminfo'])

@app.errorhandler(404)
def not_found(e):
    return ('Error! Please Try Again')

if __name__=="__main__":
    app.run(debug=True)

