from flask import Flask, render_template, request, jsonify, redirect, url_for

from word_frequency.word_frequency_counter import word_frequency_data_for_d3

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/post_text', methods=['POST'])
def post_text():
    text_data = str(request.json)
    if not text_data:
        return redirect(url_for('index'))
    word_freq = word_frequency_data_for_d3(text_data)
    return jsonify(word_freq)

if __name__ == '__main__':
    app.run(debug=False)
