from attendance_app import create_app
from attendance_app.extensions import db
from attendance_app.models import Student

app = create_app()

def populate():
    with app.app_context():
        # Clear existing students for a fresh start
        print("Clearing existing students...")
        Student.query.delete()

        departments = {
            "Engineering": {
                "branches": ["CSE", "ECE", "AIML", "DS", "IT"],
                "years": 4
            },
            "Pharmacy": {
                "branches": ["B.Pharm"],
                "years": 4
            },
            "MBA": {
                "branches": ["MBA"],
                "years": 2
            }
        }

        sections = ["A", "B", "C"]
        academic_years = ["2023-2024", "2024-2025", "2025-2026"]
        semesters = ["1 Semester", "2 Semester"]

        student_count = 0

        for dept_name, info in departments.items():
            for branch in info["branches"]:
                for year in range(1, info["years"] + 1):
                    for section in sections:
                        for ay in academic_years:
                            for sem in semesters:
                                for i in range(1, 6): # 5 dummy students
                                    # Requested format: branch-year-section-i
                                    roll_no = f"{branch.lower()}-{year}-{section}-{i}"
                                    # Unique roll number needs AY and Sem too if we want them to coexist or be unique
                                    # But since search is by all these filters, let's make it truly unique
                                    unique_roll = f"{ay}-{sem[0]}-{branch.lower()}-{year}-{section}-{i}"

                                    name = f"{branch} Student {i}"

                                    student = Student(
                                        roll_no=unique_roll,
                                        name=name,
                                        department=dept_name,
                                        branch=branch,
                                        year=year,
                                        section=section,
                                        academic_year=ay,
                                        semester=sem
                                    )
                                    db.session.add(student)
                                    student_count += 1

        db.session.commit()
        print(f"Successfully added {student_count} dummy students.")

if __name__ == "__main__":
    populate()
