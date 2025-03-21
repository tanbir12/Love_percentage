# for current datetime....
import datetime
time = datetime.datetime.now().strftime('%c')

import requests
# This Code is Published by Tanbir Pradhan. Don't use it in your project.
from random import randint
from flask import Flask , render_template , request , redirect ,url_for
from flask_pymongo import PyMongo

app = Flask(__name__)



#+++++++++++++++++++++++++++ CONFIGURE ++++++++++++++++++++++++++++++++++++++++++
app.config['MONGO_URI'] = 'mongodb+srv://pradhantanbir:Jv7Hq8bsX9MAwfw4@cluster0.m0d6k.mongodb.net/Lovator?retryWrites=true&w=majority'  
# Update with your MongoDB URI
mongo = PyMongo(app)


#++++++++++++++++++++++++++++ DATABASE AREA ++++++++++++++++++++++++++++++++++++++
# Remove the SQLAlchemy model and replace with a dictionary-based approach
# No explicit model class is needed for MongoDB

def get_locaction_ip():
    try:
        ip = request.headers.get('X-Forwarded-For').split(',')[0]
        if ip != '127.0.0.1':
            response = requests.get(f'https://ipinfo.io/{ip}/json')
            data = response.json()
            print(data)
        return f"IP: {ip}, data.get('city','unknown'),data.get('regionName'), data.get('country')"

    except :
        return "None"


#++++++++++++++++++++++++++++  Home Page Route  ++++++++++++++++++++++++++++++++

@app.route("/",methods = ['GET','POST'])
def GET_Value():

    loc = get_locaction_ip()
    referer = request.headers.get('Referer')
    if request.method == 'POST':
        Your_name = request.form.get("your_name")
        Crush_name = request.form.get("crush_name")
        
        if (str(Your_name)!="" and str(Crush_name)!=""):
            percent = randint(60,100)
            round_percent = (1-(percent/100))*440
            # Insert the data into MongoDB
            mongo.db.love_data.insert_one({
                'Your_name': Your_name,
                'Crush_name': Crush_name,
                'Date': time,
                'Percentage': percent,
                'UserData' : loc,
                'Referer' : referer
            })

            return render_template('love.html', percent = percent , round_percent = round_percent )


    return render_template('index.html')




#++++++++++++++++++++++++++++  Table Route  ++++++++++++++++++++++++++++++++
@app.route("/Table")
def Show_Models():

    filedb = mongo.db.love_data.find()
    filedb = list(filedb)
    filedb = filedb[::-1]  # Reverse the list for display

    return render_template("table.html", dbs = filedb)




if __name__=="__main__":
    app.run(debug=False, port=8000)
