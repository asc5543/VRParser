class legendTeam():
    def __init__(self):
        self.team = []
        self.LegendCore = []
        
    def __init__(self, team):
        self.team = []
        self.LegendCore = sorted(team[:2])
        self.team = self.LegendCore + sorted(team[2:])
        self.LegendCore = tuple(self.LegendCore)
        self.team = tuple(self.team)
    
    def __repr__(self):
        return "This is object of team"
    
    def __str__(self):
        return "Team: " + str(self.team)
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.getTeam() == other.getTeam()
        else:
            return False

    def getTeam(self):
        return self.team
            
    def getLegendCore(self):
        return self.LegendCore
        
class teamStatistics():
    def __init__(self):
        self.dictCoreCount = {}
        self.dictTeamCount = {}
    
    def appendTeam(self, team):
    
        # Init
        if not team.getLegendCore() in self.dictCoreCount:
            self.dictCoreCount[team.getLegendCore()] = 1
            self.dictTeamCount[team.getLegendCore()] = {}
            self.dictTeamCount[team.getLegendCore()][team.getTeam()] = 1
        
        else:
            self.dictCoreCount[team.getLegendCore()] += 1
            if not team.getTeam() in self.dictTeamCount[team.getLegendCore()]:
                self.dictTeamCount[team.getLegendCore()][team.getTeam()] = 1
            else:
                self.dictTeamCount[team.getLegendCore()][team.getTeam()] += 1
                
    def __str__(self):
        print("[Core Count]")
        for core in self.dictCoreCount:
            print(core, ":", self.dictCoreCount[core])
        print("\n[Team Count]")
        for key in self.dictCoreCount:
            print('[', key, ']')
            for subkey in self.dictTeamCount[key]:
                print(subkey, ",", self.dictTeamCount[key][subkey])
            print()
        return ""

    def sortData(self):
        self.dictCoreCount = dict(sorted(self.dictCoreCount.items(), key=lambda item: item[1], reverse=True))
        for core in self.dictCoreCount:
            self.dictTeamCount[core] = dict(sorted(self.dictTeamCount[core].items(), key=lambda item: item[1], reverse=True))
        
    def getCoreCount(self):
        return self.dictCoreCount
        
    def getCoreTeam(self, core):
        return self.dictTeamCount[core]
        
    def saveData(self, dist):
        f = open(dist, 'w')
        f.write("[Core Count]\n")
        for key in self.dictCoreCount:
            core = str(key).replace("(","").replace(")","").replace("'","")
            f.write(core + ":" + str(self.dictCoreCount[key])+ "\n")
        f.write("\n[Team Count]\n")
        for key in self.dictCoreCount:
            core = str(key).replace("(","").replace(")","").replace("'","")
            f.write(core+'\n')
            for subkey in self.dictTeamCount[key]:
                f.write(str(subkey).replace("(","").replace(")","").replace("'","")+ "," + str(self.dictTeamCount[key][subkey])+"\n")
            f.write("\n")
        f.close()
                
if __name__ == '__main__':
    member = ['Zacian-Crowned', 'Groudon', 'Incineroar', 'Gastrodon-East', 'Rotom-Heat', 'Thundurus']
    member2 = ['Zacian-Crowned', 'Kyogre', 'Incineroar', 'Gastrodon-East', 'Rotom-Heat', 'Thundurus']
    testTeam = legendTeam(member)
    testTeam2 = legendTeam(member2)

    NewteamStatistics = teamStatistics()
    NewteamStatistics.appendTeam(testTeam)
    NewteamStatistics.appendTeam(testTeam2)
    NewteamStatistics.sortData()
    print(NewteamStatistics.getCoreCount())