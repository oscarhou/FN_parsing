from enum import Enum
import re
import sys

class Column(Enum):
    POST_DATE = 0
    ACC_DATE = 1
    DETAILS = 2
    TOTAL = 3
    PRINCIPAL_TRANS = 4
    PRINCIPAL_BAL = 5
    INTEREST_TRANS = 6
    INTEREST_BAL = 7
    TAX_TRANS = 8
    TAX_BAL = 9
    SUSPENSE_TRANS = 10
    SUSPENSE_BAL = 11
    OTHER_ESCROW_TRANS = 12
    OTHER_ESCROW_BAL = 13
    FEE_TRANS = 14
    FEE_BAL = 15

class Month(Enum):
    JAN = "Jan"
    FEB = "Feb"
    MAR = "Mar"
    APR = "Apr"
    MAY = "May"
    JUN = "Jun"
    JUL = "Jul"
    AUG = "Aug"
    SEP = "Sep"
    OCT = "Oct"
    NOV = "Nov"
    DEC = "Dec"

def is_month_val(val):
    for e in Month:
        if val in e.value:
            return True
    return False

def month_str_to_int(month):
    count = 0
    for e in Month:
        count += 1
        if month in e.value:
            return count
    return None

if __name__ == "__main__":
    with open(sys.argv[1]) as parse_file:
        for line in parse_file:
            output_line = ""
            x  = re.search("\w* \d*, \d* \w* \d*, \d*", line)
            if not x:
                continue
            split_line = line.split(' ')
            output_line += "{}-{}-{}".format(split_line[0], split_line[1].strip(','), split_line[2])
            output_line += ", {}-{}-{}".format(split_line[3], split_line[4].strip(','), split_line[5])
            output_line += ", "
            count = 6
            for chunk in split_line[6:]:
                count += 1
                if not chunk.startswith('$'):
                    output_line += chunk
                else:
                    break

            for chunk in split_line[count:]:
                if chunk:
                    output_line += ", {}".format(chunk)

            print(output_line)
