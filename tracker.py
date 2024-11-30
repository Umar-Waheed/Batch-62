class Student:
    def __init__(self, name, scores):
        """
        Initializes a Student object with:
        - `name`: The name of the student (must be a string).
        - `scores`: A list of scores (floats or integers) for different subjects.
        Raises:
            ValueError: If `name` is not a string.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name must be a non-empty string.")
        self.name = name.strip()
        self.scores = scores
    
    def calculate_average(self):
        """
        Calculates the average score of the student.
        - Returns:
            The average score as a float, calculated by summing all scores and dividing by the number of scores.
        """
        return sum(self.scores) / len(self.scores)
    
    def is_passing(self):
        """
        Determines if the student has passed in all subjects.
        - Passing condition: Each score must be greater than or equal to the threshold (50).
        - Returns:
            True if the student has passed all subjects, False otherwise.
        """
        passing_score = 50
        return all(score >= passing_score for score in self.scores)
class PerformanceTracker:
    def __init__(self):
        """
        Initializes a PerformanceTracker object with:
        - `students`: A dictionary to store student data.
          - Keys: Student names (strings).
          - Values: Corresponding Student objects.
        """
        self.students = {}
    
    def add_student(self, student):
        """
        Adds a new student to the tracker.
        - Parameters:
            - `student`: A Student object to be added to the `students` dictionary.
        """
        self.students[student.name] = student
    
    def calculate_class_average(self):
        """
        Calculates the average score for the entire class.
        - Returns:
            The class average score as a float. If no students are present, returns 0.
        """
        total_score = 0
        total_students = len(self.students)
        
        # Loop through all Student objects in the tracker to calculate total scores
        for student in self.students.values():
            total_score += student.calculate_average()
        
        # Return the average score or 0 if no students are added
        return total_score / total_students if total_students > 0 else 0
    
    def display_student_performance(self):
        """
        Displays the performance of each student, including:
        - Name
        - Average Score
        - Pass/Fail Status
        """
        for student in self.students.values():
            # Calculate average score for the current student
            avg_score = student.calculate_average()
            # Determine if the student is passing or needs improvement
            status = "Passing" if student.is_passing() else "Needs Improvement"
            # Print the student's details
            print(f"Student: {student.name}, Average Score: {avg_score:.2f}, Status: {status}")
def main():
    """
    Handles user input to manage the Student Performance Tracker:
    - Allows the user to add students with their scores.
    - Calculates and displays individual and class performance.
    """
    # Step 1: Create an instance of PerformanceTracker
    tracker = PerformanceTracker()
    
    while True:
        # Prompt for student name or termination keyword
        name = input("Enter the student's name (or type 'done' to finish): ")
        if name.lower() == 'done':  # Exit the loop if the user types 'done'
            break
        
        try:
            scores = []
            # Collect scores for three subjects
            for i in range(3):  # Adjust number of iterations for more/less subjects
                score = float(input(f"Enter score for subject {i + 1}: "))
                scores.append(score)
        except ValueError:
            # Handle invalid (non-numeric) input and prompt again
            print("Invalid input. Please enter numeric values for scores.")
            continue
        
        # Step 2: Create a Student object with the provided name and scores
        student = Student(name, scores)
        # Add the student to the PerformanceTracker
        tracker.add_student(student)

    # Step 3: Display the performance of all students
    print("\nStudent Performance:")
    tracker.display_student_performance()
    
    # Step 4: Calculate and display the class average
    class_avg = tracker.calculate_class_average()
    print(f"\nClass Average Score: {class_avg:.2f}")
if __name__ == "__main__":
    """
    Ensures that the script runs the main() function only when executed directly.
    """
    main()
