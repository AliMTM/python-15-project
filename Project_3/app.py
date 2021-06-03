from flask import Flask, render_template, url_for, request, redirect
import string

app = Flask(__name__)

def key_creator(keyword):

    vocab = string.ascii_lowercase + string.ascii_uppercase + string.digits
    key = 0

    for l in keyword:
        if l.isalnum():
            key += vocab.find(l) + 1

    return key

def encrypt(key, text):

    vocab = string.ascii_lowercase + string.ascii_uppercase + string.digits
    vocab_length = len(vocab)
    output_text = ""

    for l in text:
        if l.isalnum():
            output_text += vocab[(vocab.find(l) + key) % vocab_length]
        else:
            output_text += l

    return output_text

def decrypt(key, text):

    vocab = string.ascii_lowercase + string.ascii_uppercase + string.digits
    vocab_length = len(vocab)
    output_text = ""

    for l in text:
        if l.isalnum():
            output_text += vocab[(vocab.find(l) - key) % vocab_length]
        else:
            output_text += l

    return output_text


@app.route('/')
def index():
    return render_template("input.html", input_text="Enter your Text here ...")

@app.route('/submit', methods=['POST'])
def submit():
    keyword = request.form['keyword']
    text = request.form['input_textarea']

    key = key_creator(keyword)

    if request.form.get("encrypt"):

        output_text = encrypt(key, text)
        title_text = "Encrypted Text"

    elif request.form.get("decrypt"):

        output_text = decrypt(key, text)
        title_text = "Decrypted Text"

    return render_template('output.html', output_text = output_text, title_text = title_text)

if __name__ == "__main__":
    app.run(debug=True)