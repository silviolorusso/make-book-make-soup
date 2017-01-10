# Makefile for INC/PublishingLab hybrid publications

alldocx=$(wildcard docx/*.docx) # select all docx
allmarkdown=$(filter-out md/book.md, $(shell ls md/*.md)) # select all markdown
icmls=$(wildcard icml/*.icml) # select all icml

# just a test
test: $(allmarkdown)
<<<<<<< HEAD
	@echo "Markdown files:" ;
=======
	@echo "Markdown files:" ;
>>>>>>> 591dbd523711175bbf04d9826b13b75d1d48786c
	@echo $(allmarkdown)


# create the necessary folders
folders:
	mkdir docx/ ; \
	mkdir md/ ; \
	mkdir md/imgs/ ; \
	mkdir icml/ ; \
	mkdir lib/ ; \
	mkdir scribus_html/ ;
	mkdir txt/
	mkdir html/
	touch html/preview.html;


# convert docx to md
markdowns: $(alldocx)
	for i in $(alldocx) ; \
	do md=md/`basename $$i .docx`.md ; \
	echo "File" $$i $$md ; \
	pandoc $$i \
	       	--from=docx \
		--to=markdown \
	       	--atx-headers \
		--template=essay.md.template \
		-o $$md ; \
	./scripts/md_unique_footnotes.py $$md ; \
	done


icmls: $(allmarkdown)
	cd md && for i in $(allmarkdown) ; \
	do icml=icml/`basename $$i .md`.icml ; \
	pandoc ../$$i \
		--from=markdown \
		--to=icml \
		--self-contained \
		-o ../$$icml ; \
	done
	cd icml && sed -i -e 's/file\:imgs/file\:\.\.\/md\/imgs/g' *.icml ; # change links of images


scribus: $(allmarkdown)
	for i in $(allmarkdown) ; \
	do html=`basename $$i .md`.html ; \
	./scripts/md_stripmetada.py $$i > md/tmp.md ; \
	pandoc md/tmp.md \
		--from=markdown \
		--to=html5 \
		--template=scribus.html.template \
		-o scribus_html/$$html ; \
	done


book.md: clean $(allmarkdown)
	for i in $(allmarkdown) ; \
	do ./scripts/md_stripmetada.py $$i >> md/book.md ; \
	done


epub: clean $(allmarkdown) book.md
	cd md && pandoc \
		--from markdown \
		--to epub3 \
		--self-contained \
		--epub-chapter-level=1 \
		--epub-stylesheet=../css/styles.epub.css \
		--epub-cover-image=../epub/cover.jpg \
		--epub-metadata=../epub/metadata.xml \
		--default-image-extension png \
		--toc-depth=6 \
		-o ../book.epub \
		book.md ; \
# include line, if you wanto embed font:
#		--epub-embed-font=../lib/UbuntuMono-B.ttf \

# use this to test the design without having to compile the EPUB
html: clean $(allmarkdown) book.md
	cd html && pandoc \
		--from markdown \
		--to html \
		-s \
		-c ../css/styles.epub.css \
		-o book.html \
		../md/book.md ;
	cd html && sed -i -e 's/src="imgs/src="..\/md\/imgs/g' book.html ; # change links of images


# remove outputs
clean:
	rm -f md/book.md
	rm -f book.epub
	rm -f *~ */*~  # emacs files


# Thomas Walskaar 2016 www.walska.com
floppy: clean $(allmarkdown) book.md
	cd txt && pandoc \
		--from markdown \
		--to plain \
		-s \
		-o book.txt \
		../md/book.md ; \
	rm /Volumes/FLOPPY/* ; \ # location of the floppy device
	python ../scripts/floppynetwork.py book.txt /Volumes/FLOPPY

# Sentiment analysis
# Nicoleta Pana &&&& Luca Claessens
# needs NLTK to run (pip install nltk)
# download the vader lexicon and punkt tokenizer (in python, import nltk and run nltk.download())
sentiment:
	python scripts/sentiment.py txt/.txt ;

# Dylan Degeling, Lucia Dossin, Margreet Riphagen
noise:
	@echo 'Making some noise now. This might take a while.'
	@python scripts/make_noise.py

# Make Square (Thomas Walskaar & Fabiola Fortuna)
# Covert all of whitespaces into black squares and all of the text and symbols into whitespaces
square: clean $(allmarkdown) book.md
	cd txt && pandoc \
		--from markdown \
		--to plain \
		-s \
		-o book.txt \
		../md/book.md ; \
	mkdir -p ../square
	python scripts/square.py txt/book.txt > square/square.txt
