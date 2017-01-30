import requests
import csv

playerdata = open('middata.csv', 'w')
playerdatawriter = csv.writer(playerdata)
playerdatawriter.writerow(['composite KDA/LH score'])

url = 'https://api.opendota.com/api/'
r1 = requests.get(url+'publicMatches?min_mmr=8150') #pulls a random sample of pub matches with an average mmr over 4000
matchid = r1.json()
num = range(1,1)
for n in num:
    number = matchid[n]['match_id']

    r = requests.get(url+'matches/'+ str(number))

    data = r.json()
    try:
        playernumber = 0 #radiant players
        mid_players = []
        while playernumber <= 4: #players 0-4 are on the radiant team
            playerlane= data['players'][playernumber]['lane'] #lana data for each player
            if playerlane == 2: # if the player's lane is 2, or midlane, continue
                kda = (data['players'][playernumber]['kda']) #a player's (kills+assists)/deaths, a benchmark for fighting
                lh = (data['players'][playernumber]['lh_t'][10]) #a player's number of creep kills at ten minutes, a benchmark for farming
                composite = (lh/10+kda) #a combination of farming/fighting that measures a player's overall effectiveness
                mid_players.append({'num':playernumber, 'kda':kda, 'lh':lh, 'composite':composite})
            playernumber += 1
        if len(mid_players) == 1:
            playerdatawriter.writerow([composite])
        elif len(mid_players) > 1:
            last = 0
            for player in mid_players:
                if player['lh'] > last:
                    last = player ['lh']
            playerdatawriter.writerow([composite])
        
        playernumber = 5 #dire players
        mid_players = []
        while playernumber <= 9: #players 5-9 are on the dire team
            playerlane= data['players'][playernumber]['lane'] #lana data for each player
            if playerlane == 2: # if the player's lane is 2, or midlane, continue
                kda = (data['players'][playernumber]['kda']) #a player's (kills+assists)/deaths, a benchmark for fighting
                lh = (data['players'][playernumber]['lh_t'][10]) #a player's number of creep kills at ten minutes, a benchmark for farming
                composite = (lh/10+kda) #a combination of farming/fighting that measures a player's overall effectiveness
                print(composite)
                mid_players.append({'num':playernumber, 'kda':kda, 'lh':lh, 'composite':composite})
            playernumber += 1
        if len(mid_players) == 1:
            playerdatawriter.writerow([composite])
        elif len(mid_players) > 1:
            last = 0
            for player in mid_players:
                if player['lh'] > last:
                    last = player ['lh']
            playerdatawriter.writerow([composite])
            
        winner = (data['radiant_win']) #provides true/false for radiant winning match
        playerdatawriter.writerow(['match ' + str(n), winner]) #match number
    except KeyError:
        print('notparsed')