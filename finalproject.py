import requests
import csv

playerdata = open('middata.csv', 'w')
playerdatawriter = csv.writer(playerdata)
playerdatawriter.writerow(['kda','10mlh'])

url = 'https://api.opendota.com/api/'
r1 = requests.get(url+'proMatches')

matchid = r1.json()
num = range(1,10)
for n in num:
    number = matchid[n]['match_id']

    r = requests.get(url+'matches/'+ str(number))

    data = r.json()

    playernumber = 0
    while playernumber <= 9:
        playerlane= data['players'][playernumber]['lane']
        if playerlane == 2:
            kda = (data['players'][playernumber]['kda'])
            lh = (data['players'][playernumber]['lh_t'][10])
            playerdatawriter.writerow([kda,lh])
        playernumber += 1
    playerdatawriter.writerow(['done'])
