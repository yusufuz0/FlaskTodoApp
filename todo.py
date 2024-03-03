from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////Users/Huawei/OneDrive/Masaüstü/Projeler/Flask, ORM ve SqlAchemy ile Todo App/todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)


@app.route("/")
def index():
   
   data = Todo.query.all()
   return render_template("index.html", todos = data)


@app.route("/add", methods = ["POST"])
def add():
    title = request.form.get("title")
    newTodo = Todo(title = title, complete = False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/update/<string:id>")
def update(id):
    data = Todo.query.filter_by(id = id).first()
    data.complete = not data.complete
    db.session.commit()

    return redirect(url_for("index"))
    
@app.route("/delete/<string:id>")
def delete(id):
    data = Todo.query.filter_by(id = id).first()
    db.session.delete(data)
    db.session.commit()

    return redirect(url_for("index"))
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)






