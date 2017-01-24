#Working code shown to TF Kevin
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

def getRandomFortune():
    fortunes = [
    "You will be like the righteous, who fight like a lion! Rrrr..oar !",
    "Your goal:Commit your plans to the Lord,and He will make you succeed !Grrr..eat !",
    "You will inherit $23,412 next week !Just peachy !",
    "You will go on a trip soon !",
    "You will get a pleasant surprise in the mail !"
    ]
    index = random.randint(0,4)
    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = '<h1> Fortune Cookie </h1>'

        fortune = "<strong>"+ getRandomFortune() + "</strong"
        fortune_sentence = "Your fortune : " + fortune
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"

        lucky_number = "<strong>"+str(random.randint(1,100))+ "</strong>"
        number_sentence = 'Your lucky number is :'+lucky_number
        number_paragraph = "<p>" + number_sentence + "</p>"
        cookie_again_button = "<a href='.'><button>Another cookie please !</button></a>"

        content = header + number_paragraph+ fortune_paragraph+" <br><br>" +cookie_again_button
        self.response.write(content)
        # I am writing a HTTP response to be sent to the user who sent the request to view my fortune cookie web page
'''
class LoginHandler(webapp2.RequestHandler) :
    def get(self) :
        self.response.write('Thanks for trying to login !')

routes = [
    ('/', MainHandler),
    ('/login', LoginHandler)
    ]
'''
app = webapp2.WSGIApplication( [
    ('/', MainHandler)
    ],debug=True)
