
from functions import create_plot,render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    clv_bar = clv_churn_plot()
    return render_template('index.html', plot=clv_bar)


if __name__ == '__main__':
    app.run(debug = True)


