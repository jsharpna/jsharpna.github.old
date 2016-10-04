from birthday import *

today = "2016-10-4"
dobs_data = ["1967-9-3", "1983-3-19", "1954-12-24", "1988-11-1", "1970-7-7", "2000-3-15"]

def dob_str_to_int(bday):
    return [int(s) for s in bday.split("-")]

today = dob_str_to_int(today)
Ages = [calc_age(today,dob_str_to_int(s)) for s in dobs_data]

