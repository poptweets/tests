# -*- coding: utf-8 -*-

from mongoengine import *
connect(‘mongodb_jsons’)

import datetime

class GeoJson(Document):
 # from a geojson object
 # save it in Mongodb with a geojson structure

    Date_created = DateTimeField(default=datetime.datetime.now)
    Location = PointField(auto_index=False) # as a list of 2 float numbers [ 10.000 , 240.000 ]
    username_ = CharField()
    userID_ = CharField()
    tweet_ = CharField()
    replyto_ = CharField()
    hashtags_ = CharField() # list
    language_ = CharField()
    place_ = CharField()
    country_ = CharField()
    
    nb_cycles_ = DecimalField()
    radius_ = DecimalField()
    opacity_ = DecimalField()
    color_ = CharField()

    meta = {'db_alias': 'mongodb_jsons', # save in DB ‘mongodb_jsons’
            'indexes': [                 # the geojson structure
                {'type' : 'Feature', {
                   'geometry':{
                        'type' : 'Point',
                        'coordinates' : ('Location', '2dsphere')
                        }, 
                   'properties':{
                        'content1' : 'Content1',
                        'content2' : 'Content2',    
                        'date_creation' : 'Date_created',
                        'username_' = 'username_',
                        'userID_' = 'userID_',
                        'tweet_' = 'tweet_',
                        'replyto_' = 'replyto_',
                        'hashtags_' = 'hashtags_',
                        'language_' = 'language_',
                        'place_' = 'place_',
                        'country_' = 'country_',
                        'nb_cycles_': 'nb_cycles_',
                        'radius_': 'radius_',
                        'opacity_': 'opacity_',
                        'color_': 'color_'                   
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
