def comparison(line1, line2):
    if len(line1) > len(line2):
         line1 += line2
         return line1
    elif len(line1) < len(line2):
        line2 += line1
        return line2
    else:
        return "АХЪ КАбылья чешуйа"

string1 = "!!???!!?"
string2 = "!!!?????"
print(comparison(string1,string2))