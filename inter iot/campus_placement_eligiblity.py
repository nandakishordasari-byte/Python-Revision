cgpa = 7.0
backlogs=0
skills={"Python","AI","Java","SQL"}
required={"Python","AI"}
if cgpa >= 7.0:   
    print("Stage 1 PASS — CGPA ok")
    if backlogs == 0:
        print("Stage 2 PASS — No backlogs")
        if required.issubset(skills):
            print("Stage 3 PASS — Skills ok")
            print("ELIGIBLE")
        else:
            missing = required - skills
            print(f"Stage 3 FAIL — Missing: {missing}")
    else:
        print("Stage 2 FAIL — Has backlogs. Stop here")
else:
    print("Stage 1 FAIL — CGPA too low. Stop here")