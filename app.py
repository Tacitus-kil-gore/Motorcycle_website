from flask import Flask, render_template


app = Flask(__name__)




@app.route('/')
def render_home_page():  # put application's code here
   return render_template("base.html")




if __name__ == '__main__':
   app.run()
