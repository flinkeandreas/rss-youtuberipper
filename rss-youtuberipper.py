import requests # handle the http requests to the website
import feedparser # parse the rssfeeds
from pytube import YouTube # work the youtube magic

channel_urls = ["https://www.youtube.com/feeds/videos.xml?channel_id=UCWRZyxG8M420d0Bxj7DtLbw", # Medina (danish pop)
                "https://www.youtube.com/feeds/videos.xml?channel_id=UCyqhj3unXdUW89Jgv2Lgd7A", # Linda Pira (swedish hiphop)
	              "https://www.youtube.com/feeds/videos.xml?channel_id=UCM4tt6pjbeSRL4pl-EUm0Hg"] # Cherrie (more swedish hiphop)

for url in channel_urls:
	rssrawdata = feedparser.parse(url)
	for feedentity in rssrawdata.entries:
		videolink = feedentity.link
		YouTube(videolink).streams.first().download()
		print "Ripping " + feedentity.title
