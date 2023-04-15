from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'domakisgay'

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)