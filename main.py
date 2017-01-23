#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#So,
#1)RequestHandler
#2) WSGIApplication
#are some of the classes defined in the library named webapp2.They help our web  application

import webapp2
import random
class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = '<h1> Fortune Cookie </h1>'
        lucky_number = random.randint(1,100)
        number_sentence = 'Your lucky number is :'+str(lucky_number)
        number_paragraph = "<p>" + number_sentence + "</p>"
        self.response.write(header + number_paragraph)
        # I am writing a HTTP response to be sent to the user who sent the request to view my fortune cookie web page
class LoginHandler(webapp2.RequestHandler) :
    def get(self) :
        self.response.write('Thanks for trying to login !')

routes = [
    ('/', MainHandler),
    ('/login', LoginHandler)
    ]
app = webapp2.WSGIApplication( routes,debug=True)
