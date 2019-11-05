#re checks all characters for a match or find other strings/sets
import re
#function is_valid is made, argument of uid.
#re searches through entered uid to find/match
#searches for 2 or more uppercase letters
#searches for 3 or more digits
#searches for a 10 letter UID with those right conditions.
#searches and makes sure there's no repeat.
def is_valid(uid):
    uid = ''.join(sorted(uid))
    has_2_or_more_upper = bool(re.search(r'[A-Z]{2,}', uid))
    has_3_or_more_digits = bool(re.search(r'\d{3,}', uid))
    has_10_proper_elements = bool(re.search(r'^[a-zA-Z0-9]{10}$', uid))
    no_repeats = not bool(re.search(r'(.)\1', uid))
#if UID meets conditions, return valid, if not, returns invalid.
    if has_2_or_more_upper and has_3_or_more_digits and has_10_proper_elements and no_repeats:
        return "Valid"
    else:
        return "Invalid"
#once all characters have been checked print output
for _ in range(int(input())):
    print(is_valid(input()))
