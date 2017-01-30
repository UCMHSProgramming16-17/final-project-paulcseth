import requests
import csv

playerdata = open('middata.csv', 'w')
playerdatawriter = csv.writer(playerdata)
playerdatawriter.writerow(['composite KDA/LH score'])

url = 'https://api.opendota.com/api/'
r1 = requests.get(url+'proMatches') #pulls a random sample of pro matches (I would have preferred to use pubs, but most of those aren't parsed and I don't know that I can write a parse request into the code.)

matchid = r1.json()
num = range(1,100)
for n in num:
    number = matchid[n]['match_id']

    r = requests.get(url+'matches/'+ str(number))

    data = r.json()

    playernumber = 0 #radiant players
    while playernumber <= 4: #players 0-4 are on the radiant team
        playerlane= data['players'][playernumber]['lane'] #lana data for each player
        if playerlane == 2: # if the player's lane is 2, or midlane, continue
            kda = (data['players'][playernumber]['kda']) #a player's (kills+assists)/deaths, a benchmark for fighting
            lh = (data['players'][playernumber]['lh_t'][10]) #a player's number of creep kills at ten minutes, a benchmark for farming
            composite = (lh/15+kda) #a combination of farming/fighting that measures a player's overall effectiveness
            playerdatawriter.writerow([composite]) #write the composite number into the csv
        playernumber += 1
    
    playernumber = 5 #dire players
    while playernumber <= 9: #players 5-9 are on the dire team
        playerlane= data['players'][playernumber]['lane']
        if playerlane == 2:
            kda = (data['players'][playernumber]['kda'])
            lh = (data['players'][playernumber]['lh_t'][10])
            composite = (lh/10+kda)
            playerdatawriter.writerow([composite])
        playernumber += 1
    winner = (data['radiant_win']) #provides true/false for radiant winning match
    playerdatawriter.writerow(['match ' + str(n), winner]) #match number