from flask import Flask,render_template,request,redirect
from datetime import datetime
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
db=SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    desc= db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.now)

    def __init__(self, title: str, desc: str):
        self.title = title
        self.desc = desc

    def __repr__(self)->str:
        return f"{self.id} - {self.title}"


with app.app_context():
    db.create_all()

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo = Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodos = Todo.query.all()
    return render_template('index.html',todos=allTodos)

@app.route('/delete/<int:id>')
def dltTodo(id):
    todo=Todo.query.get_or_404(id)

    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    todo= Todo.query.get_or_404(id)
    if request.method=='POST':
        todo.title=request.form['title']
        todo.desc=request.form['desc']
        db.session.commit()
        return redirect('/')
    return render_template("update.html",todo=todo)
@app.route('/show')
def products():
    todos = Todo.query.all()
    print(todos)
    return 'Products Page'

if(__name__ == '__main__'):
    app.run(debug=True)