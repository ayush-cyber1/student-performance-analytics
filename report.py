GRADE_COLORS = {
    "A+": "#1b8a5a",
    "A": "#2e9e5b",
    "B": "#6cb33f",
    "C": "#e0b72e",
    "D": "#e68a2e",
    "E": "#e0612e",
    "F": "#d63b3b",
}

STYLE = """
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; margin: 0; background: #eef2f7; color: #222; }
header { background: linear-gradient(120deg, #1f3a5f, #3a6ea5); color: white; padding: 35px 20px; text-align: center; }
header h1 { margin: 0 0 8px 0; font-size: 32px; }
header p { margin: 0; opacity: 0.9; }
.container { max-width: 1100px; margin: 0 auto; padding: 20px; }
h2 { color: #1f3a5f; border-left: 5px solid #3a6ea5; padding-left: 10px; margin-top: 40px; }
.cards { display: flex; flex-wrap: wrap; gap: 15px; margin-top: 25px; }
.card { flex: 1 1 150px; background: white; border-radius: 10px; padding: 18px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
.card .value { font-size: 30px; font-weight: bold; color: #1f3a5f; }
.card .label { font-size: 13px; color: #666; margin-top: 5px; }
.panel { background: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); overflow-x: auto; }
.row { display: flex; flex-wrap: wrap; gap: 20px; }
.row .panel { flex: 1 1 320px; }
table { border-collapse: collapse; width: 100%; font-size: 14px; }
th { background: #1f3a5f; color: white; padding: 9px; }
td { padding: 8px; text-align: center; border-bottom: 1px solid #e3e7ec; }
tr:hover td { background: #f3f7fc; }
.badge { color: white; padding: 3px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; }
.pass { background: #2e9e5b; }
.fail { background: #d63b3b; }
.short { background: #e68a2e; }
.ok { background: #3a6ea5; }
.bar-line { display: flex; align-items: center; margin: 9px 0; }
.bar-name { width: 90px; font-size: 14px; }
.bar-track { flex: 1; background: #e3e7ec; border-radius: 6px; height: 20px; }
.bar-fill { height: 20px; border-radius: 6px; background: #3a6ea5; }
.bar-value { width: 55px; text-align: right; font-size: 14px; font-weight: bold; }
.donut-wrap { text-align: center; }
.donut { width: 170px; height: 170px; border-radius: 50%; margin: 10px auto; position: relative; }
.donut-hole { position: absolute; top: 28px; left: 28px; width: 114px; height: 114px; background: white; border-radius: 50%; line-height: 114px; font-size: 26px; font-weight: bold; color: #1f3a5f; }
.legend span { margin: 0 10px; font-size: 14px; }
.dot { display: inline-block; width: 12px; height: 12px; border-radius: 50%; margin-right: 5px; }
.rank { font-weight: bold; font-size: 18px; }
#search { width: 100%; padding: 10px; font-size: 15px; border: 1px solid #bbb; border-radius: 6px; margin-bottom: 12px; }
.scroll { max-height: 500px; overflow-y: auto; }
.rules li { margin: 5px 0; }
footer { text-align: center; padding: 25px; color: #666; font-size: 13px; }
"""


def make_cards(summary):
    items = [
        ("Total Students", summary["total_students"]),
        ("Class Average", summary["class_average"]),
        ("Highest Average", summary["highest_average"]),
        ("Lowest Average", summary["lowest_average"]),
        ("Passed", summary["passed"]),
        ("Failed", summary["failed"]),
        ("Pass Percentage", str(summary["pass_percentage"]) + "%"),
        ("Attendance Shortage", summary["attendance_shortage"]),
    ]
    html = "<div class='cards'>"
    for label, value in items:
        html += "<div class='card'><div class='value'>" + str(value) + "</div>"
        html += "<div class='label'>" + label + "</div></div>"
    html += "</div>"
    return html


def make_donut(summary):
    percent = summary["pass_percentage"]
    html = "<div class='donut-wrap'>"
    html += "<div class='donut' style='background: conic-gradient(#2e9e5b 0 " + str(percent) + "%, #d63b3b " + str(percent) + "% 100%);'>"
    html += "<div class='donut-hole'>" + str(percent) + "%</div></div>"
    html += "<div class='legend'><span><i class='dot' style='background:#2e9e5b'></i>Passed: " + str(summary["passed"]) + "</span>"
    html += "<span><i class='dot' style='background:#d63b3b'></i>Failed: " + str(summary["failed"]) + "</span></div></div>"
    return html


def make_bars(names, values, maximum, colors=None):
    html = ""
    for i in range(len(names)):
        width = values[i] / maximum * 100
        color = "#3a6ea5"
        if colors is not None:
            color = colors[i]
        html += "<div class='bar-line'><div class='bar-name'>" + str(names[i]) + "</div>"
        html += "<div class='bar-track'><div class='bar-fill' style='width:" + str(round(width, 1)) + "%; background:" + color + ";'></div></div>"
        html += "<div class='bar-value'>" + str(values[i]) + "</div></div>"
    return html


def make_subject_table(subjects):
    html = "<table><tr><th>Subject</th><th>Average</th><th>Highest</th><th>Lowest</th><th>Passed</th><th>Failed</th></tr>"
    for index, row in subjects.iterrows():
        html += "<tr><td>" + row["Subject"] + "</td><td>" + str(row["Average"]) + "</td><td>" + str(row["Highest"]) + "</td>"
        html += "<td>" + str(row["Lowest"]) + "</td><td>" + str(row["Passed"]) + "</td><td>" + str(row["Failed"]) + "</td></tr>"
    html += "</table>"
    return html


