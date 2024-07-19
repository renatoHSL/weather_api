from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("data/dictionary.csv")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def word_definition(word):
    definition = df.loc[df['word'] == word].to_dict(orient='records')
    description = definition[0]['definition']
    # another solution:
    # definition = df.loc[df["word] == word]['definition'].squeeze()
    # result_dictionary = {'word': word, 'definition': definition}
    return {"definition": description,
            "word": word}


if __name__ == "__main__":
    app.run(debug=True, port=5001)
