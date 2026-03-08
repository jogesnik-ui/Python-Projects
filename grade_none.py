


def get_grade(score):
    if score < 0:
        return None
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"
    


for score in [-10, 32, 72]:
    result = get_grade(score)
    if result is not None:
        print(f"Result:{score}: {result}")
    else:
        print(f"Invalid Score:{score}")
    