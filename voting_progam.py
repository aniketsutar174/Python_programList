nomini1 = input("Enter Nomini 1 name;-")
nomini2 = input("Enter Nomini 2 name;-")

nomini1_cnt=0
nomini2_cnt=0

voter_id = [1,2]
voter_len=len(voter_id)
while True:
    if voter_id == []:
        print("Voting lines are cloesd..!\n")
        if nomini1_cnt > nomini2_cnt:
            percentage = (nomini1_cnt/voter_len)*100
            print("your",nomini1,"is won by:-",percentage)
            break
        elif nomini2_cnt > nomini1_cnt:
            percentage= (nomini2_cnt/voter_len)*100
            print("your",nomini2,"is won by:-",percentage)
            break
        break
    else:
        voter = int(input("Enter your voter id:-"))
        if voter in voter_id:
            print("Go ahead..\n")
            voter_id.remove(voter)
            print("Enter your vote for",nomini1,"or",nomini2)
            vote=int(input("Enter your vote for"))
            if vote==1:
                nomini1_cnt+=1
                print("You have voted to:-",nomini1)

            elif vote==2:
                nomini2_cnt+=1
                print("You have voted to:-",nomini2)

        else:
            print("You are not a voter..! or already voted..!")



