# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()


# reflect the tables

Base.prepare(autoload_with=engine)

# Save references to each table
print(Base.classes.keys())


measurement = Base.classes.measurement
station = Base.classes.station

Create our session (link) from Python to the DB


################################################
Flask Setup
################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    # List all available api routes.
    return (
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )



    @app.route("/api/v1.0/precipitation")
    def  precipitation():
    # Create a session (link) from Python to the DB 
        session = Session(engine)

    # getting the precipitation data for most recent date in the data 
    most_recent_date = session.query(func.max(measurement.date)).first()

     # get the dates for 1 year before the most reccent date
    date_year_ago=dt.date(2017, 8, 23) - dt.timedelta(days=365)


    # getting the prcp and date data from measurement of between 2017-08-23 and 2016-08-23
    last_year_prcp= session.query(measurement.date, measurement.prcp).filter(measurement.date >=date_year_ago).all()

     # Close session
    session.close
    
    # making a dictionary with the key of prcp and date
    precip = {date: prcp for date, prcp in last_year_prcp}

    # Return the JSON representation of your dictionary.
    return jsonify (precip)       


    @app.route("/api/v1.0/stations")
    def stations():

    # Create a session (link) from Python to the DB
        Session = Session(engine)

    # Query for all the stations.
    stations = session.query(Station.station, Station.name,
                             Station.latitude, Station.longitude, Station.elevation).all()
            
    #  Close session
    session.close()


    # presenting the stations into a dictionary
    all_stations = []
    for stations, name, latitude, longitude, elevation in stations:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        station_dict["latitude"] = latitude
        station_dict["longitude"] = longitude
        station_dict["elevation"] = elevation
        all_stations.append(station_dict)


    # Return a JSON list of stations from the dataset.    
        return jsonify(all_stations)
    



    @app.route("/api/v1.0/tobs")
    def Temperature():

    # Create session (link) from Python to the DB
        Session = Session(engine)

    # Query the dates and temperature observations of the most-active station for the previous year of data.
    # Find the most- active station of the data
    most_active_station = session.query(measurement.station).group_by(measurement.station).\
                        order_by(func.count(measurement.station).desc()).first()
     
    # Return a list of temperature observations for the previous year.

    last_12_months = session.query(measurement.date, measurement.tobs).\
    filter(measurement.station == "USC00519281").\
    filter(func.strftime(measurement.date) >date_year_ago ).all()
    
    #  Close session
    session.close()

    # present the query data as a dictionary
    tobs_temp_12  = {date: tobs for date, tobs in last_12_months}

    # Return a JSON list of temperature observations for the previous year.  
    return jsonify( tobs_temp_12)




    @app.route("/api/v1.0/<start>", defaults={'end': None})
 
    @app.route("/api/v1.0/<start>/<end>")

    def temp_stats(start,end):

#  Create a session (link) from Python to the DB
        session = Session(engine)

# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
        results_start = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
              filter(measurement.date >= start).order_by(measurement.date.desc()).all()

# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
        results_start_end = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs))\
        .filter(measurement.date >= start)\
        .filter(measurement.date <= end).all()

 #  Close session
    session.close()

#  presenting the queries as dictonaries
    for temps in results_start:
        dict1 = {"Minimum Temp":results[0][0],"Maximum Temp":results[0][1],"Average Temp":results[0][2]}

    for temps in results_start_end:
        dict2 = {"Minimum Temp":results[0][0],"Maximum Temp":results[0][1],"Average Temp":results[0][2]}
 # Return a JSON list of stations from the dataset. 
             
    return jsonify (dict1,dict2) 
    
if __name__ == "__main__":
    app.run(debug=True)
  