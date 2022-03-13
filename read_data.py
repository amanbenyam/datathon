import sys
#recipient_state_name = 53 commas in
#amount, 7 commas

states = {
"ALASKA": 0,
"ALABAMA": 0,
"ARKANSAS": 0,
"ARIZONA": 0,
"CALIFORNIA": 0,
"COLORADO": 0,
"CONNECTICUT": 0,
"DISTRICT OF COLUMBIA": 0,
"DELAWARE": 0,
"FLORIDA": 0,
"GEORGIA": 0,
"HAWAII": 0,
"IOWA": 0,
"IDAHO": 0,
"ILLINOIS": 0,
"INDIANA": 0,
"KANSAS": 0,
"KENTUCKY": 0,
"LOUISIANA": 0,
"MASSACHUSETTS": 0,
"MARYLAND": 0,
"MAINE": 0,
"MICHIGAN": 0,
"MINNESOTA": 0,
"MISSOURI": 0,
"MISSISSIPPI": 0,
"MONTANA": 0,
"NORTH CAROLINA": 0,
"NORTH DAKOTA": 0,
"NEBRASKA": 0,
"NEW HAMPSHIRE": 0,
"NEW JERSEY": 0,
"NEW MEXICO": 0,
"NEVADA": 0,
"NEW YORK": 0,
"OHIO": 0,
"OKLAHOMA": 0,
"OREGON": 0,
"PENNSYLVANIA": 0,
"RHODE ISLAND": 0,
"SOUTH CAROLINA": 0,
"SOUTH DAKOTA": 0,
"TENNESSEE": 0,
"TEXAS": 0,
"UTAH": 0,
"VIRGINIA": 0,
"VERMONT": 0,
"WASHINGTON": 0,
"WISCONSIN": 0,
"WEST VIRGINIA": 0,
"WYOMING": 0
}


def total_obligated(line):
        commas = 0
        lines_read = line.split(',')
        if str(lines_read[7]).isdigit():
                return lines_read[7]

def find_state(lines_read, start, end):
        for i in range(start, end):
                if (len(lines_read) > i):
                        if lines_read[i] in states:
                                return i
        return -1
def total_by_state(line):
        commas = 0
        lines_read = line.split(',')
        for i in range(0, 15, 5):
                ret_val = find_state(lines_read, 50 - i, 55 + i)
                if (ret_val != -1):
                        return lines_read[ret_val]

def method():
        with open(sys.argv[1], 'r') as f:
                #Ignore first line
                f.readline() 
                #100 lines of data. 
                for i in range(10000):
                        print(i)
                        line = f.readline()
                        state = total_by_state(line)
                        money = total_obligated(line)
                        if (state != None and money != None):
                                states[state] += float(money)
method()
print(states)
