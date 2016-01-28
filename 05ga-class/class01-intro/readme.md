# Class 1 - Intro

### TODO
Write skills, category belonged, and category target re: https://www.oreilly.com/ideas/analyzing-the-analyzers

## Logistics
Class 7 -> Ready at 530~

**People**
- Vanessa Ohta - Producer at GA
- Hamed Hasheminia - Instructor (prof, Canadian context)
- Michael Twardos - TA (Director of DS at Optimize.ly)

**Details**
- No Class - Monday Feb 15 
- Apr 6 last class


**Philosophy**
- Adjustable pace
- Interactive
- Learn how to learn
- Learn by teaching

**Projects:**
Learn by doing
- In-class examples
- Assignments
- - Ideally do the thing you're not doing.
- - Policy -> Prediction, or vic a versa 
- Projects are key
- Practice, Practice -> Understand the models fundamentally
- Extensive use of visuals -> Teach the algos w/ visuals

**Success**
- Questions, etc.
- Teach classmates -> Premise of you only know if you can teach

**Typical class**
- Review of previous matterials
- Theory -> PPT slides
- Lab/Code walkthrough
- in-class exercises
- homework assigned

**Ga Grad reqs**
- 80% of homework and labs
- Attendence (miss no more than 2 classes) -> 4?


**Agenda**
- What is Data Sci
- What roles exist in data sci
- What tools and approaches do data sci use to analyze data

**Lab**
- Command line
- Set up github
- intro python

## 1: What is Data Sci
Statistics, computation, and storytelling
How do you tell a story with data?
- "analysis of data using the scientific method (it may be the most overused term of the year, but you're ulikely to have a meeting where the topic odesn't come up)" [Shelly Palmer]

Without the storytelling side, you're screwed: Venn diagram (Stat/Comp/Knowledge)

Interdisciplinary, problem-solving oriented subject

- "Data scientist is a data analyst who lives in california"
- "Data scientist is someone who is better at statistics than any software engineer, and better at software engineering than a statistician"
- "Data scientist is a business analyst who lives in New York"
- "Data scientist is a statistician who lives in SF"
- "Statistics on a mac"

Data scientist is that unique blend of skills that can unlock the insights of data and tell a fantastic story via the data

Engineering skills to acquire and manage large data sets, and statistician skills to extract value from large data sets and present that data to a large audience - John Rauser

- Mentions: https://www.oreilly.com/ideas/analyzing-the-analyzers
- x: Data Businessperson, Data Creative, Data Developer, Data Researcher
- y: Business, ML/BigData,Math/OR,Programming

### Question of how you identify as a designer
![Who are you](https://d3ansictanv2wj.cloudfront.net/images/3-SkillsSelfDMosaic-2-6c755564.png)

### Volume of data used

![Volume](https://d3ansictanv2wj.cloudfront.net/images/atan_03in04-42d954c4.png)

We can collect terrabytes of data, but we may only be working on a subset of that

### T-shaped data scientist

![T shaped](https://d3ansictanv2wj.cloudfront.net/images/atan_04in01-be7264b9.png)

Data business person -> Make the story your focus
- Economists are the best storytellers
- - Eg, Economists
![Areas to focus](https://d3ansictanv2wj.cloudfront.net/images/atan_04in02-50296475.png)


### Overview of Data Workflow

#### 1) Identify the problem
- Identify the biz product objectives
- Identify and hypothesize goals andd criteria for success
- Create a set of questions for identifying correct data sets
- - What would be the best data needed? Sure, I can get ttransaction data, but as important as transaction data are the searches that didn't end in a purchase

#### 2) Acquire the data
- Identify the right data sets
- Import data and set up local/remote data structure
- determine most approp tool to work with data

#### 3) Parse the data
- Read any documentation provided
- - Understand the columns
- Perform exploratory data analysis
- - Draw simple graphs
- Verify the quality of the data

#### 4) Mine the data
- Determine sampling methodology and sample data
- - Create Test vs. Data sets. eg. Splitting the data so you don't overfit
- Format, clean, slice, and combine data in python
- Create necessary derived columsn from the data (new data)

#### 5) Refine the data
- Identify trends and outliers
- - Understanding when to cut outliers to prevent setting off regression analysis
- Apply descriptive and inferential statistics
- document and transform data
- - Manipulating the data where important

#### 6) Build a data model
- Select appropriate model
- - You can only know the approp model when you know the full dataset
- build model
- evaluate and refine model
- - At least use two or three models in the dataset for the final project. Explore multiple models!

#### 7) present the results
- Summarize findings with narrative, storytelling techniques
- - People with the best stories are the ones who really succeed
- - Dangerous if you work with something you don't have domain knowledge in. You need to udnerstand
- Present limitations and assumptions of analysis
- Identify follow up problems and questions for future analysis