from flask import Flask, render_template
import pandas as pd

app2 = Flask(__name__)

# var defined out of function is there is no dependencies
filename = "dictionary.csv"
df = pd.read_csv(filename)


@app2.route("/")
def home():
	return render_template("home_dict.html")


@app2.route("/api/v1/<word>")
def dic(word):
	definition = df.loc[df["word"].str.strip() == word]["definition"].squeeze()
	return {"word": word,
	        "definition": definition}


if __name__ == "__main__":
	app2.run(debug=True, port=5001)
