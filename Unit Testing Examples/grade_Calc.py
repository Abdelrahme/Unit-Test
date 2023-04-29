def calculate_grade(grade):
    if type(grade)==list:
        if len(grade) == 0:
            return None

        else:
            for score in grade:
                if score < 0 or score > 100:
                    return "out of the range"
            grade = sum(grade) / len(grade)

    if grade >= 90:
            return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


