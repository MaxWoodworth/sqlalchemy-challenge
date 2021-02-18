# Import Dependecies pandas, numpy, sqlalchemy, and flask/jsonify
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

## Create Engine (copy pasta from jupyter notebook)
engine = create_engine("sqlite:///resources/hawaii.sqlite")
    # reflect an existing database into a new model
base=automap_base()
    # reflect the tables
base.prepare(engine, reflect=True)
    # Save references to each table
measurement = base.classes.measurement
stations = base.classes.station
    # Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)
#Routes
# / Homepage and list all routes that are available
@app.route("/")
def aloha():
    return(
        f"Aloha! Check out this Historical Weather Data for Hawaii.<br/>"
        f"All Available Routes<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

#Percipitation route #copy pasta current_data
@app.route("/api/v1.0/precipitation")
def current_data():
    current_data = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #bring in rain query and return jsonify
    rain = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date > current_data).\
    order_by(measurement.date).all()
    return jsonify(dict(rain))
    
#Stations
#Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/station")
def stations():
    #kept getting 500 error when I tried to run from stations.station but this should work the same
    stat = session.query(measurement.station).all()
    #after testing there was a ton of space between sations so I used ravel to get a flattened array ny unraveling and making it a list.
    # link to documentation https://numpy.org/doc/stable/reference/generated/numpy.ravel.html
    stations = list(np.ravel(stat))
    return jsonify(stations)

#Temperatures
#Query the dates and temperature observations of the most active station for the last year of data.
#Return a JSON list of temperature observations (TOBS) for the previous year.
@app.route("/api/v1.0/tobs")
def temps():
     #again copy pasta format for getting the last years data
     current_data = dt.date(2017, 8, 23) - dt.timedelta(days=365)
     #copy pasta final query from jupyternb
     final = session.query(measurement.tobs).\
     filter(measurement.station == 'USC00519281').\
     filter(measurement.date > current_data).all()
     finals = list(np.ravel(final))
     return jsonify(finals)



if __name__ == "__main__":
    app.run(debug=True)