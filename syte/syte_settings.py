# -*- coding: utf-8 -*-

DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.0'


#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'fredericjacobs.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = 'QaSNpYk4iYNAjTuNB6VJ1Hgh4y8tgNV1YJvgjC9mOT2VOHvMZB'

#RSS Feed Integration: (by default use Tumbrl rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'https://api.twitter.com/'
TWITTER_CONSUMER_KEY = '8Rny4itbogL77GCZQu7A'
TWITTER_CONSUMER_SECRET = 'HwQPSBGECUAMNLAixir7P6cTvcfGU95neLH4Ewe67iM'
TWITTER_USER_KEY = '18018877-S1pYJuSHuwDaX0KEii2GKMTWd4Y4CBqn3pzmES0'
TWITTER_USER_SECRET = 'DslE3mEnz2wv7TfrdtEtZsboO9xLoi6ddrco8pJQAE'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = 'd569ab44bbad7ed94352530c1b7ed435dabcb9e7'

GITHUB_OAUTH_ENABLED = True
GITHUB_CLIENT_ID = '03a99bf3155799da11b5'
GITHUB_CLIENT_SECRET = 'f3fd59cae9d56faa4a64c8ce9e626e654d86dee7'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = True
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '1108533.4a6bc48.801e97fe0210416893e38ed1156e5324'
INSTAGRAM_USER_ID = '1108533'

INSTAGRAM_OAUTH_ENABLED = False
INSTAGRAM_CLIENT_ID = '4a6bc48d0d2449d48ced0eeee275b8e5'
INSTAGRAM_CLIENT_SECRET = '419464e8912746029b463cb57c297607'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


#Foursquare Integration
FOURSQUARE_INTEGRATION_ENABLED = True
FOURSQUARE_API_URL = 'https://api.foursquare.com/v2/'
FOURSQUARE_ACCESS_TOKEN = 'DTXSJT4EIKW2BJUZKKM0MXLGRV4RWUBQZ5KRDKQCWM13SB0E'
FOURSQUARE_SHOW_CURRENT_DAY = True

FOURSQUARE_OAUTH_ENABLED = False
FOURSQUARE_CLIENT_ID = 'MYGZPTQRE0S5XHPNIAXNEBO0K32USKGRCYY5FTO1WOHCBZX4'
FOURSQUARE_CLIENT_SECRET = 'NZZ3PDHCZIULP3SWSZBLT45SPN42DFX455Q01NL4ZK0KFLEW'
FOURSQUARE_OAUTH_AUTHORIZE_URL = 'https://foursquare.com/oauth2/authenticate'
FOURSQUARE_OAUTH_ACCESS_TOKEN_URL = 'https://foursquare.com/oauth2/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = 'UA-10448312-8'


#Woopra
WOOPRA_TRACKING_DOMAIN = ''
WOOPRA_TRACKING_IDLE_TIMEOUT = 300000  # 5 minutes
WOOPRA_TRACKING_INCLUDE_QUERY = False



#Disqus Integration
DISQUS_INTEGRATION_ENABLED = False
DISQUS_SHORTNAME = ''


#Lastfm Integration
LASTFM_INTEGRATION_ENABLED = False
LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'
LASTFM_API_KEY = '[ENTER LASTFM API_KEY HERE, SEE LASTFM SETUP INSTRUCTIONS]'

#SoundCloud Integration
SOUNDCLOUD_INTEGRATION_ENABLED = True
SOUNDCLOUD_API_URL = 'https://api.soundcloud.com/'
SOUNDCLOUD_CLIENT_ID = 'e36315e6c89679990963d22c5a39a2fc'
SOUNDCLOUD_SHOW_ARTWORK = False
SOUNDCLOUD_PLAYER_COLOR = 'ff912b'


#Bitbucket Integration
BITBUCKET_INTEGRATION_ENABLED = False
BITBUCKET_API_URL = 'https://api.bitbucket.org/1.0/'
# Forks count require one connection for each repository,
# set BITBUCKET_SHOW_FORKS to false to disable
BITBUCKET_SHOW_FORKS = False

#Tent.io Integration
TENT_INTEGRATION_ENABLED = True
TENT_ENTITY_URI = 'https://fred.tent.is'
TENT_FEED_URL = 'https://fred.tent.is'




if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://www.fredericjacobs.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
