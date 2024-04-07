def value(greeting):
    if greeting.startswith("здравствуйте"):
        return 100
    elif greeting.startswith("з"):
        return 20
    else:
        return 0
