# Student Performance Analytics System

A simple Python project that reads student data from a CSV file, analyzes it using NumPy and Pandas, and shows the results in the terminal, in a Jupyter Notebook, and on a live website.

## Live Demo
https://ayush-cyber1.github.io/student-performance-analytics/

## Technology Used
- Python
- NumPy
- Pandas
- Matplotlib (only for charts in the notebook)

## Project Files
| File | Purpose |
|------|---------|
| main.py | Runs the project, prints the analysis, creates results.csv and the web page |
| functions.py | Reusable functions for calculations and processing |
| report.py | Functions that build the HTML result page |
| Student_Performance_Analysis.ipynb | Jupyter Notebook with step-by-step analysis and charts |
| students.csv | Dataset with 60 student records |
| results.csv | Output file with Total, Average, Grade, Result |
| docs/index.html | Live result page (published with GitHub Pages) |
| requirements.txt | Libraries needed |

## Dataset Columns
Student_ID, Name, Department, Maths, Physics, Chemistry, English, Computer, Attendance

## Rules Used
**Grading (based on average marks)**

| Average | Grade |
|---------|-------|
| 90 and above | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 50 - 59 | D |
| 40 - 49 | E |
| below 40 | F |

**Pass / Fail:** A student passes only if they score at least 40 in every subject.

**Attendance:** Below 75% is marked as Shortage.

## What the Project Does
1. Loads the CSV file using Pandas
2. Calculates total and average marks for each student using NumPy
3. Assigns grades and Pass/Fail using loops and functions
4. Finds highest, lowest and average performance of the class
5. Shows subject-wise and department-wise analysis
6. Shows grade distribution and top 5 students
7. Lists failed students
8. Saves results.csv and creates the web page docs/index.html

## How to Run
```
pip install -r requirements.txt
python main.py
```
To open the notebook:
```
jupyter notebook Student_Performance_Analysis.ipynb
```

## Sample Findings
- Total students: 60
- Class average: 62.5
- Pass percentage: 80%
- Best subject: Computer
- Top student: Aarav Sharma (CSE) with 92.4 average

## Concepts Used
Variables, data types, loops, functions, conditions, NumPy arrays and operations, Pandas DataFrame, filtering, groupby, sorting.
