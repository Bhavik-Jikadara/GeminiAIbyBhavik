from flask import Flask, render_template, request
import google.generativeai as genai
import textwrap

from IPython.display import display
from IPython.display import Markdown
import os
from dotenv import load_dotenv
load_dotenv()


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


app = Flask(__name__)

# setup your API_KEY
genai.configure(
    # Put the key in the GOOGLE_API_KEY or .env file
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(model_name='gemini-pro')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/response', methods=['GET', 'POST'])
def response():
    return render_template("response.html")


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        text = request.form.get("text")
        response = model.generate_content(text)

    return render_template('response.html', gen_response=response.text)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
