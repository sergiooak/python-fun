from datetime import date
from random import randint
import sys
import subprocess
import os


def get_date_string(d):
    rtn = d.strftime("%Y-%m-%dT%H:%M:%SZ")
    return rtn


d1 = date(2021, 7, 1)


def main():
    days = [d1]
    for day in days:
        curdate = get_date_string(day)
        for commit in range(1):
            rand = str(randint(0, 1000000))
            string = "echo {} > gitHack/{}.txt".format(curdate, rand)
            string = "git add gitHack/{}.txt; git commit --date='{}' -m 'update'".format(rand, curdate, curdate, curdate)
            string = "git push"
            subprocess.call(string, shell=True)


if __name__ == "__main__":
    main()
