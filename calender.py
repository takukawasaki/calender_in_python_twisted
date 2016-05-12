#!/Users/kawasakitaku/Documents/python-PVM/ln-python2.7/bin/python2.7

from twisted.internet import reactor
from twisted.web.resource import Resource,NoResource
from twisted.web.server import Site



from calendar import calendar

class YearPage(Resource):
    def __init__(self,year):
        Resource.__init__(self)
        self.year = year

    def render_GET(self,request):
        return "<html><body><pre>%s</pre></body></html>" % (calendar(self.year),)

class CalenderHome(Resource):
    def getChild(self,name,request):
        if name == '':
            return self
        if name.isdigit():
            return YearPage(int(name))
        else:
            return NoResource()

    def render_GET(self,request):
        return "<html><body>Welcome to the calender server!</body></html>"

root = CalenderHome()
factory = Site(root)
reactor.listenTCP(8000,factory)
reactor.run()
