from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishtofrench():
    textToTranslate = request.args.get('textToTranslate')
    text = translator.englishtofrench(textToTranslate)
    return text

@app.route("/frenchToEnglish")
def frenchtoenglish():
    textToTranslate = request.args.get('textToTranslate')
    text = translator.frenchtoenglish(textToTranslate)
    return text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
