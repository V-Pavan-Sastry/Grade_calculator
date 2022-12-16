########## GRADE CALCULATOR ############
#
#   SUBMITTED BY :
#                   V Pavan [1BM20EI058]
#                   Rohith H Gowda [1BM20EI043]
#   GUIDE: 
#               Prof.  Vani A
#
########################################

########### GLOBAL VARIABLES ############
t1=-1 #total marks in DSP
t2=-1 #total marks in PCS
t3=-1 #total marks in CST
t4=-1 #total marks in PE1
t5=-1 #total marks in PE2
t6=-1 #total marks in TNI
t7=-1 #total marks in IFE
t0t=0 #total marks in 5th sem
#########################################

#######################################
# FUNCTION TO FIND IF THE INPUT VALUE IS IN THE RANGE

def valcheck(x,y):
    if x>=0 and x<=y:
        return '0'
    else:
        return '1'

#######################################

#######################################
# FUNCTION TO FIND Total Score In subjects with LAB

def sub_score_lab():
    c1=-1
    c2=-1
    c3=-1
    l=-1
    a=-1
    c1 = int(input("Enter cie 1 marks (max marks 40): "))
    while valcheck(c1,40)=='1':
        print("INVALID INPUT")
        c1 = int(input("ReEnter cie 1 marks (max marks 40): "))
    c2 = int(input("Enter cie 2 marks (max marks 40): "))
    while valcheck(c2,40)=='1':
        print("INVALID INPUT")
        c2 = int(input("ReEnter cie 2 marks (max marks 40): "))
    c3 = int(input("Enter cie 3 marks (max marks 40): "))
    while valcheck(c3,40)=='1':
        print("INVALID INPUT")
        c3 = int(input("ReEnter cie 3 marks (max marks 40): "))
    l = int(input("Enter Lab marks (max marks 25): "))
    while valcheck(l,25)=='1':
        print("INVALID INPUT")
        l = int(input("ReEnter Lab marks (max marks 25): "))
    a = int(input("Enter AAT marks (max marks 5): "))
    while valcheck(a,5)=='1':
        print("INVALID INPUT")
        a = int(input("ReEnter AAT marks (max marks 5): "))
    min_val=min(c1,c2,c3)
    #print(min_val)
    x=c1+c2+c3-min(c1,c2,c3)
    #print(x)
    t=(x/4)+a+l
    #print(t)
    return t 
#######################################

#######################################
# FUNCTION TO FIND Total Score In subjects without LAB

def sub_score():
    c1=-1
    c2=-1
    c3=-1
    a=-1
    c1 = int(input("Enter cie 1 marks (max marks 40): "))
    while valcheck(c1,40)=='1':
        print("INVALID INPUT")
        c1 = int(input("ReEnter cie 1 marks (max marks 40): "))
    c2 = int(input("Enter cie 2 marks (max marks 40): "))
    while valcheck(c2,40)=='1':
        print("INVALID INPUT")
        c2 = int(input("ReEnter cie 2 marks (max marks 40): "))
    c3 = int(input("Enter cie 3 marks (max marks 40): "))
    while valcheck(c3,40)=='1':
        print("INVALID INPUT")
        c3 = int(input("ReEnter cie 3 marks (max marks 40): "))
    a = int(input("Enter AAT marks (max marks 10): "))
    while valcheck(a,10)=='1':
        print("INVALID INPUT")
        a = int(input("ReEnter AAT marks (max marks 10): "))
    min_val=min(c1,c2,c3)
    #print(min_val)
    x=c1+c2+c3-min(c1,c2,c3)
    #print(x)
    t=(x/2)+a
    #print(t)
    return t 
    
#######################################

############ MAIN FUNCTION ###########
 
if __name__ == "__main__": 

############ CHOOSE SUBJECT / SELECT OPERATION ###################
    while True:
        print("")
        print("")
        print("SELECT SUBJECT :")
        if t1!=-1:
            print("1: Digital Signal Processing : ",t1)
        else:
            print("1: Digital Signal Processing : Not Entered")
        if t2!=-1:
            print("2: Process Control System : ",t2)
        else:
            print("2: Process Control System  : Not Entered")
        if t3!=-1:
            print("3: Communication Systems : ",t3)
        else:
            print("3: Communication Systems  : Not Entered")
        if t4!=-1:
            print("4: Program ELective 1[python/C++] : ",t4)
        else:
            print("4: Program ELective 1[python/C++] : Not Entered")  
        if t5!=-1:
            print("5: Program ELective 2[Product development Technologies/Analytical instrumentation] : ",t5)
        else:
            print("5: Program ELective 2[Product development Technologies/Analytical instrumentation] : Not Entered")  
        if t6!=-1:
            print("6: Transducers and Instrumentation : ",t6)
        else:
            print("6: Transducers and Instrumentation : Not Entered") 
        if t7!=-1:
            print("7: Inovation for Enterprenuership : ",t7)
        else:
            print("7: Inovation for Enterprenuership : Not Entered")
        print("8: Check Grade")
        m=int(input("Choose a Subject/operation : "))
