# rss-youtuberipper
A python script for automatically downloading all new videos from a list of Youtube-channels. 

Steps: 
1) Download the script (rss-youtuberipper.py)
2) Make sure you have the right python-libraries installed. You need requests (built-in), feedparser (https://pypi.python.org/pypi/feedparser) and pytube (https://github.com/nficano/pytube)
3) Open the .py-file in your favorite editor and add the Youtube-channels you want to rip to the list. You'll find the url of the channels rss-feed by changing everything after https://www.youtube.com/feeds/videos.xml?channel_id= to the id of the channel you want to rip. You can find the id by opening a random video from the channel and clicking on the channel name from there. This will lead to the channel startpage and display the id in the browser url-bar.
4) [Optionally] Add the script to you crontab to make sure the script will run continiously.
