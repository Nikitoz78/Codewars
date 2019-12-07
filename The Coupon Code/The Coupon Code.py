def date(d):
    import datetime
    s3 = ''
    s = (str(d).split(','))
    s2 = s[1].split(' ')
    s1 = s[0].split(' ')
    for i in s1:
        s3 += (i + '.')
    s3 += str(s2[1])
    d = datetime.datetime.strptime(s3, "%B.%d.%Y")
    return d


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if isinstance(correct_code, str) and isinstance(entered_code, str):
        if correct_code == 'false':
            correct_code = False
            entered_code = int(entered_code)
        elif correct_code == 'true':
            correct_code = True
            entered_code = int(entered_code)
        if entered_code == correct_code and date(current_date) <= date(expiration_date):
             return True
        else:
            return False
    else:
        return False
