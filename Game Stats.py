#This program keeps track of your game stats, ie how many times you placed
#1st, 2nd, 3rd, etc. It can even save the results to a file for future reference.

#Written by Ian Schwartz
MAX = 64 #change as needed
num = input(("How many places are there (2-" + str(MAX) + ")? "))
try:
    num = int(num)
except ValueError:
    print ("That's not a number... :(")
else:
    if ((num < 2) | (num > MAX)):
        print ("Out of Range :(")
    else:
        names = []
        places = []
        games = 0
        if (num == 2):
            names = ["Wins: ","Losses: "]
            places = [0, 0]
        else:
            i = 0
            while (i < num):
                places.append(0)
                if (i==0):
                    names.append("1st: ")
                elif (i==1):
                    names.append("2nd: ")
                elif (i==2):
                    names.append("3rd: ")
                else:
                    names.append(str(i+1)+"th: ")
                i += 1
        cin = ""
        while ((cin != 'q') & (cin != 'Q')):
            try:
                int(cin)
            except ValueError:
                #cin is NaN
                if (((cin == 's') | (cin == 'S')) & (games != 0)):
                    #save stats
                    from datetime import date
                    now = date.today()
                    File = open('Stats/' + now.strftime('%y-%m-%d') + '.txt','a')
                    game = raw_input("Which game is this? ")
                    File.write(game + " stats:\n")
                    i = 0
                    while (i < num):
                        File.write(names[i] + "\t" + str(places[i]) + "\t" + str(int((float(places[i])/games)*100)) + "%\n")
                        i += 1
                    File.write("Total Games: " + str(games) + "\n\n")
                    File.close()
                elif ((cin == 'n') | (cin == 'N')):
                    #new stats
                    games = 0
                    i = 0
                    while (i < num):
                        places[i] = 0
                        i += 1
                #maybe load later
                elif (((cin == 'w') | (cin == 'W')) & (num == 2)):
                    places[0] += 1
                    games += 1
                elif (((cin == 'l') | (cin == 'L')) & (num == 2)):
                    places[1] += 1
                    games += 1
                else:
                    "Do nothing"
            else:
                #cin IS a number
                cin = int(cin)
                if((cin > 0) & (cin <= num)):
                    #the number is between 1 & num
                    places[cin-1] += 1
                    games += 1
                else:
                    "Do nothing"
            #display
            if(games != 0):
                i = 0
                while (i < num):
                    print (names[i] + "\t" + str(places[i]) + "\t" + str(int((float(places[i])/games)*100)) + "%")
                    i += 1
            else:
                i = 0
                while (i < num):
                    print (names[i] + "\t" + str(places[i]) + "\t0%")
                    i += 1
            print ("Total games: " + str(games) + " ")
            cin = input("")
