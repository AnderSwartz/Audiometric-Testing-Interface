freqs = list(range(1000, 10001, 1000))
freqs.append(500)
freqs.append(250)
scores = {}
print("running prototype...")
for freq in freqs:
    hits = {}
    attempts = {}
    # print(hits)
    # print(attempts)
    hits[0] = 0 #probably dont need these anymore
    attempts[0] = 0
    amp = 0

    #This starts as False because we want to first trial to count
    new_ascending_presentation = False 
    #When it is True, that means we just went down 10 dbs, and we
    #dont want to count the next presentation as a hit or an attempt

    prev_hit = False
    attempts[-5] = 0
    while (prev_hit and attempts[amp+10] < 3) or (prev_hit and attempts[amp+10] >= 3 and hits[amp+10] / attempts[amp+10] < .5) or (not prev_hit and attempts[amp-5] < 3) or (not prev_hit and attempts[amp-5] >= 3 and hits[amp-5] / attempts[amp-5] < .5):
        prev_hit = False
        print("Testing frequency",freq,"hz at amplitude of",amp,"db")
        user_input = input("Can you hear it? Enter y or n: ")
        while user_input != "y" and user_input != "n":
            user_input = input("please enter y or n: ")
        if not new_ascending_presentation:
            if amp in attempts:
                attempts[amp] +=1
            else:
                attempts[amp] =1
        if user_input == "y":
            if not new_ascending_presentation:
                if amp in hits:
                    hits[amp] += 1
                else:
                    hits[amp] = 1
            prev_hit = True
            amp -= 10
            new_ascending_presentation = True
        else:
            if amp not in hits:
                hits[amp] = 0
            amp += 5
            new_ascending_presentation = False
        if amp not in attempts:
            attempts[amp] = 0
        # print(attempts)
        # print(hits)
        
        # print("prev_hit",prev_hit)
        # print("hits",hits)
        # print("attempts",attempts)
        # if(prev_hit):
        #     print(prev_hit and attempts[amp+10] < 3)
        #     print(prev_hit and attempts[amp+10] >= 3 and hits[amp+10] / attempts[amp+10] < .5)
        # else:
        #     print(not prev_hit and attempts[amp-5] < 3)
        #     print(not prev_hit and attempts[amp-5] >= 3 and hits[amp-5] / attempts[amp-5] < .5)
    if prev_hit:
        scores[str(freq)+"hz"] = str(amp+10)+"db"
    else:
        scores[str(freq)+"hz"] = str(amp-5)+"db"
    print(scores)
print(scores)
    

       

