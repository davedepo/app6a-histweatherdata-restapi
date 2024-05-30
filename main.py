from flask import Flask, render_template
import pandas as pd

# to create website object instances
app = Flask("__name__")


# to connect HTML pages with website object - use .route() method
@app.route("/")
# to render HTML document from "templates" dir/folder - import render_template
def home():
	return render_template("home.html")


# to add more pages
@app.route("/api/v1/<station>/<date>")
def about(station, date):
	filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
	df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
	temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
	return {"station": station,
	        "date": date,
	        "temperature": temperature}


if __name__ == "__main__":
	# to run
	app.run(debug=True)
