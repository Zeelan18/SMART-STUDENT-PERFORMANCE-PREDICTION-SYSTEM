# Smart Student Performance Prediction System

## 1. PROBLEM STATEMENT:

- Student performance is influenced by multiple academic and behavioral factors.
- Faculty may find it difficult to identify students who are at risk at an early stage.
- A data-driven system can help predict student performance.
- The system can provide recommendations for improving student outcomes.

## 2. PROPOSED SOLUTION:

- Collect student-related academic information.
- Process the entered data.
- Use a Machine Learning model to predict performance.
- Classify students based on predicted performance.
- Generate intelligent recommendations.
- Display the results through a user-friendly interface.

## 3. PROCESS FLOW:

```text
Start
  ↓
Enter Student Details
  ↓
Enter Subject Marks
  ↓
Enter Attendance Data
  ↓
Enter Study Hours
  ↓
ML Prediction
  ↓
Display Result
  ↓
End

4. PROJECT MAPPING:

V-Model Stage| Smart Student Project
Requirement Analysis| Identify student performance prediction requirements
System Design| Design system architecture, input forms and user interface
Implementation| Develop Python and Machine Learning application
Integration| Integrate UI, data processing and ML model
Testing| Test individual modules and complete system
Validation| Check system against defined requirements
Demonstration| Present the working student performance prediction system

---

5. PROJECT - MODULAR APPLICATION DEVELOPMENT:

The application can be developed using separate functions/modules.

Create separate functions:

get_student_data()
get_subject_marks()
get_attendance_data()
get_study_hours()
get_previous_performance()
validate_input()
calculate_average()
calculate_performance()
predict_performance()
determine_risk_level()
generate_recommendation()
display_result()

Suggested Module Responsibilities:

Module| Responsibility
Student Data Module| Collect student details
Marks Module| Collect and process subject marks
Attendance Module| Collect attendance information
Study Hours Module| Collect monthly study hours
Performance Module| Calculate academic performance
Prediction Module| Predict student performance
Recommendation Module| Generate improvement suggestions
Display Module| Display final results

---

6. REQUIREMENT ANALYSIS:

6.1 FUNCTIONAL REQUIREMENTS:

The system should:

- Accept student details.
- Accept student name and student ID.
- Accept marks for multiple subjects.
- Accept attendance percentage.
- Accept monthly attendance information.
- Accept monthly study hours.
- Accept previous academic performance.
- Validate user inputs.
- Store/process student information.
- Preprocess input data.
- Calculate average marks.
- Calculate overall performance.
- Apply the trained Machine Learning model.
- Predict student performance.
- Classify the student's performance level.
- Determine the student's risk level.
- Generate academic recommendations.
- Display results through the user interface.
- Handle invalid inputs.
- Provide a reset/clear option.

---

6.2 NON-FUNCTIONAL REQUIREMENTS:

The application should be:

- User-friendly
- Easy to understand
- Easy to operate
- Fast in generating predictions
- Reliable
- Maintainable
- Scalable
- Secure with respect to student data
- Easy to test
- Accurate in processing student information

---

6.3 IDENTIFY THE USER:

Primary users may include:

- Faculty
- Academic coordinators
- Mentors
- Students
- Academic administrators

---

6.4 USER REQUIREMENT:

The user should be able to:

- Enter student information.
- Enter subject-wise marks.
- Enter attendance information.
- Enter monthly study hours.
- Enter previous academic performance.
- Submit the information for analysis.
- View calculated academic performance.
- View predicted performance.
- Understand the student's risk level.
- Receive improvement recommendations.
- Reset the entered information.

---

6.5 IDENTIFY SYSTEM INPUTS:

The system can use the following inputs:

Student Information:

- Student ID
- Student Name

Academic Information:

- Subject 1 Marks
- Subject 2 Marks
- Subject 3 Marks
- Subject 4 Marks
- Subject 5 Marks
- Previous Academic Performance

Attendance Information:

- Month 1 Attendance Percentage
- Month 2 Attendance Percentage
- Month 3 Attendance Percentage
- Month 4 Attendance Percentage
- Month 5 Attendance Percentage

Study Information:

- Month 1 Study Hours
- Month 2 Study Hours
- Month 3 Study Hours
- Month 4 Study Hours
- Month 5 Study Hours

Other Academic Information:

- Internal Assessment Marks
- Assignment Completion Percentage

---

6.6 IDENTIFY SYSTEM OUTPUTS:

The system should provide:

- Average subject marks
- Average attendance percentage
- Average study hours
- Previous academic performance
- Overall performance score
- Predicted performance level
- Risk level
- Prediction score/probability
- Key factors affecting performance
- Recommended actions

---

6.6.1 PERFORMANCE PREDICTION:

The system may classify student performance into the following categories:

- Excellent
- Good
- Average
- At Risk

---

6.6.2 RISK LEVEL:

The system can determine the student's academic risk level:

- Low Risk
- Moderate Risk
- High Risk

---

6.6.3 ADDITIONAL OUTPUT:

The system can provide:

- Prediction score/probability
- Average marks
- Average attendance
- Average study hours
- Previous academic performance
- Risk level
- Key factors affecting performance
- Recommended actions

---

Example:

Student Name: Arun

Average Marks: 82%

Average Attendance: 91%

Average Study Hours: 4.5 Hours/Day

Previous Academic Performance: Good

Prediction: Good Performance

Risk Level: Low

Recommendation:
Maintain the current study pattern and attendance.
Continue regular revision and assignment completion.

---

7. SYSTEM OBJECTIVES:

The main objectives of the system are:

- To predict student academic performance.
- To identify students who may be at academic risk.
- To analyze multiple academic factors.
- To analyze attendance patterns.
- To analyze study-hour patterns.
- To consider previous academic performance.
- To provide early identification of students requiring support.
- To provide personalized academic recommendations.
- To help faculty monitor student performance.
- To support data-driven academic decision making.

---






