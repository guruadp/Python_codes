players = {     
    "left_wing" : ['Jaison', 'Sundar'],    
    "left_back" : ['Harish','Nilesh'],
    "center_back" : ['Viswas','Nilesh'],    
    "pivot" : ['Viswas', 'Naveen'],
    "right_back" : ['Subash','Vikram'],
    "right_wing" : ['Vikram', 'Subash']
}

positions = ['left_wing','left_back','center_back','pivot','right_back','right_wing']

team = []
for lw in players["left_wing"]:
    loop_flag = True
    if lw not in team:
        team.append(lw)
    else:
        #team = []
        continue
    for lb in players["left_back"]:
        if lb not in team and len(team) == 1:
            team.append(lb)
        else:
            #team = []
            continue
        for cb in players["center_back"]:
            if (cb not in team) and len(team) == 2:
                team.append(cb)
            else:
                #team = []
                continue
            for pp in players["pivot"]:
                if pp not in team and len(team) == 3:
                    team.append(pp)
                else:
                    #team = []
                    continue
                
                for rb in players["right_back"]:
                    if rb not in team and len(team) == 4:
                        team.append(rb)
                    else:
                        #team = []
                        continue
                    for rw in players["right_wing"]:                   
                        if rw not in team and len(team) == 5:
                            team.append(rw)
                            print(team)
                            team = []
                        else:
                            #team = []
                            continue

                        
    

                    