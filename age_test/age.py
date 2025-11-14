def test_age(age):
    if  0 <= age < 9:
        return "child"
    elif 9 <= age < 18:
        return "teenager"
    elif 18 <= age < 65:
        return "adult"
    elif 65 <= age < 125:
        return "golden age"
    else:
        return f"{age} is not a valid age"
    
    