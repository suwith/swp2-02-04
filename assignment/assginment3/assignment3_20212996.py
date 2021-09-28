import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")

        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            except:
                print("Invalid order: please Enter it in order of name, age, and score.")

        elif parse[0] == 'del':
            try:
                for p in scdb:
                    for i in scdb:
                        if p['Name'] == parse[1]:
                            scdb.remove(p)
                        break
            except:
                print("Invalid name: " + parse[1])
            else:
                print("Invalid name is none")

        elif parse[0] == 'show':
            try:
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            except:
                print("Invalid command: " + parse[1])

        # 주어진 name의 사람만 찾아서 출력
        elif parse[0] == 'find':
            try:
                for p in scdb:
                    for j in scdb:
                        if p['Name'] == parse[1]:
                            for attr in sorted(p):
                                print(attr + "=" + p[attr], end=' ')
                            print()
                        else: print("name is none")
                        break
            except:
                print("name is none")
            else:
                print("Invalid name: " + parse[1])

        # 주어진 name의 사람만 찾아서 score를 amount만큼 더해줌
        elif parse[0] == 'inc':
            try:
                for p in scdb:
                    for i in scdb:
                        if p['Name'] == parse[1]:
                            amount = parse[2]
                            p['Score'] = str(int(p['Score']) + int(amount))
                        break
            except:
                print("name or amount is none")
            else:
                print("Invalid name : " + parse[1])
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
