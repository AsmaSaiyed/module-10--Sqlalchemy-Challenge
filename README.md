# Sqlalchemy-Challenge -Hawaii

This file includes the use of Pandas, Sqlalchemy, VSCode and Flask to conduct a climate analysions for a Hawaii Vacation trip. 
The files (climate_starter.ipynb and hawaii.sqlite) were used to complete your climate analysis and data exploration and are present in the Resourcces file.

The following steps were conducted to accomplish this task.
1.Use the SQLAlchemy create_engine() function to connect to the SQLite database.

2.Use the SQLAlchemy automap_base() function to reflect the tables into classes, and then save references to the classes named station and measurement.

3.Link Python to the database by creating a SQLAlchemy session.


# Part 1: Analyze and Explore the Climate Data #

### Precipitation Analysis ###
1.Find the most recent date in the dataset.

2.Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

3.Select only the "date" and "prcp" values.

4.Load the query results into a Pandas DataFrame. Explicitly set the column names.

5.Sort the DataFrame values by "date".

6.Plot the results by using the DataFrame plot method

7.Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis ###
1.Design a query to calculate the total number of stations in the dataset.

2.Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
List the stations and observation counts in descending order.Answer the following question: which station id has the greatest number of observations?

3.Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

4.Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:

5.Filter by the station that has the greatest number of observations.

6.Query the previous 12 months of TOBS data for that station.

7.Plot the results as a histogram with bins=12, as the following image shows:

# Part 2: Design Your Climate App #
Now that initial analysis is complete, design a Flask API based on the queries that were just developed. To do so, use Flask to create the routes as follows:

1./

* Start at the homepage.

* List all the available routes.



2./api/v1.0/precipitation

* Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

* Return the JSON representation of your dictionary.




3./api/v1.0/stations

* Return a JSON list of stations from the dataset.




4./api/v1.0/tobs

* Query the dates and temperature observations of the most-active station for the previous year of data.

* Return a JSON list of temperature observations for the previous year.




5./api/v1.0/<start> and /api/v1.0/<start>/<end>

* Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

* For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

* For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
