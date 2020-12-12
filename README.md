# LyricsSolitaire

### Author: He Haolan

The project for final assignment of 2020 Sept term HASS, The Traditional Chinese Lyrics

a script that takes in a line of Chinese traditional lyrics as input and gives output in a Solitaire style, requires Python run time environment.

## Sample outputs

[image1](assets/sample1.jpg)

[image2](assets/sample2.jpg)

## The Benefits

- Enable people of obtaining more knowledge of lyrics based on their existing scope of view, cultivating their accumulation of knowledge
- Fun to play with, making people more interested in learning Chinese traditional lyrics

## How it works

- use python request module for crawling data from https://so.gushiwen.org, generating a text file contains all the lyrics.
- use bash for formatting and splitting multiple sentence in a line
	- `sed -i 's/？/。/g' poem.txt`
	- `sed -i 's/！/。/g' poem.txt`
	- `sed -i 's/。/\n/g' poem.txt`
- use xpinyin and pickle module for creating a dictionary object with the pinyin of the first word as key and the line as value
- use pickle module for accessing the dictionary and gives out corresponding output to the input