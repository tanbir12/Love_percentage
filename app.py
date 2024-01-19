
# This Code is Published by Tanbir Pradhan. Don't use it in your project.
from random import randint
from flask import Flask , render_template , request , redirect ,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



#+++++++++++++++++++++++++++ CONFIGURE ++++++++++++++++++++++++++++++++++++++++++
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lovepercentage.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#++++++++++++++++++++++++++++ DATABASE AREA ++++++++++++++++++++++++++++++++++++++
db = SQLAlchemy(app)

class filedbs(db.Model):
   id = db.Column('file_id', db.Integer, primary_key = True)
   Your_name = db.Column(db.String(40))
   Crush_name = db.Column(db.String(40))
   
   
   def __init__(self,Your_name,Crush_name):
       self.Your_name = Your_name
       self.Crush_name = Crush_name   


#++++++++++++++++++++++++++++++    For Creating The Database db  ++++++++++++++++++++++++++++++++++
# with app.app_context():
#         db.create_all()



#++++++++++++++++++++++++++++  Home Page Route  ++++++++++++++++++++++++++++++++

@app.route("/",methods = ['GET','POST'])
def GET_Value():

    if request.method == 'POST':
        Your_name = request.form.get("your_name")
        Crush_name = request.form.get("crush_name")

        if (str(Your_name)!="" and str(Crush_name)!=""):
            filedb = filedbs(Your_name,Crush_name)
            db.session.add(filedb)
            db.session.commit()
            percent = randint(90,100)
            return render_template('love.html', percent = percent )


    return render_template('love2.html')



if __name__=="__main__":
    app.run(debug=True, port=8000)


