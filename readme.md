# Namuwiki Template Generator
## Inroduction

This is a namuwiki template generator for regular session of Arbitrator/Administrator Appointment Committee(중재자 임명 회의/관리자 임명 회의).

[Namuwiki](https://en.wikipedia.org/wiki/Namuwiki) is a Paraguay-based Korean wiki powered by *The Seed*. Since *The Seed* has its own syntax different from that of *Mediawiki*, this program might not work on *Mediawiki*-based wiki websites.

## Usage
``` sh
python AppCom.py -p Admin -r 15 -s ./Staff.csv -c ./Candidate.csv
```

* ```-p {Arb,Admin}, --position {Arb,Admin}```
    * ```Arb``` refers to **Arbitrator(중재자)**, and ```Admin``` refers to **Administrator(관리자)**.
* ```-r ROUND, --round ROUND```
    * Number of regular sessions.
* ```-s STAFFLIST, --StaffList STAFFLIST```
    * Directory path to eligible staff list, .csv
* ```-c CANDIDATELIST, --CandidateList CANDIDATELIST```
    * Directory path to candiates list, .csv

## Note
1. Arbitrators and administrators are collectively refered to as **staff(운영진)**.
2. **Eligible staffs(추천 가능 운영진)** refers to staffs with recommendation authority under subparagraph *1.1 Recommendation of Administrator(1.1. 관리자 추천)* and *1.2. Recommendation of Arbitrator(1.2. 중재자 추천)* of **Namuwiki:Request for Permissions(나무위키:운영진 지원)**.
3. Both staff list and candidate list should be written in **.csv file**.
4. In the .csv file, **Candidate** and **Staff** refers to the name of column. **Don't remove them from the file.**
5. **Staff.csv** contains *the list of eligible staffs for arbitrator position(추천 가능 운영진 명단)* under **Namuwiki:Arbitrator Appointment Committee(나무위키:중재자 임명 회의)**, as of *2021. 06. 27.*