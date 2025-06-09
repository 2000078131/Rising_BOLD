import sys

# Fresher profile class
class FresherProfile:
    def __init__(self, fresher_id, name, department, skills):
        self.fresher_id = fresher_id
        self.name = name
        self.department = department
        self.skills = skills
        # Progress tracking for onboarding steps
        self.training_status = {
            'daily_quiz': 'Pending',  # Pending, Completed
            'coding_challenge': 'Not Started',  # Not Started, In Progress, Completed
            'assignment_submission': 'Pending',  # Pending, Submitted
            'certification': 'In Progress',  # Not Started, In Progress, Completed
        }
        # Assessment scores
        self.assessments = {
            'quiz_scores': [],
            'coding_scores': [],
            'assignments_scores': [],
            'certification_completed': False
        }
        # Onboarding plan (simplified)
        self.onboarding_plan = []

    def update_progress(self, task, status, score=None):
        if task in self.training_status:
            self.training_status[task] = status
            if score is not None:
                # Add score to assessments accordingly
                if task == 'daily_quiz':
                    self.assessments['quiz_scores'].append(score)
                elif task == 'coding_challenge':
                    self.assessments['coding_scores'].append(score)
                elif task == 'assignment_submission':
                    self.assessments['assignments_scores'].append(score)
                elif task == 'certification':
                    self.assessments['certification_completed'] = (status == 'Completed')

    def average_score(self, assessment_type):
        scores = self.assessments.get(assessment_type, [])
        if not scores:
            return None
        return sum(scores) / len(scores)

    def __str__(self):
        return f"{self.fresher_id} - {self.name} ({self.department})"


# Agent classes simulate the multi-agent framework
class OnboardingAgent:
    def create_onboarding_plan(self, fresher):
        # For simplicity, assign fixed daily tasks for 5 days
        plan = [
            "Day 1: Complete Company Orientation",
            "Day 2: Complete Role-Specific Training Modules",
            "Day 3: Practice Coding Challenges",
            "Day 4: Submit Assignment",
            "Day 5: Complete Certification Exam"
        ]
        fresher.onboarding_plan = plan


class AssessmentAgent:
    # Simulate assessments and scoring
    def evaluate_quiz(self, fresher):
        print("Simulating Quiz Assessment...")
        try:
            score = int(input("Enter quiz score (0-100): "))
            if 0 <= score <= 100:
                fresher.update_progress('daily_quiz', 'Completed', score)
                print(f"Quiz submitted with score: {score}")
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def evaluate_coding(self, fresher):
        print("Simulating Coding Challenge Assessment...")
        status = input("Enter coding challenge status (Not Started/In Progress/Completed): ")
        score = None
        if status == 'Completed':
            try:
                score = int(input("Enter coding challenge score (0-100): "))
                if 0 <= score <= 100:
                    fresher.update_progress('coding_challenge', status, score)
                    print(f"Coding challenge status updated to: {status} with score: {score}")
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            fresher.update_progress('coding_challenge', status)
            print(f"Coding challenge status updated to: {status}")

    def evaluate_assignment(self, fresher):
        print("Simulating Assignment Submission...")
        status = input("Enter assignment status (Pending/Submitted): ")
        score = None
        if status == 'Submitted':
            try:
                score = int(input("Enter assignment score (0-100): "))
                if 0 <= score <= 100:
                    fresher.update_progress('assignment_submission', status, score)
                    print(f"Assignment status updated to: {status} with score: {score}")
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            fresher.update_progress('assignment_submission', status)
            print(f"Assignment status updated to: {status}")

    def evaluate_certification(self, fresher):
        print("Simulating Certification Completion...")
        status = input("Enter certification status (Not Started/In Progress/Completed): ")
        fresher.update_progress('certification', status)
        print(f"Certification status updated to: {status}")