def make_department_table(departments):
    html = "<table><tr><th>Department</th><th>Students</th><th>Avg Marks</th><th>Avg Attendance</th><th>Passed</th></tr>"
    for index, row in departments.iterrows():
        html += "<tr><td>" + row["Department"] + "</td><td>" + str(int(row["Students"])) + "</td><td>" + str(row["Average_Marks"]) + "</td>"
        html += "<td>" + str(row["Average_Attendance"]) + "</td><td>" + str(int(row["Passed"])) + "</td></tr>"
    html += "</table>"
    return html


def make_top_table(top):
    medals = ["1st", "2nd", "3rd", "4th", "5th"]
    html = "<table><tr><th>Rank</th><th>Name</th><th>Department</th><th>Total</th><th>Average</th><th>Grade</th></tr>"
    position = 0
    for index, row in top.iterrows():
        color = GRADE_COLORS[row["Grade"]]
        html += "<tr><td class='rank'>" + medals[position] + "</td><td>" + row["Name"] + "</td><td>" + row["Department"] + "</td>"
        html += "<td>" + str(row["Total"]) + "</td><td>" + str(row["Average"]) + "</td>"
        html += "<td><span class='badge' style='background:" + color + "'>" + row["Grade"] + "</span></td></tr>"
        position += 1
    html += "</table>"
    return html


def make_full_table(full_table):
    html = "<table id='students'><tr><th>ID</th><th>Name</th><th>Dept</th><th>Total</th><th>Average</th><th>Grade</th><th>Result</th><th>Attendance</th></tr>"
    for index, row in full_table.iterrows():
        grade_color = GRADE_COLORS[row["Grade"]]
        result_class = "pass" if row["Result"] == "Pass" else "fail"
        attendance_class = "short" if row["Attendance"] < 75 else "ok"
        html += "<tr><td>" + str(row["Student_ID"]) + "</td><td>" + row["Name"] + "</td><td>" + row["Department"] + "</td>"
        html += "<td>" + str(row["Total"]) + "</td><td>" + str(row["Average"]) + "</td>"
        html += "<td><span class='badge' style='background:" + grade_color + "'>" + row["Grade"] + "</span></td>"
        html += "<td><span class='badge " + result_class + "'>" + row["Result"] + "</span></td>"
        html += "<td><span class='badge " + attendance_class + "'>" + str(row["Attendance"]) + "%</span></td></tr>"
    html += "</table>"
    return html


def make_html_report(summary, subjects, departments, grades, top, full_table, file_name):
    page = "<!DOCTYPE html><html><head><meta charset='utf-8'>"
    page += "<meta name='viewport' content='width=device-width, initial-scale=1'>"
    page += "<title>Student Performance Analytics System</title><style>" + STYLE + "</style></head><body>"
    page += "<header><h1>Student Performance Analytics System</h1>"
    page += "<p>Built with Python, NumPy and Pandas</p></header><div class='container'>"

    page += make_cards(summary)

    page += "<p><b>Best student:</b> " + summary["best_student"] + " &nbsp;|&nbsp; "
    page += "<b>Needs most support:</b> " + summary["weakest_student"] + "</p>"

    page += "<h2>Pass / Fail and Grades</h2><div class='row'>"
    page += "<div class='panel'><h3>Pass Percentage</h3>" + make_donut(summary) + "</div>"
    grade_names = list(grades["Grade"])
    grade_values = [int(v) for v in grades["Students"]]
    grade_colors = [GRADE_COLORS[g] for g in grade_names]
    page += "<div class='panel'><h3>Grade Distribution</h3>"
    page += make_bars(grade_names, grade_values, max(grade_values), grade_colors) + "</div></div>"

    page += "<h2>Top 5 Students</h2><div class='panel'>" + make_top_table(top) + "</div>"

    page += "<h2>Subject-wise Performance</h2><div class='row'>"
    subject_names = list(subjects["Subject"])
    subject_values = [float(v) for v in subjects["Average"]]
    page += "<div class='panel'><h3>Average Marks by Subject</h3>" + make_bars(subject_names, subject_values, 100) + "</div>"
    page += "<div class='panel'>" + make_subject_table(subjects) + "</div></div>"

    page += "<h2>Department-wise Performance</h2><div class='row'>"
    dept_names = list(departments["Department"])
    dept_values = [float(v) for v in departments["Average_Marks"]]
    page += "<div class='panel'><h3>Average Marks by Department</h3>" + make_bars(dept_names, dept_values, 100) + "</div>"
    page += "<div class='panel'>" + make_department_table(departments) + "</div></div>"

    page += "<h2>Rules Used</h2><div class='panel'><ul class='rules'>"
    page += "<li><b>Grades:</b> 90+ = A+, 80+ = A, 70+ = B, 60+ = C, 50+ = D, 40+ = E, below 40 = F (based on average marks)</li>"
    page += "<li><b>Pass:</b> a student must score at least 40 in every subject</li>"
    page += "<li><b>Attendance shortage:</b> attendance below 75%</li></ul></div>"

    page += "<h2>All Students</h2><div class='panel'>"
    page += "<input id='search' type='text' placeholder='Search by name, department, grade or result...' onkeyup='filterTable()'>"
    page += "<div class='scroll'>" + make_full_table(full_table) + "</div></div>"

    page += "</div><footer>Student Performance Analytics System | Python Project</footer>"
    page += """<script>
function filterTable() {
  var text = document.getElementById('search').value.toLowerCase();
  var rows = document.getElementById('students').getElementsByTagName('tr');
  for (var i = 1; i < rows.length; i++) {
    var rowText = rows[i].innerText.toLowerCase();
    rows[i].style.display = rowText.indexOf(text) > -1 ? '' : 'none';
  }
}
</script></body></html>"""

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(page)
