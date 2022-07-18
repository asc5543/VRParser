import urllib.request
from team import legendTeam
from team import teamStatistics
from html.parser import HTMLParser

class VRTeamParser(HTMLParser):

    def __init__(self, *, convert_charrefs=True):
        """Initialize and reset this instance.
        If convert_charrefs is True (the default), all character references
        are automatically converted to the corresponding Unicode characters.
        """
        self.convert_charrefs = convert_charrefs
        self.reset()
        self.target = False
        self.teamRecord = False
        self.teamList = []
        self.team = []
       
    def handle_starttag(self, tag, attrs):
    
        # Team and Result section start
        if tag == 'span':
            if ('class','elementor-divider-separator') in attrs:
                if not self.target:
                    self.target = True
                else:
                    self.target = False
                    self.teamRecord = True
                   
        # Team Record
        if tag == 'img' and self.target:
            if ('class','lazyload') in attrs:
                for attr in attrs:
                    if attr[0] == 'alt':
                        if attr[1] and not self.teamRecord:
                            self.team.append(attr[1].capitalize())
                            break
        if len(self.team) == 6:
            self.teamList.append(self.team)
            #print(self.team)
            self.team = []

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass
       
def teamParser(data):
    parser = VRTeamParser()
    parser.feed(data)
    return parser.teamList
    
def VRParser(URL):    
    webUrl = urllib.request.urlopen(URL)
    teamList = []
    if webUrl.getcode() == 200:
        data = webUrl.read().decode('utf-8')
        teamList = teamParser(data)
    else:
        print("Error!")
    
    Event = URL.split(r'/')[-2].capitalize()
    #print(Event)
    return teamList
        
if __name__ == '__main__':
    f = open("urllist.txt")
    urlList = ""
    if f.mode == 'r':
        urlList = f.read().split("\n")
    f.close()
    teamAnalyze = teamStatistics()
    teamList = []
    for url in urlList:
        if url:
            teamList += VRParser(url)
    for team in teamList:
        tempTeam = legendTeam(team)
        teamAnalyze.appendTeam(tempTeam)
        
    teamAnalyze.sortData()
    teamAnalyze.saveData('JuneResult.txt')