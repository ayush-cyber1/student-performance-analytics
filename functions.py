import numpy as np
import pandas as pd

SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer"]
PASS_MARKS = 40
MIN_ATTENDANCE = 75


def load_data(file_name):
    """Read the student CSV file and return a DataFrame."""
    return pd.read_csv(file_name)


def calculate_total_and_average(df):
    """Add Total and Average columns using NumPy."""
    marks = df[SUBJECTS].to_numpy()
    df["Total"] = np.sum(marks, axis=1)
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df


def get_grade(average):
    """Grading rule: 90+ A+, 80+ A, 70+ B, 60+ C, 50+ D, 40+ E, else F."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def assign_grades(df):
    """Loop through every average and store the grade."""
    grades = []
    for avg in df["Average"]:
        grades.append(get_grade(avg))
    df["Grade"] = grades
    return df


def get_result(row):
    """A student passes only if every subject has at least 40 marks."""
    for subject in SUBJECTS:
        if row[subject] < PASS_MARKS:
            return "Fail"
    return "Pass"


def assign_results(df):
    """Loop through every student and store Pass or Fail."""
    results = []
    for index, row in df.iterrows():
        results.append(get_result(row))
    df["Result"] = results
    return df


def attendance_status(df):
    """Mark students whose attendance is below the minimum."""
    df["Attendance_Status"] = np.where(df["Attendance"] >= MIN_ATTENDANCE, "OK", "Shortage")
    return df


def subject_analysis(df):
    """Average, highest, lowest and pass count for each subject."""
    data = []
    for subject in SUBJECTS:
        column = df[subject].to_numpy()
        data.append({
            "Subject": subject,
            "Average": round(float(np.mean(column)), 2),
            "Highest": int(np.max(column)),
            "Lowest": int(np.min(column)),
            "Passed": int(np.sum(column >= PASS_MARKS)),
            "Failed": int(np.sum(column < PASS_MARKS)),
        })
    return pd.DataFrame(data)


def department_analysis(df):
    """Average marks, attendance and pass count for each department."""
    summary = df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Average_Marks=("Average", "mean"),
        Average_Attendance=("Attendance", "mean"),
    )
    summary["Passed"] = df[df["Result"] == "Pass"].groupby("Department")["Student_ID"].count()
    summary = summary.fillna(0).round(2).reset_index()
    return summary


def grade_distribution(df):
    """Count of students in each grade."""
    order = ["A+", "A", "B", "C", "D", "E", "F"]
    counts = df["Grade"].value_counts()
    data = []
    for grade in order:
        data.append({"Grade": grade, "Students": int(counts.get(grade, 0))})
    return pd.DataFrame(data)


def top_performers(df, n=5):
    """Return the top n students by average marks."""
    top = df.sort_values(by="Average", ascending=False).head(n)
    return top[["Student_ID", "Name", "Department", "Total", "Average", "Grade"]]


def class_summary(df):
    """Overall class numbers in a dictionary."""
    averages = df["Average"].to_numpy()
    best = df.loc[df["Average"].idxmax()]
    worst = df.loc[df["Average"].idxmin()]
    passed = int(np.sum(df["Result"] == "Pass"))
    total = len(df)
    return {
        "total_students": total,
        "class_average": round(float(np.mean(averages)), 2),
        "highest_average": float(np.max(averages)),
        "lowest_average": float(np.min(averages)),
        "best_student": best["Name"],
        "weakest_student": worst["Name"],
        "passed": passed,
        "failed": total - passed,
        "pass_percentage": round(passed / total * 100, 2),
        "attendance_shortage": int(np.sum(df["Attendance"] < MIN_ATTENDANCE)),
    }
