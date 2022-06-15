# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 10:08:52 2022

@author: kater
"""

import pandas as pd
import sqlalchemy
import myconfig as cfg



schema="gans2"
host=cfg.get_data('DATABASE_HOST')
user=cfg.get_data('DATABASE_USER')
password=cfg.get_data('DATABASE_PASSWORD')
port=cfg.get_data('DATABASE_PORT')
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'


cities_df = pd.read_csv('cities.csv')
cities_df.to_sql('cities', 
              if_exists='append', 
              con=con, 
              index=False)

weather = pd.read_csv('weather.csv')
weather.to_sql('weathers', 
              if_exists='append', 
              con=con, 
              index=False)

airports = pd.read_csv('airports_new.csv')
airports.to_sql('airports', 
              if_exists='append', 
              con=con, 
              index=False)

flights = pd.read_csv('flights_new.csv')
flights.to_sql('flights', 
              if_exists='append', 
              con=con, 
              index=False)