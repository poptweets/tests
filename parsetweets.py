## A program to parse Turkish geocoded tweets
## put the results in a GeoJSON
## Julien Paris : 16/05/2014

import json
import time
import sys
import threading

 
## Check the copyrights for using the codes below ...
import tweepy

#from .models import Stream_Tweet_World


# LISTENER RECEIVING DATAS + CALL CLEANER ------------------------------------------------------------------
class StdOutListener(tweepy.StreamListener):

    def __init__(self):        
        self.Tweets_list = []
        self.laps = 0.0 # interval of x seconds between two tweets
        self.Tweets_geojson = {"type": "FeatureCollection","features": ""}
        self.color_dots_ = "#ff7800" # some orange
        self.max_cycle = 2500.0 # erase after x cycles

        self.opacity_max_dots_ = 1.0
        self.lessopa_ = self.opacity_max_dots_ / self.max_cycle

        self.radius_max_dots_ = 100.0 # in pixels for Leaflet
        self.lessradius_ = self.radius_max_dots_ / self.max_cycle

##    def json_unicode(self, list_):
##        # get the character's unicode for Json lists
##        json_uni = json.loads(list_)
##        return json_uni

      
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)
        print '__ parsing new tweet'
        
        if decoded['geo'] is None :
            pass
        else :
            #print decoded
            
            #### GEO CODE ----------- ################################ 
            geo_ = decoded['geo']['coordinates']
            print geo_

            #### TIME ----------- ################################ 
            time_ = decoded['created_at']

            #### TWEET ----------- ################################ 
            tweet_ = decoded['text'] #.encode('ascii', 'ignore') # .decode('utf-8')
            
            #### USER ID ----------- ################################ 
            userID_ = decoded['user']['id']
            username_ = decoded['user']['screen_name']

            #### PLACE NAME ----------- ################################ 
            try : 
                place_ = decoded['place']['name']
            except:
                place_ = None
                pass
            
            #### COUNTRY ----------- ################################ 
            try :
                country_ = decoded['place']['country']
            except :
                country_ = None
                pass

            #### REPLY_TO ID---------- ############################ 
            try :
                replyto_ = decoded['in_reply_to_user_id']
            except :
                replyto_ = None
                pass
            
            #### LANGUAGE ----------- ################################ 
            try :
                language_ = decoded['user']['lang']
            except :
                language_ = None
                pass

            #### HASHTAGS ----------- ################################ 
            try : 
                hashtags_ = decoded['hashtags']
            except:
                hashtags_ = None
                pass

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
                    #"username_": json_unicode(username_),
                    #"tweet_": json_unicode(tweet_),
                    #"replyto_": json_unicode(replyto_),
                    #"hashtags_": json_unicode(hashtags_),
                    #"language_": json_unicode(language_),
                    #"place_": json_unicode(place_),
                    #"country_": json_unicode(country_),
                    
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


            self.Tweets_list.append(Tweet_geojson)
            # print self.Tweets_list 
            # print "    L_ tweet appended to self.Tweets_list..." # works OK


            for tw_json in self.Tweets_list :
                nbcycle = tw_json['properties']['nb_cycles_']

                if nbcycle >= 0 and nbcycle < self.max_cycle:
                    tw_json['properties']['nb_cycles_'] += 1
                    # print "     L_ :", nbcycle # works OK

                    # varcycle_ = tw_json['properties']['nb_cycles_']
                    # print "    L_ cycle number: ", varcycle_ , " / opacity: ", self.lessopa_
                    
                    tw_json['properties']['opacity_'] -= self.lessopa_
                    tw_json['properties']['radius_'] -= self.lessradius_
                                      

                elif nbcycle > self.max_cycle :
                    self.Tweets_list.remove(tw_json) 
            #print "    L_ cleaning done for self.Tweets_list..." # ...


            self.Tweets_geojson["features"] = self.Tweets_list
            with open('TEST_Tweets_geojson_out6.js', 'w') as outfile:
                json.dump(self.Tweets_geojson, outfile)
            print "    L_ Tweets_geojson_out.js overwritten..." # works OK

            Tweet_geojson = ''
            # print "    L_ Tweet_geojson emptied..." # works OK


            time.sleep(self.laps)

            return True


    def on_error(self, status):
        pass
        #print "--- Error status : ",status


# MAIN CALL FUNCTIONS--------------------------------------------------------------------
class Main_Parse_and_clean:
    
    def __init__(self, on_off_pause=1):
        self.on_off_pause = "on"
        print "Starting parsing"
    
    def Parse_and_Clean (self, geobox):
    
        ### TWITTER API TOKEN ####################################     
        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''
        
        geobox_choosen = geobox # Here to be able to call function defining new geoboxes
    
        track_choosen = [] # nothing by default
        
        l = StdOutListener() ## call function Twitter Listener
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        #i=1
        if self.on_off_pause=="on" :
            try :
                stream = tweepy.Stream(auth, l)
               # stream.filter(track=track_choosen)
                stream.filter(locations=geobox_choosen, async=False)
                           
            except:
                pass

        elif self.on_off_pause == "pause"
            pass
        
        else:
            pass
