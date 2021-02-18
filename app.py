# Import Dependecies pandas, numpy, sqlalchemy, and flask/jsonify
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Create Engine (copy pasta from jupyter notebook)
engine = create_engine("sqlite://resources/hawaii.sqlite")
    # reflect an existing database into a new model
base=automap_base()
    # reflect the tables
base.prepare(engine, reflect=True)
