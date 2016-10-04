def calc_age(today,dob):
    """
    This returns the age of a person in years
    Input: 2 lists of three integers: year, month, day
    Output: Integer
    """
    age = today[0] - dob[0]
    if not bday_passed(today,dob):
        age += -1
    return age
    
def bday_passed(today,dob):
    """
    This tests if their birthday has occured yet this year
    returns True is birthday has occured
    """
    if today[1] > dob[1]: 
        passed_flag = True
    if today[1] < dob[1]:
        passed_flag = False
    if today[1] == dob[1]:
        if today[2] >= dob[2]:
            passed_flag = True
        else:
            passed_flag = False
    return passed_flag
