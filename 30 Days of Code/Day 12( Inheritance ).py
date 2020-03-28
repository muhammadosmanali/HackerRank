

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        score = 0
        for x in self.scores:
            score += x
        avg_score = score // len(self.scores)
        if 90 <= avg_score <= 100:
            return "O"
        elif 80 <= avg_score < 90:
            return "E"
        elif 70 <= avg_score < 80:
            return "A"
        elif 55 <= avg_score < 70:
            return "P"
        elif 40 <= avg_score < 55:
            return "D"
        else:
            return "T"


