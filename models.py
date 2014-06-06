from django.db import models

from mongoengine import *
connect ('poptweets')

# Create your models here.

'''
var Tweets_json = {"type": "FeatureCollection",
                    "features":
                    [
                        {"geometry":
                            {"type": "Point", ...
'''
'''
    Tweet_geojson = {
        "type": "Feature",
        "properties": {
            "time_": time_,
            
            "username_": username_,
            "userID_": userID_,
            "tweet_": tweet_,
            "replyto_": replyto_,
            "hashtags_": hashtags_,
            "language_": language_,
            "place_": place_,
            "country_": country_,
            "username_": json_unicode(username_),
            "tweet_": json_unicode(tweet_),
            "replyto_": json_unicode(replyto_),
            "hashtags_": json_unicode(hashtags_),
            "language_": json_unicode(language_),
            "place_": json_unicode(place_),
            "country_": json_unicode(country_),
            
            "nb_cycles_": 0,
            "radius_": self.radius_max_dots_,
            "opacity_": self.opacity_max_dots_,
            "color_": self.color_dots_,
            },
        "geometry": {
            "type": "Point",
            "coordinates": # tweets coordinates long and lat are inverted
                [geo_[1], # lat
                 geo_[0]] # long
            }
        }
'''

'''
class Poll(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    choices = ListField(EmbeddedDocumentField(Choice))

    meta = {
        'indexes': [
            'question', 
            ('pub_date', '+question')
        ]
    }
''' 
