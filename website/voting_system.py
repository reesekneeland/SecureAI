import json

class VotingSystem:
    
    def __init__(self, fl):
        self.fl = fl
        with open(self.fl, 'r') as file:
            self.db = json.load(open(file))

    def winnerImage(self):
        winners = 1
        if len(self.db) == winners: return self.img_dbSample(winners, sort=True, ascending=False)
        else:
            for tup in list(self.db.items())[1:]:
                if tup[1][0] == list(self.db.values())[0][0]: winners += 1
                else: break
        return self.img_dbSample(winners, sort=True, ascending=False)

    # Getting the first num images and their corresponding rating averages
    # returns a dictionary
    def img_dbSample(self, num, sort=False, ascending=True):
        db_list = list()
        if sort:
            if ascending: db_list = list(dict(sorted(self.db.items(), key = lambda x:x[1][0])).items())
            else: db_list = list(dict(sorted(self.db.items(), key = lambda x:x[1][0]), reverse = True).items())
        else: db_list = list(self.db.items())
        return dict(db_list[:num])

    def addImage(self, img, ave, num, stren):
        self.db[img] = (ave, num, stren)
        with open(self.fl, 'w') as file:
            json.dump(self.db, file)
        

    def updateImage(self, img, ave, num, stren, rm=False):
        if not rm: self.db[img] = (((self.db[img][0] + ave) // self.db[img][1] + num), self.db[img][1] + num, stren)
        elif rm == True: self.db.pop(img)
        else: print('Command is prohibited.')
        with open(self.fl, 'w') as file:
            json.dump(self.db, file)

    def getImageRate(self, img):
        return self.db[img][0]

    def getImageStrength(self, img):
        return self.db[img][2]

    def getImageTotalVotes(self, img):
        return self.db[img][1]

    def getTotalImages(self):
        return len(self.db)