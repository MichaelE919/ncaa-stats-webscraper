# NCAA Basketball Stats Webscrapper
> Collects team stats for the top 68 NCAA basketball teams and writes them to a preformatted Excel spreadsheet.

This Python script uses the Request and Beautiful Soup libraries to collect team stats from teamrankings.com and kenpom.com and creates a series of lists and dictionaries to contain the information.
With the help of the Pandas and Openpyxl libraries, the various team stats are written to a preformatted Excel spreadsheet.

![](header.png)

## Background

This was the first Python project I worked on by myself after taking an online course and reading numerous articles and tutorials. For a couple of years, I used the Excel spreadsheet to determine my March Madness picks, but I *scraped* the data myself. It took hours (lots of hours), and eventually I thought, "There has to be a better way."
I credit most of the inspiration for this project to Al Sweigart's book [Automate the Boring Stuff with Python](http://automatetheboringstuff.com/). There is one chapter on webscraping and another working with Excel spreasheets, and I was able to put that information to use to create this Python script.

## The Four Factors

If your are a basketball stats nerd, you may have heard this term. I read about this in an article, and I used it as a baseline for determining which team would win a particular matchup. The [Four Factors](https://www.nbastuffer.com/analytics101/four-factors/) are metrics that correlate with winning basketball games, and are comprised of the following stats: Effective Field Goal Percentage, Turnover Rate, Offensive Rebounding Percentage, and Free Throw Rate. These stats have become popular in predicting NBA and NCAA basketball games.

## Usage

Clone or download the repository to your machine, change into the newly created directory, then run the script. Python takes care of the rest. (Almost, as I'll point out in a but.)

```sh
git clone https://github.com/MichaelE919/ncaa-stats-webscrapper.git
cd ncaa-stats-webscrapper
python get_stats.py
```
The script will create a NCAA Bracket Spreadsheet-final.xlsx. Use this to make your picks. While the new spreadsheet now contains all the necessary stats for the 68 teams in the tournament, you must still create "bracket" manually by copying and pasting the rows for each team from the Provided Ranking tab to the First Four and Round of 64 tabs. A series of IF formulas populates the rest of the tabs and gives you the winner for each matchup including the championship game. 
Basically, the IF formulas compare the values for each of the stats. Whichever team has the better value wins that stat, and whichever team wins the most stats, wins the matchup.

## Meta

Michael Eichenberger – [@michaele919](https://twitter.com/michaele919) – mikeetpt@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/michaele919/github-link](https://github.com/michaele919/)

## Next Steps

At some point in the future, I'd like to make this script better by doing the following things:

1. There are *a lot* of for loops. I'd like to speed them up by converting them to list comprehensions
2. There are hard-coded elements that I'd like to replace with reusable code, if possible.
3. Automate the manual work required in the Excel spreadsheet. As I said before I started this thing, "There's got to be a better way!"

If anyone would like to take these on, please do so and create a pull request. I would love some feedback!
