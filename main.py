config = {}

config['webapp2_extras.sessions'] = {
    'secret_key': 'my-key'
}

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


app = webapp2.WSGIApplication([
    webapp2.Route('/',
                  handler='user_profile.handler.index.index_handler.Index')
], debug=True, config=config)
