import requests
from datetime import datetime
import json
from collections import Counter

GAMEID = 1100
if __name__ == '__main__':

    drawIds = []
    today = datetime.today().strftime('%Y-%m-%d')
    iter = today.split("-")[2]
    yymm = "-".join(today.split("-")[:2])


    def getData(url):
        r = requests.get(url)
        data = json.loads(r.text)
        return data

    for day in range(int(iter)):
        day = day+1

        if len(str(day))==1:
            date = f"{yymm}-0{day}"
        else:
            date = f"{yymm}-{day}"

        api = f"https://api.opap.gr/draws/v3.0/{GAMEID}/draw-date/{date}/{date}/draw-id"

        data = getData(api)
        drawIds.append(data)

    for x,day in enumerate(drawIds):
        winningNums = []

        for draw in day:

            api = f"https://api.opap.gr/draws/v3.0/{GAMEID}/{draw}"
            data = getData(api)
            winningNums.extend(data["winningNumbers"]["list"])

        c = Counter(winningNums)
        print(f"Most winning number is number {c.most_common(1)[0][0]} with {c.most_common(1)[0][1]} occurencies for day {x+1}")