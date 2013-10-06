#####
# Usage (poor man's man page)
# generatemp3 <requestId> <videoIds> --startTimes <startTimes> --endTimes <endTimes>
#  - requestId should be unique for each request. But if we want to keep old (already processed) clips, they'll still be here under that id
#  - videoIds are space-separated 11-character youtube video ids
#  - startTimes and endTimes are of format minute.second (e.g. 1.40). Note the minute is required.
#  - final output is in file id-spliced.mp3 (e.g. 123-spliced.mp3)
#  - ex. python generatemp3 123 E3418SeWZfQ lVFNRrL79w0 --startTimes 0.30 0.12 --endTimes 0.35 0.15
#####

import argparse, subprocess, sys

MEDIA_ROOT = "media"
cliproot = '../../' + MEDIA_ROOT + '/uploaded_clips/'
quizroot = '../../' + MEDIA_ROOT + '/uploaded_quizzes/'

def youtomp3 (id, link):
	link = 'http://www.youtube.com/watch?v=' + link

	print('youtube-dl ' + link + ' -o ' + cliproot + str(id) + '-ytmp4.mp4')
	sys.stdout.flush()

	subprocess.call('youtube-dl ' + link + ' -o ' + cliproot + str(id) + '-ytmp4.mp4', shell=True)
	subprocess.call('ffmpeg -i ' + cliproot + str(id) + '-ytmp4.mp4 ' + '-f mp3 -vn ' + cliproot + str(id) + '-mp3.mp3', shell=True)
	subprocess.call('rm ' + cliproot + '*.mp4', shell=True)

def stmp3 (id, start, end):
	subprocess.call('mp3splt ' + cliproot + str(id) + '-mp3.mp3 ' + str(start) + ' ' + str(end) + ' -o ' + cliproot + str(id) + '-cut', shell=True)
	subprocess.call('rm ' + cliproot + str(id) + '-mp3.mp3', shell=True)

def mermp3 (id, sfiles):
	splice = 'mp3wrap ' + quizroot + str(id) + '-quiz.mp3'
	for sfile in sfiles:
		splice += ' ../../' + MEDIA_ROOT + '/' + sfile

	subprocess.call(splice, shell=True)
	subprocess.call('mv ' + str(id) + '-spliced_MP3WRAP.mp3 ' + str(id) + '-spliced.mp3', shell=True)
