from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import AnswerForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chapter/<int:number>', methods=['GET', 'POST'])
def chapter(number):
    form = AnswerForm()

    if number == 0:
        return render_template('preface.html')

    chapterFileName = 'chapter-{number}.html'
    
    return render_template(chapterFileName.format(number=number), form=form)

@app.route('/expand/<topic_name>')
def expand(topic_name):
    return render_template('expand-topics/' + topic_name + '.html')


if '__main__' == __name__:
    app.run()
