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
engine = create_engine("sqlite://resources/hawaii.sqlite")
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
        f"Aloha!"
    )