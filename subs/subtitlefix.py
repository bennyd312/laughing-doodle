#This programme fixes subtitles by adjusting the time when the subtitle is played.

difference = int(input("What is the time difference between subtitle and audio?: "))
difference = 9 #House of the dragon s1e2

file = open("subtitle.txt", "r", encoding = "utf8")
newfile = open("newsubtitle.txt", "w", encoding = "utf8")

lines = file.readlines()

def fixline(line,time):#adjusts the start or end time of a single line

    line[5]+=time

    for i in range(len(line)-3):
        if (5-i)%2==1:
            
            if line[5-i]//10!=0:
                line[5-i-1]+=1
                line[5-i]= line[5-i]%10
            else:
                break
            
        else:

            if line[5-i]//6!=0:
                line[5-i-1]+=1
                line[5-i] = line[5-i]%6
            else:
                break
    return line


def fixsub(line,time): 
    
    baseline = [i for i in line]# splits the line into individual characters
    numbersonly = [int(i) for i in line if i.isdigit()] #takes the numbers (time) from the original line
    starttime = fixline(numbersonly[:9],time) #time when the subtitle starts playing
    endtime = fixline(numbersonly[9:],time) # ends playing
    
    j=0
    
    time = starttime
    
    for i in endtime:
        time.append(i)

    for i in time:
        
        while True:
            
            if baseline[j].isdigit():
                
                baseline[j] = str(i)
                j+=1
                break
            
            else:
                
                j+=1

            
    finalline = "".join(baseline)
    return finalline

for i in range(len(lines)):
    if (i+1)%4==2:
        newfile.write(fixsub(lines[i],9))
    else:
        newfile.write(lines[i])

print("Finished")
file.close()
newfile.close()










