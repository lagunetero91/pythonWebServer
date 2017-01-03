#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse
import httplib, urllib, urllib2
ADDR = "localhost"
PORT = 80

class RequestHandler(BaseHTTPRequestHandler):
	#Tratamiento de peticiones POST
	def do_POST(self):
		tamaño = int(self.headers['Content-Length'])
		#dividimos los campos de la petición
		campos_post = urlparse.parse_qs(self.rfile.read(lenght))
		#Mostramos campos de la petición
		for key, value in campos_post.iteritems():
			print "%s=%s" % (key,value)	
	
	#Tratamiento de peticiones GET
	def go_GET(self):




#Servidor Web en localhost en puerto 80
httpd = HTTPServer((ADDR,PORT),RequestHandler)
httpd.serve_forever()