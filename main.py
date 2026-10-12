import functions as fn
import report


def print_title(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main():
    df = fn.load_data("students.csv")

    print_title("STEP 1: DATASET INFORMATION")
    print("Number of records :", len(df))
    print("Number of columns :", len(df.columns))
    print("Column names      :", list(df.columns))
    print()
    print(df.head())
    print()
    print("Missing values in dataset:", int(df.isnull().sum().sum()))

    df = fn.calculate_total_and_average(df)
    df = fn.assign_grades(df)
    df = fn.assign_results(df)
    df = fn.attendance_status(df)

    print_title("STEP 2: PROCESSED DATA (first 10 students)")
    print(df[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]].head(10).to_string(index=False))

    summary = fn.class_summary(df)

    print_title("STEP 3: CLASS SUMMARY")
    print("Total students      :", summary["total_students"])
    print("Class average       :", summary["class_average"])
    print("Highest average     :", summary["highest_average"], "-", summary["best_student"])
    print("Lowest average      :", summary["lowest_average"], "-", summary["weakest_student"])
    print("Students passed     :", summary["passed"])
    print("Students failed     :", summary["failed"])
    print("Pass percentage     :", summary["pass_percentage"], "%")
    print("Attendance shortage :", summary["attendance_shortage"], "students below 75%")

    subjects = fn.subject_analysis(df)
    print_title("STEP 4: SUBJECT-WISE PERFORMANCE")
    print(subjects.to_string(index=False))
    best_subject = subjects.loc[subjects["Average"].idxmax()]
    weak_subject = subjects.loc[subjects["Average"].idxmin()]
    print()
    print("Best subject  :", best_subject["Subject"], "(average", best_subject["Average"], ")")
    print("Weakest subject:", weak_subject["Subject"], "(average", weak_subject["Average"], ")")

    departments = fn.department_analysis(df)
    print_title("STEP 5: DEPARTMENT-WISE PERFORMANCE")
    print(departments.to_string(index=False))

    grades = fn.grade_distribution(df)
    print_title("STEP 6: GRADE DISTRIBUTION")
    print(grades.to_string(index=False))

    top = fn.top_performers(df, 5)
    print_title("STEP 7: TOP 5 PERFORMERS")
    rank = 1
    for index, row in top.iterrows():
        print(rank, "-", row["Name"], "|", row["Department"], "| Average:", row["Average"], "| Grade:", row["Grade"])
        rank += 1

    print_title("STEP 8: FAILED STUDENTS")
    failed = df[df["Result"] == "Fail"]
    print(failed[["Student_ID", "Name", "Department", "Average"]].to_string(index=False))

    df.to_csv("results.csv", index=False)
    full_table = df[["Student_ID", "Name", "Department", "Total", "Average", "Grade", "Result", "Attendance"]]
    report.make_html_report(summary, subjects, departments, grades, top, full_table, "docs/index.html")

    print()
    print("Saved results.csv and docs/index.html")


main()
