# Python Project: &nbsp;Py Me Up, Charlie

## Background

Welcome to the world of programming with Python. &nbsp;In this project, we will be using Python to complete **two** Python analyses: &nbsp;PyBank and PyPoll.

Both of these challenges encompass a real-world situation where Python scripting skills can come in handy.

## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this challenge, we are tasked with creating a Python script for analyzing the financial records of your company. &nbsp;We will create a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). &nbsp;The dataset is composed of two columns: &nbsp;`Date` and `Profit/Losses`.

* The task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset.

  * The net total amount of "Profit/Losses" over the entire period.

  * The changes in "Profit/Losses" over the entire period, and the average of those changes.

  * The greatest increase in profits (date and amount) over the entire period.

  * The greatest decrease in losses (date and amount) over the entire period.

* As an example, the analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, the final script should both print the analysis to the terminal and export a text file with the results.

## PyPoll

![Vote Counting](Images/Vote_counting.png)

* In this challenge, we are tasked with helping a small, rural town modernize its vote counting process.

* We were given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). &nbsp;The dataset is composed of three columns: &nbsp;`Voter ID`, `County`, and `Candidate`. &nbsp;The task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast.

  * A complete list of candidates who received votes.

  * The percentage of votes each candidate won.

  * The total number of votes each candidate won.

  * The winner of the election based on popular vote.

* As an example, the analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, the final script should both print the analysis to the terminal and export a text file with the results.
