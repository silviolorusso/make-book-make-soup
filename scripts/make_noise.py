#!/usr/bin/env python
import wave, struct, math

#text
# defines text to be used (should loop through all md files)
your_file = open("md/01.md","r+")
text = your_file.read()

text = text.replace("\n" , " " )

 # divides the text into lines and defines some arrays
words = text.split(" ")
nr = len(words)

filename = "/wav/noise.wav"
nframes=0
nchannels=1
sampwidth=2 # in bytes so 2=16bit, 1=8bit
framerate=44100
bufsize=2048

w = wave.open(filename, 'w')
w.setparams((nchannels, sampwidth, framerate, nframes, 'NONE', 'not compressed'))

max_amplitude = float(int((2 ** (sampwidth * 8)) / 2) - 1)

freq = 1200
cycle = framerate / freq
duration = 0.05

data = ''

for l in range(int(nr)):
    wordlength = len(words[l])
    for wo in range(int(wordlength)):
        for i in range(int(duration * framerate)):
            value = int(nr*math.sin(l*freq*math.pi*float(framerate)/float(i + 1)))
            data = struct.pack('<h', value)
            w.writeframesraw( data )
    if l%300 == 0:
        print str(l) + '/'+str(nr)+' Adding noise. Please wait.'
    elif l == (nr - 1):
        print 'Done. Enjoy.'

w.close()