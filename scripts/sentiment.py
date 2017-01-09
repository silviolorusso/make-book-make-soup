########################

## SENTIMENT ANALYSIS ##

#########################

import os,sys,time
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

#small function to translate/map values
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


#load the textfile that is passed on from the makefile
text = open(sys.argv[1], 'r').read()
#decode and re-encode to prevent common issues
text = unicode(text, 'utf-8')
#tokenize sentences
o_sentences = tokenize.sent_tokenize(text)
sentences = ['']

SENTENCE_BATCH_SIZE = 5

#batch sentences into chunks of 'SENTENCE_BATCH_SIZE'
for i in range(0,len(o_sentences),5):
	sentences.append(" ".join(o_sentences[i:i+SENTENCE_BATCH_SIZE]))

#load the sentiment analyzer
sid = SentimentIntensityAnalyzer()

#load and configure the HTML file we will be outputting to
print('writing to the HTML file, please wait a few seconds.')

with open("html/preview.html", "w") as html_file:
  	html_file.write("<html><head> \
  		<style> \
  		@import url('https://fonts.googleapis.com/css?family=Poppins:500'); \
  		body{font-family: 'Poppins', sans-serif; font-size:40px; text-rendering:optimizeLegibility; line-height:56px; margin:3em;\
  		background-color:rgb(43,4,33);}\
  		.back{margin: 30px;}\
  		.back span{-webkit-filter: blur(43px); \
		-moz-filter: blur(43px); \
		-o-filter: blur(43px); \
		-ms-filter: blur(43px); \
		filter: blur(43px); \
		padding:3em;} \
		.front{position:absolute;top:0;left:0; margin: 3em; margin-top:1em;} \
		.front span:first-child {paddin-left:0;} \
		.front span, .back span{margin-top:20px;margin-bottom:20px}\
		.hidden{display:none;}\
		.zoomOut{transform: scale(0.5)}\
		*{transition: all 2s ease;}\
		</style></head><body><div class='back'>")

  	#translate the scores from the sentence into rgb values
	for sentence in sentences:
	     ss = sid.polarity_scores(sentence)
	     i = 0
	     rgb = [0]
	     for k in sorted(ss):
	     	if i is 1:
	     		r = translate(ss[k], 0, 0.5, 43, 254)
	     		g = translate(ss[k], 0, 0.5, 4, 255)
	         	b = translate(ss[k], 0, 0.5, 33, 24)   	
	        i += 1
	     #again, encode the sentence to prevent drama
	     sentence = "&nbsp;"+sentence.encode('utf-8').strip()
	     html = '<span style="background-color:rgb({},{},{});color:rgb({},{},{});">{}</span>'.format(int(r),int(g),int(b),int(r),int(g),int(b),sentence)
	     html_file.write(html)
	     html_file.flush()
	#close the first loop (background colors)     
	html_file.write("</div><div class='front'>");

	#rewrite the text over the background
	for sentence in sentences:
	     ss = sid.polarity_scores(sentence)
	     i = 0
	     rgb = [0]
	     for k in sorted(ss):
	     	if i is 2:
	     		r = translate(ss[k], 1, 0, 63, 249)
	     		g = translate(ss[k], 1, 0, 66, 0)
	         	b = translate(ss[k], 1, 0, 69, 133)   	
	        i += 1
	     sentence = sentence.encode('utf-8').strip()
	     html = '<span style="color:white;">{}</span>'.format(sentence)
	     html_file.write(html)
	     html_file.flush()
	#close the html file
	html_file.write("</div>\
	<script>\
	document.querySelector('body').addEventListener('click', toggleFront);\
	function toggleFront(){\
	var front = document.querySelector('.front'); \
	front.classList.toggle('hidden');\
	document.querySelector('body').classList.toggle('zoomOut');\
	}\
	</script>\
	</body>\
	</html>")

print('Done.')

