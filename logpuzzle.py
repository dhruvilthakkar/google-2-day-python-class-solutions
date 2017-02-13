#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  f=open(filename,'r')
  text=f.read()
  m=re.findall('[\S]+puzzle[\S]+',text)
  # +++your code here+++
  final=[]
  for each in m:
    if each not in final:
      final.append(each)
      #print each
  return  final
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
  count=0
  for each_url in img_urls:
    complete_url='http://code.google.com'+each_url
    print complete_url
    urllib.urlretrieve(complete_url,dest_dir+'/img'+str(count))
    count+=1
  index_file=dest_dir+'/index.html'
  index='<html><body><img src="img0"><img src="img1"><img src="img2"><img src="img3"><img src="img4"><img src="img5"><img src="img6"><img src="img7"><img src="img8"><img src="img9"><img src="img10"><img src="img11"><img src="img12"><img src="img13"><img src="img14"><img src="img15"><img src="img16"><img src="img17"><img src="img18"><img src="img19"></body></html>'
  f=open(index_file,'w')
  f.write(index)
  return
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
