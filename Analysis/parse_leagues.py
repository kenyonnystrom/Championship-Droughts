import sys

# Format to run:
# python3 [MLB path] [NBA path] [NFL path] [NHL path]

MLB = sys.argv[1]
NBA = sys.argv[2]
NFL = sys.argv[3]
NHL = sys.argv[4]

perHubOut = open('RegionalStats.csv', 'w')
allTeamOut = open('TeamStats.csv', 'w')

hubs = {}
for f in (MLB,NBA,NFL,NHL):
    league = open(f, 'r')
    next(league)
    for row in league:
        line = row.split("\n")[0].split(",")
        if line[0] not in hubs:
            hubs[line[0]] = [[f.split("/")[-1][:-4]] + line[1:]]
        elif hubs[line[0]] is not None:
            hubs[line[0]] += [[f.split("/")[-1][:-4]] + line[1:]]
    league.close()

perHubOut.write("Regional Hub,Teams,Last Chip,Fr. Years Since\n")
allTeamOut.write("Regional Hub,Team,Fr. Years Since Last Chip\n")

for key in hubs.keys():
    perHubOut.write("{},{},".format(key, len(hubs[key])))
    mostRecent = 0
    for team in hubs[key]:
        mostRecent = max(int(team[3]), mostRecent)
        #if key == "Los Angeles":
        #    print(int(team[3]), mostRecent)
    cumFranYears = 0
    for team in hubs[key]:
        cumFranYears += min(2023 - mostRecent, 2023 - int(team[2]))
        allTeamOut.write("{},{},{}\n".format(key, team[1], min(2023 - mostRecent, 2023 - int(team[2]))))
    perHubOut.write("{},{}\n".format(mostRecent, cumFranYears))

perHubOut.close()
allTeamOut.close()
