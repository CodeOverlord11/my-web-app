from flask import Flask,render_template
app=Flask()

@app.route("/")
def display_index():
    return render_template('index.html')