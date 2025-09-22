import requests
import pandas as pd
import numpy as np
from datetime import date

def fetchData(Symbols, Dataframe):
    today_str = date.today().strftime("%Y-%m-%d")

    url = (
        "https://data.alpaca.markets/v2/stocks/bars?symbols="
        + Symbols
        + "&timeframe=5Min&start="
        + today_str
        + "T13%3A30%3A00.000000000Z&end="
        + today_str
        + "T13%3A34%3A59.999999999Z&limit=10000&adjustment=raw&feed=sip&currency=USD&sort=asc"
    )

    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": "PKMSTQ6SAGZVGWQ9D34N",
        "APCA-API-SECRET-KEY": "uU57dokEzdmfxg6SRQh8hkuI4QC0SFE4oVbT23Wj",
    }

    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    data = r.json()

    for ticker, bars in data.get("bars", {}).items():
        if not bars:
            continue
        b = bars[0]
        new_values = {
            "opening Price": b.get("o", np.nan),
            "closing Price": b.get("c", np.nan),
            "5min. High": b.get("h", np.nan),
            "5min. Low": b.get("l", np.nan),
            "ORV 5 min.": b.get("v", np.nan),
        }

        # nur updaten, wenn Ticker existiert
        mask = Dataframe["Ticker"] == ticker
        if mask.any():
            for col, val in new_values.items():
                Dataframe.loc[mask, col] = val
                
    Dataframe["rel. ORV"] = Dataframe["ORV 5 min."] / Dataframe["ORV 14 days"]
    
    Dataframe = Dataframe.sort_values(by="rel. ORV", ascending=False).reset_index(drop=True)
    
    return Dataframe

def getCash():
    url = "https://paper-api.alpaca.markets/v2/account"

    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": "SECRET",
        "APCA-API-SECRET-KEY": "SECRET"
    }

    response_cash = requests.get(url, headers=headers)

    # JSON-Antwort in Python-Dict umwandeln
    data = response_cash.json()

    # Nur den Cash-Wert zurückgeben
    return float(data["cash"])