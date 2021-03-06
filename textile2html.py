#!/usr/bin/python2.7
import textile
import argparse
import sys

def get_arguments(parser):
	parser.add_argument('-f', '--file', help="Textile file name", dest="file")
	parser.add_argument('-t', '--type', help="Set the output (standar|file)", default="file", dest="type")
	parser.add_argument('-o', '--output', help="Output file name", default="untitled.html", dest="output")
	args = parser.parse_args()
	return args

def read_textile(archivo):
	f = open(archivo, 'r')
	text = f.read()
	f.close()
	return text

def textile_2_html(text):
	html = textile.textile(text)
	return html

def write_html(html, archivo):
	s = str(html)
	f = open(archivo, "w+")
	f.write(s)
	f.close()
	


parser = argparse.ArgumentParser()	
args = get_arguments(parser)
text = ""
text = read_textile(args.file)
if args.type == 'file':
	write_html(textile_2_html(text), args.output)
else:
	print textile_2_html(text)
	
