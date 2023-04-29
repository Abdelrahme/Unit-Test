def calculate_grade(scores):
    if type(scores)==list:
        if len(scores) == 0:
            return None

        else:
            for score in scores:
                if score < 0 or score > 100:
                    return "out of the range"
            scores = sum(scores) / len(scores)

    if scores >= 90:
            return "A"
    elif scores >= 80:
        return "B"
    elif scores >= 70:
        return "C"
    elif scores >= 60:
        return "D"
    else:
        return "F"


