Developping Pop'Tweets : 
=====

Those files are samples of what constitutes the architecture of Pop'Tweets web app.


Purpose of Pop'Tweets :
=====

RealTime webapp to show and analyze stream of geocoded datas.

Pop'Tweets aims :
    - to be simple to use;
    - to select a topic you are interested in (concerts, friends, protests...);
    - to see the tweets appearing directly on a map on different scales (country, city, street...) ;
    - to see the changes happening live, so popping first and disappearing then on the map ;
    - to be able read the stream"s history and the evolution in the time.

Pop'Tweets is designed for :
    - Anyone curious about maps and informations;
    - Social scientists who would like to analyze Twitter evolution;
    - Activists who would like to make surveys of specific events;


Current problems to solve (on 06/06/2014):
=====

- Set up a multiDB in Django : 
    on one side the Sqlite3 (in local) or Mysql (in production) for users infos;
    on another side the MongoDB via Mongoengine driver to store the geo-coded tweets;

- Set up the admin backend to acces MongoDB datas on the backend;

- Store User infos and set up a session manager;


Technical challenges :
=====

Pop'Tweets is an app written in Python, and uses a popular web framework named Django. The design of the app is based on the Bootstrap library. The Python program calls the Twitter API to get a live stream of datas (with Tweepy) from a specific geographical area (first filtering by geo-box). Then it filters only the geo-coded tweets, and continuously index and store them in a dynamic database coded in Json (MongoDB for instance).

Call asynchronously Celery and RabbitMQ : 
  - to be able to render other programs at the same time. Those other programs are as following :

Rendering the tweets on a map :
  - the rendering is done thanks to the Leaflet library, displaying the tweets on an Open Street Map layout, adding in a popup the content of the tweet or user information (like its name). Some codes in JQuery makes that map refresh automatically every x seconds.

Requesting some specific criterias for a Pop'Tweets search :
  - specify location, topics, hashtag, username... and store them in a MongoDB database.

Registering users :
  - collect basics informations given by the users like twitter username, email, location, password, searches history... and store them in a MySQL database.

Getting the most discussed or most popular topics of the moment :
  - using the Twitter API.

Analyzing the streams :
  - with Numpy and Panda Python libraries.

Getting feedback from users :
    from a blog page included in the web app. 
