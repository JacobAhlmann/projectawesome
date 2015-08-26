from flask import Flask, render_template
from twisted.internet import reactor
from twisted.internet.protocol import Factory,Protocol
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('main.html')


# class IphoneChat(Protocol):
# 	def connectionMade(self):
# 		self.factory.clients.append(self)
# 		print "a client connected"
#
# 	def connectionLost(self, reason):
# 		self.factory.clients.remove(self)
# 		print "AAAHMAGADH HE IS DEAD"
#
# 	def dataReceived(self,data):
# 		a = data.split(':')
# 		print a
# 		if len(a)>1:
# 			command = a[0]
# 			content = a[1]
#
# 			msg=""
# 			if command=="iam":
# 				self.name=content
# 				msg=self.name+ " has joined"
# 			elif command == "msg":
# 				msg=self.name+ ": "+content
# 				print msg
# 			for c in self.factory.clients:
# 				c.message(msg)
# 	def message(self, message):
# 		self.transport.write(message +'\n')
#
# factory=Factory()
# factory.clients=[]
# factory.protocol=IphoneChat
# reactor.listenTCP(80, factory)
# print "Iphone Chat server started"
# reactor.run()
