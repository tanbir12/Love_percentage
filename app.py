# for current datetime....
import datetime
time = datetime.datetime.now().strftime('%c')



# This Code is Published by Tanbir Pradhan. Don't use it in your project.
from random import randint
from flask import Flask , render_template , request , redirect ,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,migrate
app = Flask(__name__)



#+++++++++++++++++++++++++++ CONFIGURE ++++++++++++++++++++++++++++++++++++++++++
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lovepercentage.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#++++++++++++++++++++++++++++ DATABASE AREA ++++++++++++++++++++++++++++++++++++++
db = SQLAlchemy(app)

class filedbs(db.Model):
   id = db.Column('file_id', db.Integer, primary_key = True)
   Date = db.Column(db.String(10))
   Your_name = db.Column(db.String(40))
   Crush_name = db.Column(db.String(40))
   Percentage = db.Column(db.Integer)
   
   
   def __init__(self,Your_name,Crush_name,Date,Percentage):
       self.Your_name = Your_name
       self.Crush_name = Crush_name
       self.Date = Date 
       self.Percentage = Percentage  


#++++++++++++++++++++++++++++++    For Creating The Database db  ++++++++++++++++++++++++++++++++++
# with app.app_context():
#         db.create_all()


migrate = Migrate(app,db)


#++++++++++++++++++++++++++++  Home Page Route  ++++++++++++++++++++++++++++++++

@app.route("/",methods = ['GET','POST'])
def GET_Value():

    if request.method == 'POST':
        Your_name = request.form.get("your_name")
        Crush_name = request.form.get("crush_name")
        
        if (str(Your_name)!="" and str(Crush_name)!=""):
            percent = randint(90,100)
            filedb = filedbs(Your_name,Crush_name,time,percent)
            db.session.add(filedb)
            db.session.commit()
            return render_template('love.html', percent = percent )


    return render_template('index.html')




#++++++++++++++++++++++++++++  Table Route  ++++++++++++++++++++++++++++++++
@app.route("/Table")
def Show_Models():

    filedb = filedbs.query.all()
    filedb = list(filedb)
    filedb = filedb[::-1]
    return render_template("table.html", dbs = filedb)




if __name__=="__main__":
    app.run(debug=True, port=8000)


