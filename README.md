# Web notebook

aim for this project is to create a web based note book that allows taking notes -> searching key concept easily

planned further features is to make it into THE ultimate text editor

## execution plan

### front end

static navigation bar left

navbar with 

	- search (real time search)
	- new post

dynamic content right

live tiles

	- if no content just show random boxes
	- upon searches will run regex to retrieve boxes to show
	- with enter hit will show the final search
	- if valid also shows related boxes
	- allow delete/modification (implement later)

new post

	- keyword column
	- text box with word limitation
	- implement a real time word count (with JS?)
	- tags
	- post

### back end

new post

	- text analysis
	- label and save to csv

get random text for live tiles

	- generate random value and pull rows accordingly from csv
	- end game to have some algorithm to determine user preference/ interest

post modification

	- allow delete/modification (implement later)


### expected dependencies

	- pandas
	- os
	- js
	- auth?