from flask import Flask, render_template
from reaction import get_reaction




app = Flask(__name__)

@app.route('/')
def index():
  
    prt = input('Enter Port Number: [COM1,COM2,COM3,COM4,COM5,COM6,COM7]: ')
    time = get_reaction(prt)
    return render_template('index.html',time = time)


if __name__ == "__main__":
    app.run(debug=True)

    