import pandas as pd

# Load dataset
df = pd.read_csv("week 1/student_performance.csv")

# Convert first 10 rows to HTML
html_table = df.head(10).to_html(index=False)

# Full HTML content
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Week 1 - Student Performance</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <h1>Week 1 Assignment</h1>
    <h2>Student Performance Dataset</h2>
    {html_table}
</body>
</html>
"""

# Save HTML file
with open("Week1_StudentPerformance.html", "w") as f:
    f.write(html_content)

print("HTML report generated successfully!")
