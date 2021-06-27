"""
Originally made by ldmsys, converted by iseoulu.
Distributed under CC BY-NC-SA 2.0 KR.

Template generating code for regular session of Arbitrator/Administrator Appointment Committee

Note:
    1. Arbitrators and administrators are hereinafter collectively refered to as staff.
    2. Eligible staffs refers to staffs with recommendation authority under subparagraph '1.1 Recommendation of Administrator' and '1.2. Recommendation of Arbitrator' of 'Namuwiki:Request for Permissions'.
    3. Both staff list and candidate list should be written in .csv file.
"""
import argparse, os
import csv
import pandas as pd
def file_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise NotADirectoryError(string)


def main():
    parser = argparse.ArgumentParser(description="Print the table for regular session of the Arbitrator/Administrator Appointment Committee")
    parser.add_argument(
        '-p', '--position', required=True, choices=["Arb", "Admin"], help='Arb refers to Arbitrator, Admin refers to Administrator')
    parser.add_argument(
        '-r', '--round', required=True, type=int, help='Number of regular sessions')
    parser.add_argument(
        '-s', '--StaffList', required=True, type=file_path, help='Directory path to eligible staff list, .csv')
    parser.add_argument(
        '-c', '--CandidateList', required=True, type=file_path, help='Directory path to candiates list, .csv')
    args = parser.parse_args()

    df_st = pd.read_csv(args.StaffList, delimiter=',')
    st = df_st.iloc[:,0]

    df_cndt = pd.read_csv(args.CandidateList, delimiter=',')
    cndt = df_cndt.iloc[:,0]

    if args.position == "Admin":
        nomination = "관리자"
    elif args.position == "Arb":
        nomination = "중재자"
    
    width = 100 / (len(cndt)+1)
    width = "{0:.2f}".format(width)
    print("||<table bordercolor=#00a495><tablealign=center><table bgcolor=#ffffff,#2d2f34><rowbgcolor=#00a495><-8> '''{{{#ffffff 제 "+str(args.round)+"회",nomination,"임명 회의}}}''' ||")
    print("||<width="+width+"%><rowbgcolor=#00a495><colbgcolor=#00a495>", end="||")
    for candidate in cndt:
        print("<width="+width+"%> \'\'\'[[사용자:"+candidate+"|{{{#yellow "+candidate+"}}}]]\'\'\'", end=" ||")
    print("")
    for staff in st:
        print("|| \'\'\'[[사용자:"+staff+"|{{{#ffffff "+staff+"}}}]]\'\'\'", end=" ||")
        for x in range(len(cndt)):
            print(" ", end="||")
        print("")
    print("|| '''{{{#FFF 표결 결과}}}'''",end=" ||")
    for x in range(len(cndt)):
        print("<#FFA>", end=" - ||")
    print("")
    print("|| [[https://board.namu.wiki/|'''{{{#FFF 임명 결과}}}''']]",end=" ||")
    for x in range(len(cndt)):
        print("<#FFA>", end=" - ||")
    print("")
    print("||<-8> '''{{{#ffffff O는 찬성, X는 반대, - 는 기권, 공란은 불참을 의미}}}''' ||")
    print("## 참고: #FFA - 미확정(노랑) | #FAA - 기각(빨강) | #AFA - 통과(초록) | 최종 기호: ✓, ✗")

if __name__ == "__main__":
    main()