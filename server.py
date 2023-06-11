from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'happy'


# show route
@app.route('/')
def homes():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] +=1
    return render_template('index.html')

@app.route("/addTwo")
def addTwo():
    session['counter'] += 1
    return redirect('/')

# action route
# @app.route('/count', methods=['POST'])
# def count():
#     if request.form["change"]=="add":
#         session["counter"] += 1
#     elif request.form["change"]=="reset":
#         session["counter"] = 0

#     return redirect("/")

@app.route('/increment', methods = ['POST'])
def increment():
    session['counter'] += int(request.form['addMultiple'])
    session['counter'] -= 1
    return redirect('/')


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True, host = 'localhost', port = 5000)    # Run the app in debug mode.
