import sys
import os
import re
import datetime


def is_leap_year(year):
    if not year % 4 and year % 100 or not year % 400:
        return True
    return False


def begin_days(date):
    days = [31, 29 if is_leap_year(
        date[0]) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days[:date[1] - 1]) + date[2]


def calc_time_diff(date_1, date_2):
    if date_1 > date_2:
        date_1, date_2 = date_2, date_1
    return sum([366 if is_leap_year(year) else 365 for year in range(date_1[0], date_2[0])]) + begin_days(date_2) - begin_days(date_1)


def check_date(date):
    days = [31, 29 if is_leap_year(
        date[0]) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if date[0] < 1 or date[1] < 1 or date[1] > 12 or date[2] < 1 or date[2] > days[date[1] - 1]:
        return False
    return True


if __name__ == "__main__":

    now = datetime.datetime.now().date()
    now = [now.year, now.month, now.day]
    argv = ' '.join(sys.argv[1:])
    target = None

    reg_ymd = r'(\d+)[^0-9]+(\d+)[^0-9]+(\d+)[^0-9]*'
    reg_md = r'(\d+)[^0-9]+(\d+)[^0-9]*'

    res = re.match(reg_ymd, argv)

    if res:
        target = [i for i in map(int, res.groups())]
    else:
        res = re.match(reg_md, argv)
        if res:
            target = [i for i in map(int, res.groups())]
            target = now[0:1] + target
    if target:
        if now[1:] > target:
            target[0] += 1
        if check_date(target):
            if now == target:
                print('Is today')
            elif now < target:
                print('After %d days' % (calc_time_diff(now, target),))
            else:
                print('Before %d days' % (calc_time_diff(target, now),))

        else:
            print('Date does not exist')
    else:
        print('Date format error')

                

        
