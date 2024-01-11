from flask import Flask, render_template, request
from reaction import get_reaction
import plotly.express as px

app = Flask(__name__)

time_lst = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prt = request.form['port']
        time_value = get_reaction(prt)
        
        time_lst.append(time_value)
        
        return render_template('index.html', time=time_value, reaction_times_list=time_lst, plot=None)

    return render_template('index.html', time=None, reaction_times_list=time_lst, plot=None)

@app.route('/generate_graph', methods=['POST'])
def generate_graph():

    fig = px.line(x=list(range(1, len(time_lst) + 1)), y=time_lst, title='Reaction Times Over Attempts', labels={'x': 'Attempt Number', 'y': 'Reaction Time (milliseconds)'})

    plot_html = fig.to_html(full_html=False)

    return render_template('index.html', time=None, reaction_times_list=time_lst, plot=plot_html)

if __name__ == "__main__":
    app.run(debug=True)
