import os, sys, json
from subprocess import check_output, CalledProcessError

def main():
    lines = str(check_output(["gh", "pr", "list"]), "utf-8").split("\n")
    prs = sorted([l.split()[0] for l in lines if l])
    for pr in prs:
        #diff = str(check_output(["gh", "pr", "diff", pr]), "utf-8")
        #print(diff)

        #try:
        #    merge = str(check_output(["gh", "pr", "merge", "-m", pr]), "utf-8")
        #    print(merge)
        #except CalledProcessError:
        #    print("skip", pr)

        cmt = str(check_output(["gh", "pr", "comment", pr, "-b", "please resolve merge conflicts"]), "utf-8")
        print(cmt)

if __name__ == '__main__':
     main()
