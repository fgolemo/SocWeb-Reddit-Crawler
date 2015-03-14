import praw
r = praw.Reddit('Research Project Crawler for User Behavior, VU Amsterdam, The Social Web 2015, bot 1/4 by u/fgolemo v 1.0.')
r.set_oauth_app_info(client_id='**********',
                     client_secret='*********************',
                     redirect_uri='http://127.0.0.1:65010/authorize_callback')
url = r.get_authorize_url('uniqueKey', 'identity', True)
import webbrowser
webbrowser.open(url)

access_information = r.get_access_information('************************')
print access_information

