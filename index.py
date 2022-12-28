from flask import Flask, render_template
from riotwatcher import LolWatcher, ApiError
from operator import itemgetter, attrgetter

app = Flask(__name__)
# golbal variables
api_key = 'RGAPI-8ccb5abf-49ce-4bd4-be3c-27c52452a7cd'
watcher = LolWatcher(api_key)
my_region = 'la1'

headings = ('Invocador', 'Cuenta', 'Liga','Division','PL', 'Partidas', 'Victorias', 'Derrotas', 'Winrate')
nick = [
    'DanAT',
    'OtpYummiJg',
    'Arima Shuffle',
    'PasteIitoJunior',
    'BenitoCämeläs',
    'NoMeDejesPlis',
    'cake124',
    'SEBASTIÁM',
    'littledrusos',
    'BabyCGAKey'
]

datosi = []
for i in range(0, len(nick)):
    me = watcher.summoner.by_name(my_region, nick[i])
    stats = watcher.league.by_summoner(my_region, me['id'])
    for elem in stats:      #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        for k,v in elem.items():        #accedemos a cada llave(k), valor(v) de cada diccionario
            if k == 'tier':
                tier = v  
                if tier == 'IRON':
                    tier = '6IRON'
                if tier == 'BRONZE':
                    tier = '5BRONZE'
                if tier == 'SILVER':
                    tier = '4SILVER'
                if tier == 'GOLD':
                    tier = '3GOLD' 
                if tier == 'PLATINUM':
                    tier = '2PLATINUM' 
                if tier == 'DIAMOND':
                    tier = '1DIAMOND' 
            if k == 'rank':
                rank = v   
            if k == 'leaguePoints':
                lp = v    
            if k == 'wins':
                wins = v   
            if k == 'losses':
                losses = v   
        if nick[i] == 'DanAT':
            name = 'Atara'
        if nick[i] == 'OtpYummiJg':
            name = 'Andrés'
        if nick[i] == 'Arima Shuffle':
            name = 'Chiky'
        if nick[i] == 'PasteIitoJunior':
            name = 'Holman'
        if nick[i] == 'BenitoCämeläs':
            name = 'JuanDa'
        if nick[i] == 'NoMeDejesPlis':
            name = 'Marlon'
        if nick[i] == 'cake124':
            name = 'Miguel'
        if nick[i] == 'SEBASTIÁM':
            name = 'Sebastián'
        if nick[i] == 'littledrusos':
            name = 'Villa'
        if nick[i] == 'BabyCGAKey':
            name = 'William'
        name = str(name)
        cant = wins + losses
        wr = (wins / cant)*100
        cant = str(cant)
        winrate = str(round(wr, 2))
        tier = str(tier)  
        rank = str(rank)  
       # lp = -lp
        lp = str(lp)  
        wins = str(wins)  
        losses = str(losses)  
        data = (name, nick[i], tier, rank, lp, cant, wins, losses, winrate)
        datosi.append(data)

datosi = sorted(datosi, key=itemgetter(2 , 3, 4))
print(datosi)

@app.route('/')
def home():
    return render_template('index.html', headings = headings, datosi = datosi)
# # Permite ejecutar el archivo como el main
if __name__ == '__main__':
    app.run(debug=True)
