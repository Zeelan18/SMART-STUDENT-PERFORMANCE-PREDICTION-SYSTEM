import pandas as pd

data = pd.read_excel("student data.xlsx")

# Calculate study score
study_score = (data["study_hours"] / 8) * 100

# Calculate performance score
performance_score = (
    data["attendance"] * 0.25
    + study_score * 0.20
    + data["internal_marks"] * 0.25
    + data["assignment"] * 0.20
    + data["previous_score"] * 0.10
)

# Sort students by performance score
data["performance_score"] = performance_score

data = data.sort_values(
    by="performance_score"
).reset_index(drop=True)

# Create balanced performance labels
data["performance"] = "Average"

data.loc[
    data.index < 33,
    "performance"
] = "Poor"

data.loc[
    data.index >= 67,
    "performance"
] = "Good"

# Save Excel
data.to_excel(
    "student data.xlsx",
    index=False
)

print("Performance labels created successfully!")

print("\nPerformance distribution:")
print(
    data["performance"].value_counts()
)

print("\nUpdated Excel file saved!")