from flask import Flask, render_template


app = Flask(__name__)




@app.route('/')
def render_home_page():  # put application's code here
   return render_template("base.html")


@app.route('/motorcycles.html')
def render_motorcycles():  # put application's code here
   return render_template("motorcycles.html")

@app.route('/Sigma.html')
def render_sigma():  # put application's code here
   return render_template("Sigma.html")




if __name__ == '__main__':
   app.run()
