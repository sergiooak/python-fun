from datetime import date
from random import randint
import sys
import subprocess
import os


def get_date_string(d):
    rtn = d.strftime("%a %b %d %X %Y %z -0400")
    return rtn


d1 = date(2016, 9, 26)


def main():
    days = [d1]
    for day in days:
        curdate = get_date_string(day)
        for commit in range(1):
            rand = str(randint(0, 1000000))
            string = "echo {} > gitHack/{}.txt; git add gitHack/{}.txt; GIT_AUTHOR_DATE='{}' GIT_COMMITTER_DATE='{}' git commit -m 'update'; git push;".format(curdate, rand, rand, curdate, curdate)
            # subprocess.call(string, shell=True)
            print(string)
            # subprocess.call("echo '" + curdate + str(randint(0, 1000000)) +
            # "' > realwork.txt; git add realwork.txt; GIT_AUTHOR_DATE='" +
            #  curdate + "' GIT_COMMITTER_DATE='" + curdate
            #   + "' git commit -m 'update'; git push;")
        # subprocess.call("git rm realwork.txt; git commit -m 'delete'; git push;")


if __name__ == "__main__":
    main()
