from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route('/englishToFrench', methods=['GET', 'POST'])
def english_to_french():
    text_to_translate = request.args.get('textToTranslate')
    english_text = request.form.get(text_to_translate)  # replace 'text' with the actual name of your input field
    french_text = translator.english_to_french(english_text)
    return french_text

@app.route('/frenchToEnglish', methods=['GET', 'POST'])
def french_to_english():
    text_to_translate = request.args.get('textToTranslate')
    french_text = request.form.get(text_to_translate)  # replace 'text' with the actual name of your input field
    english_text = translator.french_to_english(french_text)
    return english_text

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
