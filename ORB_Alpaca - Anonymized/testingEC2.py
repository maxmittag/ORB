import pandas as pd
from getLiveData import fetchData, getCash

Cash = getCash()

Stocklist = pd.DataFrame(columns=["Ticker", "opening Price", "closing Price", "5min. High", "5min. Low", "ATV 14 days / day", "ATR 14 days", "ORV 14 days", "ORV 5 min.", "rel. ORV"])

df = pd.read_csv('stocklist_full_processed.csv', header=None, names=['Symbols'])

Stocklist["Ticker"] = df["Symbols"]

symbols_str = "%2C".join(Stocklist["Ticker"].astype(str).tolist())

TickerNumber = 1390

#REMOVE BELOV
symbols_str = "%2C".join(Stocklist["Ticker"].astype(str).tolist()[:TickerNumber])

Stocklist = fetchData(symbols_str, Stocklist.head(TickerNumber))

Stocklist.to_csv("Stocklist_TEST.csv", index=False, encoding="utf-8")

print(Cash)
print(len(Stocklist))