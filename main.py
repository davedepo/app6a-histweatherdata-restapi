from flask import Flask, render_template
import pandas as pd

# to create website object instances - import Flask
app = Flask("__name__")

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 ", "CN"]]


# to connect HTML pages with website object - use .route() method
@app.route("/")
# to render HTML document from "templates" dir - import render_template
def home():
	return render_template("home.html", data=stations.to_html())


# to add more pages/url endpoints
@app.route("/api/v1/<station>/<date>")
def about(station, date):
	filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
	df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
	temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
	return {"station": station,
	        "date": date,
	        "temperature": temperature}


@app.route("/api/v1/<station>")
def all_data(station):
	filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
	df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
	result = df.to_dict(orient="records")
	return result


@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
	filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
	df = pd.read_csv(filename, skiprows=20)
	df["    DATE"] = df["    DATE"].astype(str)
	result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
	return result


if __name__ == "__main__":
	# to run
	app.run(debug=True)
