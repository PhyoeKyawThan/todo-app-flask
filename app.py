from flask import Flask, request, render_template, redirect, url_for
from db import db

app = Flask(__name__)
app.secret_key = 'domakisgay'

db = db.DB()

@app.route('/',)
def index():
   datas = db.todo_lists()
   id = 0
   return render_template('index.html', lists=datas, id=id) 

@app.route('/add_todo',  methods=['POST', 'GET'])
def add_todo():
    if request.method == 'POST':
        title = request.form['title']
        todos = request.form['todos']
        data = [{'title': title, 'todo': todos}]
        db.insert(data)
        return redirect(url_for('index'))
    
@app.route('/delete/<id>')
def delete(id):
    db.delete(id)
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    title = request.form['update_title']
    todo  = request.form['update_todo']
    for data in db.todo_lists():
        if title != data[1]:
            db.update(data[0], 'title', title)
        
        if todo != data[2]:
            db.update(data[0], 'todo', todo)

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)