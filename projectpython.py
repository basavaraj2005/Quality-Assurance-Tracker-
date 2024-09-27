class QualityAssuranceTracker:
    def __init__(self):
        self.quality_checks = {}
        self.quality_issues = {}

    def log_quality_check(self, check_id, outcome):
        """Log a quality check with its outcome."""
        self.quality_checks[check_id] = outcome
        print(f"Quality check '{check_id}' logged with outcome: '{outcome}'.")

    def manage_quality_issue(self, issue_id, description):
        """Manage and resolve quality issues."""
        if issue_id not in self.quality_issues:
            self.quality_issues[issue_id] = description
            print(f"Quality issue '{issue_id}' added: '{description}'.")
        else:
            print(f"Quality issue '{issue_id}' already exists. Updating description.")
            self.quality_issues[issue_id] = description

    def display_quality_checks(self):
        """Display all logged quality checks."""
        print("\nLogged Quality Checks:")
        for check_id, outcome in self.quality_checks.items():
            print(f"Check ID: {check_id}, Outcome: {outcome}")

    def display_quality_issues(self):
        """Display all quality issues."""
        print("\nQuality Issues:")
        for issue_id, description in self.quality_issues.items():
            print(f"Issue ID: {issue_id}, Description: {description}")

def main():
    tracker = QualityAssuranceTracker()

    while True:
        print("\nQuality Assurance Tracker Menu:")
        print("1. Log Quality Check")
        print("2. Manage Quality Issue")
        print("3. Display Quality Checks")
        print("4. Display Quality Issues")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            check_id = input("Enter Check ID: ")
            outcome = input("Enter Outcome: ")
            tracker.log_quality_check(check_id, outcome)
        elif choice == '2':
            issue_id = input("Enter Issue ID: ")
            description = input("Enter Issue Description: ")
            tracker.manage_quality_issue(issue_id, description)
        elif choice == '3':
            tracker.display_quality_checks()
        elif choice == '4':
            tracker.display_quality_issues()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
