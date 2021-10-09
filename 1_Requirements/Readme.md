# Introduction
A learner’s performance is measured in terms of his/her marks. It is one of the indicators of a learner’s progress.This application helps to monitor the learning progress in a very clear and informative manner. The analysis and visualization of the data helps to understand the performance of all with respect to each course and overall in a better way. The application provides a detailed sheet containing the total, percentages, and grades of all learners. It also provides various options to users to get the deatils of the learners like getting details of learners with scope of improvement, to search for a particular learner and so on. 

# Research
* Data consolidation is the process where all the datas from the organization is integrated in one place.
* The consolidation of data is an important step for data management process and integration. This makes the information of data to be available quickly and easily, also this increases productivity and efficiency by having all datas in one place.
* The consolidation of data allows us to gather the datas from different worksheets to a master worksheet and vice versa. 
* The excel consolidate function allows us to select datas from the various locations and creating a table which summarizes the information for you.

# Requirements

## Cost and Features

| Solution | Time | Cost | Feature | Difference |
| --- | :---: | :---: | --- | --- |
| Manual calculations | Available since very long time | Time consumption | Can be done using only pen-paper | Our system is automatic, time efficient & accurate |
| Spreadsheet softwares (MS Excel, Libre Calc) | Available since long time | Paid/Free | Pleathora of features | For specific task, they are only semi-automatic while our system is automatic |
| Web-applications (doodu.io, data analysis) | Fairly latest | Paid/Free | High availability (on every platform) | Takes more time then our system. Not suitable for large data |
| Various template excel files | Came out after spreadsheet softwares | Mostly free | Pre-formatted, Automatically updates with data | Only pre-defined amount of data can be analyzed |
| Data analysis libraries for python (like pandas) | Since last decade | Free | Large number of analysis tools | Requires more learning to use, while our system requires almost no learning |


# Detail requirements
## High Level Requirements
| ID | Description | Category | Status |
| ----- | ----- | ------- | --------- |
| HLR01 | Data validation | Technical | Implemented |
| HLR02 | Working with excel files | Requirement | Implemented |
| HLR03 | Data analysis | Process | Implemented |
| HLR04 | Visualization of data | Requirement | Implemented |
| HLR05 | User interface | Requirement | Implemented |


##  Low level Requirements
| ID | Description | HLR ID | Status |
| ------ | --------- | ------ |------- |
| LLR01 | Find the missing rows(entries) | HLR01 | Implemented |
| LLR02 | A row in input sheet must contain data of all fields/columns | HLR01 | Implemented |
| LLR03 | Marks should only be number(no alphabets) | HLR01 | Implemented |
| LLR04 | Marks should only be positive & less then defined maximum marks | HLR01 | Implemented |
| LLR05 | Reading data from the excel sheet | HLR02 | Implemented |
| LLR06 | Writing data into the excel sheet| HLR02 | Implemented | 
| LLR07 | Finding average for overall & each courses | HLR03 | Implemented |
| LLR08 | Finding Total & percentage for overall program | HLR03 | Implemented |
| LLR09 | Relative grading of the students based on performance (overall)| HLR03 | Implemented |
| LLR10 | Defining criteria for pass/fail | HLR03 | Implemented |
| LLR11 | Identifying & highlighting students with scope of improvements (overall & each courses) | HLR03 | Implemented |
| LLR12 | Displaying top performers for overall program & each courses | HLR03 | Implemented |
| LLR13 | Generating the bell curve based on data analysis (overall & each) | HLR04 | Implemented |
| LLR14 | Generating the pie chart based on grades (overall & each) | HLR04 | Implemented |
| LLR15 | Generating the bar chart based on percentage (overall) | HLR04 | Implemented |
| LLR16 | Options to search for info of a particular employee | HLR05 | Implemented |
| LLR17 | Functions to display user interface requirements | HLR05 | Implemented |



# 4 W's & 1 H

## WHO?

* Any faculty member who wants to generate the performance reports of his/her students.
* Any faculty who wishes to analyse and visualize the performance of the students in an organized manner.
* Any member of the faculty who would like to generate an accurate grade for all students in any subject.
* 
## WHAT?

* A utility that automates the analysis and visualization of the marks/results obtained by students and generate the respective grade for different subjects , statistics and performance reports.
* 
## WHEN?

* Whenever a faculty/teacher would like to generate performance reports, grades and statistics of the students' performance automatically without any stress and wastage of time
* When manual generation of the report, feedback and grades becomes tedious
* 
## WHERE?

* This utility is computer based and is compatible with python environment and can be accessed anywhere through your laptop/desktop.
* 
## HOW?

* Reflecting on how tiresome and time consuming it can be to manually analyse all the students' data, generate grades and reports and how we can provide a platform that can automate this task and help our faculty members.
* 
## SWOT analysis

![swotanalysis](https://user-images.githubusercontent.com/86735554/124467054-f63d5b00-ddb4-11eb-8f71-e674c3411828.png)

| Strengths | Weaknesses | Opportunities | Threats |
|-----------|------------|---------------|---------|
|1. Data analysis is automated|No Graphical user interface|Can include Graphical user interface|Not very visually pleasing since there is no GUI|
|2. Data Visualization is automated|Processes limited number of excel sheets|Can be scaled to multiple sheets/subjects|Generates reports for fixed number of subjects|
|3. Very time efficient|Does not provide individual reports for each student|Can generate report for each student|---------|
|4. Reduces faculty work load|------------|---------------|---------|
|5. User Friendly|------------|---------------|---------|
|6. Provides report for each subject|------------|---------------|---------|