################## DATA INPUT FOR DSP ####################################
        if m==1:
            if t1==-1:
                print("Entering Digital Signal Processing Marks")
                t1=sub_score_lab()
                print("Your total score in Digital Signal Processing : ",t1)
            else:
                y=str(input("Values have been appended for DSP.Do you wish to overwrite(Y/N)"))
                if y.upper()=='Y':
                    print("Entering Digital Signal Processing Marks")
                    t1=sub_score_lab()
                    print("Your total score in Digital Signal Processing : ",t1)
                elif y.upper()=='N':
                    continue
                else:
                    print("")
                    print("INVALID INPUT")
################## DATA INPUT FOR PCS ####################################
        elif m==2:
            if t2==-1:
                print("Entering Process Control System")
                t2=sub_score_lab()
                print("Your total score in Process Control System : ",t2)
            else:
                y=str(input("Values have been appended for PCS.Do you wish to overwrite(Y/N)"))
                if y.upper()=='Y':
                    print("Entering Process Control System Marks")
                    t1=sub_score_lab()
                    print("Your total score in Process Control System : ",t2)
                elif y.upper()=='N':
                    continue
                else:
                    print("")
                    print("INVALID INPUT")
################## DATA INPUT FOR TNI ####################################
        elif m==6:
            if t6==-1:
                print("Entering Transducers and Instrumentations")
                t6=sub_score_lab()
                print("Your total score in Transducers and Instrumentation : ",t6)
            else:
                y=str(input("Values have been appended for TNI.Do you wish to overwrite(Y/N)"))
                if y.upper()=='Y':
                    print("Entering Transducers and Instrumentations")
                    t6=sub_score_lab()
                    print("Your total score in Transducers and Instrumentation : ",t6)
                elif y.upper()=='N':
                    continue
                else:
                    print("")
                    print("INVALID INPUT")
################## DATA INPUT FOR CST ####################################
        elif m==3:
            if t3==-1:
                print("Entering Communication Systems")
                t3=sub_score()
                print("Your total score in Communication Systems: ",t3)
            else:
                y=str(input("Values have been appended for CST.Do you wish to overwrite(Y/N)"))
                if y.upper()=='Y':
                    print("Entering Communication Systems")
                    t3=sub_score()
                    print("Your total score in Communication Systems: ",t3)
                elif y.upper()=='N':
                    continue
                else:
                    print("")
                    print("INVALID INPUT")
################## DATA INPUT FOR PE1 ####################################
        elif m==4:
            if t4==-1:
                print("Entering Program ELective 1[python/C++] Marks")
                t4=sub_score()
                print("Your total score in Program ELective 1[python/C++] : ",t4)
            else:
                y=str(input("Values have been appended for PE1.Do you wish to overwrite(Y/N)"))
                if y.upper()=='Y':
                    print("Entering Program ELective 1[python/C++] Marks")
                    t4=sub_score()
                    print("Your total score in Program ELective 1[python/C++] : ",t4)
                elif y.upper()=='N':
                    continue
                else:
                    print("")
                    print("INVALID INPUT")
################## DATA INPUT FOR PE2 ####################################
        elif m==5:
            if t5==-1:
                print("Entering Program ELective 2[Product development Technologies/Analytical instrumentation] Marks")
                t5=sub_score()
                print("Your total score in Program ELective 2[Product development Technologies/Analytical instrumentation]] : ",t5)
            else:
                y=str(input("Values have been appended for PE2.Do you wish to overwrite(Y/N)"))
                if y.upper()=='Y':
                    print("Entering Program ELective 2[Product development Technologies/Analytical instrumentation] Marks")
                    t5=sub_score()
                    print("Your total score in Program ELective 2[Product development Technologies/Analytical instrumentation]] : ",t5)
                elif y.upper()=='N':
                    continue
                else:
                    print("")
                    print("INVALID INPUT")
################## DATA INPUT FOR IFE ####################################
        elif m==7:
            if t7==-1:
                print("Entering Inovation for Enterprenuership Marks")
                t7=sub_score()
                print("Your total score in Inovation for Enterprenuership : ",t7)
            else:
                y=str(input("Values have been appended for IFE.Do you wish to overwrite(Y/N)"))
                if y.upper()=='Y':
                    print("Entering Inovation for Enterprenuership Marks")
                    t7=sub_score()
                    print("Your total score in Inovation for Enterprenuership : ",t7)
                elif y.upper()=='N':
                    continue
                else:
                    print("")
                    print("INVALID INPUT")
################## COMPUTE TOTAL MARKS AND GRADE  ####################################            
        elif m==8:
            if t1!=-1 and t2!=-1 and t3!=-1 and t4!=-1 and t5!=-1 and t6!=-1 and t7!=-1:
                tot=((t1+t2+t3+t4+t5+t6+t7)/350)*100
                print("TOTAL PERCENTAGE = ",tot," %")
                print("GRADE = ",end="")
                if tot>90:
                    print(" grade = S")
                elif tot>80 and tot<90:
                    print(" grade = A")
                elif tot>70 and tot<80:
                    print(" grade = B")
                elif tot>60 and tot<70:
                    print(" grade = C")
                elif tot>50 and tot<60:
                    print(" grade = D")
                elif tot>40 and tot<50:
                    print(" grade = E")
                else:
                    print(" grade = F")
                exit()
            else:
                print("")
                print("ALL VALUES ARE NOT ENTERED . PLEASE ENTER TO COMPUTE GRADE")
                print("")
        else:
            print("INVALID INPUT")
##########################################################################




