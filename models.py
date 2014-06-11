# -*- coding: utf-8 -*-

from mongoengine import *
connect('mongodb_jsons')

import datetime

class GeoJson(Document):
 # from a geojson object
 # save it in Mongodb with a geojson structure

    Date_created = DateTimeField(default=datetime.datetime.now)
    Location = PointField(auto_index=False) # as a list of 2 float numbers [ 10.000 , 240.000 ]
    username_ = CharField()
    userID = CharField()
    tweet = CharField()
    replyto = CharField()
    hashtags = CharField() # list
    language = CharField()
    place = CharField()
    country = CharField()
    
    nb_cycles = DecimalField()
    radius = DecimalField()
    opacity = DecimalField()
    color = CharField()

    meta = {'db_alias': 'mongodb_jsons', # save in DB ‘mongodb_jsons’
            'indexes': [                 # the geojson structure
                {'type' : 'Feature', {
                   'geometry':{
                        'type' : 'Point',
                        'coordinates' : ('Location', '2dsphere')
                        }, 
                   'properties':{
                        'date_creation' : 'Date_created',
                        'username_' = 'username_',
                        'userID_' = 'userID_',
                        'tweet' = 'tweet_',
                        'replyto' = 'replyto_',
                        'hashtags' = 'hashtags_',
                        'language' = 'language_',
                        'place' = 'place_',
                        'country' = 'country_',
                        'nb_cycles': 'nb_cycles_',
                        'radius': 'radius_',
                        'opacity': 'opacity_',
                        'color': 'color_'                   
                        }
                    }
                }]
            }

'''
"nb_cycles_": 0,
"radius_": self.radius_max_dots_,
"opacity_": self.opacity_max_dots_,
"color_": self.color_dots_,   
'''
