def comparison(line1, line2):
    x = line1.count("!") + line1.count("?")
    y = line2.count("!") + line2.count("?")
    return line1 + line2 if x > y else line2 + line1 if y > x else "АХЪ КАбылья чешуйа"

string1 = "!!!писить??"
string2 = "!!какать!?!"
print(comparison(string1,string2))