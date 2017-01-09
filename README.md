	  ,__ __    ___,  ,      ___    , __   __    __   ,       
	 /|  |  |  /   | /|   / / (_)  /|/  \ /\_\/ /\_\//|   /   
	  |  |  | |    |  |__/  \__     | __/|    ||    | |__/    
	  |  |  | |    |  | \   /       |   \|    ||    | | \     
	  |  |  |_/\__/\_/|  \_/\___/   |(__/ \__/  \__/  |  \_/  
	  ,__ __    ___,  ,      ___          __   _        , __  
	 /|  |  |  /   | /|   / / (_)    ()  /\_\/(_|    | /|/  \ 
	  |  |  | |    |  |__/  \__      /\ |    |  |    |  |___/ 
	  |  |  | |    |  | \   /       /  \|    |  |    |  |     
	  |  |  |_/\__/\_/|  \_/\___/  /(__/ \__/    \__/\_/|     
	                                                          
	                                                         
A Workshop on Speculative Workflows

Conceived by [Silvio Lorusso](http://silviolorusso.com) / [PublishingLab](http://www.publishinglab.nl/)

---

Labeled COPE (Create Once, Publish Everyhwere), single-source publishing, multi-channel publishing, etc, the possibility of automagically converting a single manuscript to every possible format has been the Holy Grail of the publishing industry for quite some time. 


	                /||\
	                ||||
	                ||||
	                |||| /|\
	           /|\  |||| |||
	           |||  |||| |||
	           |||  |||| |||
	           |||  |||| d||
	           |||  |||||||/
	           ||b._||||~~'
	           \||||||||
	            `~~~||||
	                ||||
	                ||||
	~~~~~~~~~~~~~~~~||||~~~~~~~~~~~~~~
	  \/..__..--  . |||| \/  .  ..
	\/         \/ \/    \/
	        .  \/              \/    .
	. \/             .   \/     .
	   __...--..__..__       .     \/
	\/  .   .    \/     \/    __..--..


But this very possibility hasn't been explored from an imaginative and speculative perspective. Generally speaking, the formats resulting from single-source publishing often belong to a traditional idea of publication that doesn't take advantage of algorithmic^ filtering.  

The aim of this workshop is to imagine formats that overcome what is generally understood as publication. What kind of publications can we think of, besides EPUBs, PDF, HTML? How can these be automatically dissected, remixed or expanded?  

Employing a markdown-oriented workflow that includes the use of Make and Pandoc, we will convert/transform/filter/expand/dissect Kafka's *The Trial*.^^

^ Don't be scared, by algorithm I simply mean ["a set of rules for solving a problem in a finite number of steps"](http://www.dictionary.com/browse/algorithm).

^^ You might wonder why I chose *The Trial* for this workshop... The first reason is that is one of the few books I've found already formatted in markdown and the second reason is that it seems fitting this idea of ramificated process.      

## What Are You Looking at

	      __...--~~~~~-._   _.-~~~~~--...__
	    //               `V'               \\ 
	   //                 |                 \\ 
	  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
	 //__.....----~~~~._\ | /_.~~~~----.....__\\
	====================\\|//====================
	                dwb `---`  

This repository consists of a collection of resources aimed at the development hybrid publications, in both reflowable format (EPUB3) and *fixed layout* (Scribus and inDesign structured content). The resources propose a workflow based on the conversion between markup languages, using [Pandoc]() and [Markdown]() source-files as its essential elements. Most of the ideas materialized in this collections of resources originated from the research developed by the [Digital Publishing Toolkit](http://networkcultures.org/digitalpublishing/) consortium, especially with the contributions from [Michael Murtaugh](http://automatist.org/) and later with andre further development by [André Castro](http://www.andrecastro.info/a/).

The repository also includes a markdown version of *The Trial* by Franz Kafka found [here](https://github.com/worldclassics/the-trial). 

## Ok, Let's Start

	              \\\\
	              \c .(
	               \ _/
	            ___/(  /(
	           /--/ \\//
	       __ )/ /\/ \/
	      `-.\  //\\
	         \\//  \\
	          \/    \\
	                 \\
	  jgs            '--`


- Install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Install [Pandoc](http://pandoc.org/installing.html) (You can check if it's installed by run `pandoc -v` in the terminal. If you don't get errors, Pandoc is working)
- Create an account on [GitHub](https://github.com/)
- Shout your username so that I can add you to the repo
- Clone this repo by running on the terminal:

`git clone https://github.com/silviolorusso/make-book-make-soup`

and then:

`cd make-book-make-soup`

With these commands you will download all the files included in this repo.

- Form a group of 3/4 people

### What Do I Do with All These Files??

	                             ____
	                     __,-~~/~    `---.
	                   _/_,---(      ,    )
	               __ /        <    /   )  \___
	- ------===;;;'====------------------===;;;===----- -  -
	                  \/  ~"~"~"~"~"~\~"~)~"/
	                  (_ (   \  (     >    \)
	                   \_( _ <         >_>'
	                      ~ `-i' ::>|--"
	                          I;|.|.|
	                         <|i::|i|`.
	                        (` ^'"`-' ")
	------------------------------------------------------------------
	Nuclear Explosion Mushroom.  by Bill March

The brain of this workflow is a file called `makefile`. Make gets its knowledge of how to do stuff from the `makefile`, which in turn includes *rules*.  

Our `makefile` includes rules to create markdown files from docx files, EPUB files from markdown files, etc. Let's have a look at one *rule*:

	test: $(allmarkdown)
		@echo "Markdown files:" ; 
		@echo $(allmarkdown)

This *rule*, named "test" will just output the variable `$(allmarkdown)` which contains all our markdown files. Let's try it out.

In the Terminal, simply write `makefile test`. The names of our mardown files should now appear:

	Markdown files:
	md/01.md md/02.md md/03.md md/04.md md/05.md md/06.md md/07.md md/08.md md/09.md md/10.md 

Feel free to try other rules that you find in the `makefile`!

A detailed explanation of how to use this repostory can be found on wiki [wiki/From-Manuscript-to-EPUB](https://github.com/DigitalPublishingToolkit/Hybrid-Publishing-Resources/wiki/From-Manuscript-to-EPUB).

### Our Makefile, My Rules

	                              _
	                           _ooOoo_
	                          o8888888o
	                          88" . "88
	                          (| -_- |)
	                          O\  =  /O
	                       ____/`---'\____
	                     .'  \\|     |//  `.
	                    /  \\|||  :  |||//  \
	                   /  _||||| -:- |||||_  \
	                   |   | \\\  -  /'| |   |
	                   | \_|  `\`---'//  |_/ |
	                   \  .-\__ `-. -'__/-.  /
	                 ___`. .'  /--.--\  `. .'___
	              ."" '<  `.___\_<|>_/___.' _> \"".
	             | | :  `- \`. ;`. _/; .'/ /  .' ; |
	             \  \ `-.   \_\_`. _.'_/_/  -' _.' /
	   ===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
	                           `=--=-'                    hjw

Now that we know how a *rule* is structured is time to create our own. But first we need to have an idea of what the possibilities are and what we want to do.

I'd suggest to think of a *rule* as a filter, a machine that takes content as its input, does something to that input, and then outputs the transformed input. Furthermore, you could think of a *rule* as a delivery service. A service take takes your content, somehow repackages it, and delivers it to different places/people. Here's some kinda trivial (and not so crazy) ideas for new *rules*:

	make italian	add an automatic translator to the workflow
	make short		only highlight the important passages of a book
	make biblio		download all the books in your book's bibliography
	make new		generate new text from your book through a neural network 
	make ppl		extract a list of names from your book	

I think a good hint into what it means to think speculatively about automated publishing workflows is the `make floppy` rule created by Thomas Walskaar. This rule simply converts our book into plain text and upload it into a floppy disk. This simple rule imaginatively subverts the narrative of technological progress that normally drives the discourse in the e-publishing field. Let's see how it works:

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

First, some cleanup is done on the source files, then Pandoc converts our markdown book into txt, every file is deleted from the floppy disk, and finally a Python script (`/scripts/floppynetwork.py`) is launched. This script echoes some ASCII art in the Terminal and then moves the txt file to the floppy. 

Now it's your turn:

- take some time to discuss about some new rules
- discuss your ideas with other groups
- develop your rules of choice

### Cookbook Time

	                    ________
	                 .##@@&&&@@##.
	              ,##@&::%&&%%::&@##.
	             #@&:%%000000000%%:&@#
	           #@&:%00'         '00%:&@#
	          #@&:%0'             '0%:&@#
	         #@&:%0                 0%:&@#
	        #@&:%0                   0%:&@#
	        #@&:%0                   0%:&@#
	        "" ' "                   " ' ""
	      _oOoOoOo_                   .-.-.
	     (oOoOoOoOo)                 (  :  )
	      )`"""""`(                .-.`. .'.-.
	     /         \              (_  '.Y.'  _)
	    | #         |             (   .'|'.   )
	    \           /              '-'  |  '-'
	jgs  `=========`

Now that you have your rules working, it's time to bring them together in the remote `makefile`. To do this, add your new and modified files to the staging area:

	git add -A .

Commit your changes:

	git commit -m "My new rule!"

Push them to the remote repository:

	git push

Remember to include your names and a decription of the rule as a comment.

**There will be conflicts**, but don't worry, we're gonna solve them one by one.

### What Now?

	                                                _.........._
	                                              ,'            `.
	                                              |`-==========-'|
	                                             /                \
	                                             \    ________    /
	                                              |,-'        `-.|
	                              _               |`-.________.-'|
	                       ____,-' `-.            |  :       :   |
	                    _.' .--.\.    \           |    : :  .    |
	                 _.' `-.`--'  `.   \          |:  : :  :  .  |
	                /       \ `.-' /`-. `-.       |      : '     |
	 ==============/`-.      `-.` /.-' `.  \======|    : : . :   |========
	              _\   \        `-. \.-' \.' hjw  |     :        |
	       ____ .' \,-. `.         `.\.-'         \       :      /
	      /  .-`--./   \  \     ___.'              `._:______'_.'
	    ,-`-/  ___/__._'   /_.-'
	   (  .-`-(__ /  `.`-''
	    `/   |/  `|    |
	     `--' \   \    |
	           `--'`._.'

Thanks to all the participants! Hope you enjoyed :)

---

### 9th of January, 2017

	       .-""""-.        .-""""-.
	      /        \      /        \
	     /_        _\    /_        _\
	    // \      / \\  // \      / \\
	    |\__\    /__/|  |\__\    /__/|
	     \    ||    /    \    ||    /
	      \        /      \        /
	       \  __  /        \  __  / 
	        '.__.'          '.__.'
	         |  |            |  |
	jgs      |  |            |  |

#### Participants

- Luca Classaens
- Dylan Degeling
- Lucia Dossin
- Fabiola Fortuna
- Nicoleta Pana
- Margreet Riphagen
- Thomas Walskaar



#### Ideas for a Recipe

- make `mood`: sentiment analysis on the text made into a series of data visualizations and maybe shown together with motivational quotes
- make `vip`: replace sentences with famous people's tweets
- make `meme`: select meme-worthy sentences to create memes
- make `lazy`: summarize the book with images only
- make `scrambledegg`: randomly scrambling the text
- make `blackbar`: replace all spaces with black bars
- make `nokia`: publish the book for old nokia phones
- make `tei`: play with [TEI](http://www.tei-c.org/) format
- make `poster`: extract data from text and format it as a minimalistic poster
- make `skills`: produce a 3d shape expressing metrics like word frequency, etc.
- make `summary`: summarize the book in some meaningful way
- make `soundtrack`: compose an audio soundtrack for the book    

---

- add description of new rules 

---

License: [GPL3](http://www.gnu.org/copyleft/gpl.html)

The greater part of this framework was developed as part of the [Digital Publishing Toolkit](http://digitalpublishingtoolkit.org) by Michael Murtaugh with the support of [Institute for Network Cultures](http://networkcultures.org)
and [Creating 010](http://creating010.com), and further developed by André Castro.

Silvio Lorusso 2017

---