class ProfileAgent:
    # Update fresher profiles based on assessment updates (integrated in update_progress)

    def display_profile(self, fresher):
        print(f"\nProfile for {fresher.name} (ID: {fresher.fresher_id})")
        print(f"Department: {fresher.department}")
        print(f"Skills: {', '.join(fresher.skills)}")
        print("Training Status:")
        for task, status in fresher.training_status.items():
            print(f"  {task.replace('_', ' ').title()}: {status}")
        print("Average Scores:")
        print(f"  Quiz: {self.format_score(fresher.average_score('quiz_scores'))}")
        print(f"  Coding Challenge: {self.format_score(fresher.average_score('coding_scores'))}")
        print(f"  Assignment: {self.format_score(fresher.average_score('assignments_scores'))}")
        print(f"  Certification Completed: {'Yes' if fresher.assessments['certification_completed'] else 'No'}")

    def format_score(self, score):
        return f"{score:.2f}" if score is not None else "N/A"


class ReportingAgent:
    def generate_report(self, freshers):
        print("\n--- Training Progress Report ---")
        for f in freshers:
            avg_quiz = f.average_score('quiz_scores')
            avg_coding = f.average_score('coding_scores')
            avg_assign = f.average_score('assignments_scores')
            cert = 'Yes' if f.assessments['certification_completed'] else 'No'
            print(f"Fresher: {f.name} ({f.department})")
            print(f"  Quiz Avg Score: {avg_quiz:.2f}" if avg_quiz is not None else "  Quiz Avg Score: N/A")
            print(f"  Coding Avg Score: {avg_coding:.2f}" if avg_coding is not None else "  Coding Avg Score: N/A")
            print(f"  Assignment Avg Score: {avg_assign:.2f}" if avg_assign is not None else "  Assignment Avg Score: N/A")
            print(f"  Certification Completed: {cert}")
            print("-" * 40)


# Console menu interface
def main():
    print("Welcome to Mavericks Onboarding Training Console")
    freshers = []
    onboard_agent = OnboardingAgent()
    assess_agent = AssessmentAgent()
    profile_agent = ProfileAgent()
    reporting_agent = ReportingAgent()

    # Sample freshers
    freshers.append(FresherProfile("1000075845", "Akash Ammireddy", "Data Engineering", ["Python", "SQL", "Snowflake"]))
    freshers.append(FresherProfile("2000078131", "Harsha Sajja", "Data Engineering", ["Python", "SQL", "Snowflake"]))
    freshers.append(FresherProfile("2000078432", "Vemula Charan", "Data Engineering", ["Python", "SQL", "Snowflake"]))
    freshers.append(FresherProfile("2000078106", "Melam Dinesh", "Data Engineering", ["Python", "SQL", "Snowflake"]))
    
    # Create onboarding plans for all freshers
    for f in freshers:
        onboard_agent.create_onboarding_plan(f)

    while True:
        print("\nMain Menu:")
        print("1. View Fresher Profiles")
        print("2. Update Fresher Assessments")
        print("3. View Fresher Training Dashboard")
        print("4. Generate Training Report")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            print("\nList of Freshers:")
            for idx, f in enumerate(freshers, start=1):
                print(f"  {idx}. {f}")
        elif choice == '2':
            print("\nSelect Fresher to Update:")
            for idx, f in enumerate(freshers, start=1):
                print(f"  {idx}. {f.name}")
            sel = input("Enter fresher number: ").strip()
            if sel.isdigit() and 1 <= int(sel) <= len(freshers):
                fresher = freshers[int(sel)-1]
                print(f"\nUpdating assessments for {fresher.name}:")
                assess_agent.evaluate_quiz(fresher)
                assess_agent.evaluate_coding(fresher)
                assess_agent.evaluate_assignment(fresher)
                assess_agent.evaluate_certification(fresher)
            else:
                print("Invalid selection.")
        elif choice == '3':
            print("\nSelect Fresher to View Dashboard:")
            for idx, f in enumerate(freshers, start=1):
                print(f"  {idx}. {f.name}")
            sel = input("Enter fresher number: ").strip()
            if sel.isdigit() and 1 <= int(sel) <= len(freshers):
                profile_agent.display_profile(freshers[int(sel)-1])
            else:
                print("Invalid selection.")
        elif choice == '4':
            reporting_agent.generate_report(freshers)
        elif choice == '5':
            print("Exiting... Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
