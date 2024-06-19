from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "motorcycles.db"

def create_connection(db_filename):
   try:
      connection = sqlite3.connect(db_filename)
      return connection
   except Error as e:
      print(e)
      return None



@app.route('/')
def render_home_page():  # put application's code here
   return render_template("index.html")


@app.route('/motorcycles.html')
def render_motorcycles():  # put application's code here

   query = "Select Model, Make, Price, Displacement, Power, ABS, Style From moto_table"
   connection = create_connection(DATABASE)
   cursor = connection.cursor()
   cursor.execute(query)

   data_list = cursor.fetchall()
   print(data_list)

   return render_template("motorcycles.html", data=data_list)

@app.route('/Sports.html')
def render_Sports():  # put application's code here

   query = "Select Model, Make, Price, Displacement, Power, ABS, Style From moto_table WHERE Style = 'Sport'"
   connection = create_connection(DATABASE)
   cursor = connection.cursor()
   cursor.execute(query)

   data_list = cursor.fetchall()
   print(data_list)

   return render_template("Sports.html", data=data_list)


if __name__ == '__main__':
   app.run()
