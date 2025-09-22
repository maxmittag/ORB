import pandas as pd
import getStocksInPlay as pre
from buy import execute_buys_and_sells
from sendMSG import sendMessage
from wait import wait_until
from getLiveData import fetchData, getCash

#_________________________________________________________________________________________________________
#                                        PRELOADING

sendMessage("preloading started!")

Stocklist = pd.DataFrame(columns=["Ticker", "opening Price", "closing Price", "5min. High", "5min. Low", "ATV 14 days / day", "ATR 14 days", "ORV 14 days", "ORV 5 min.", "rel. ORV"])

Stocklist = pre.filterStocksInPlay_preOpen(Stocklist)

Cash = getCash()

print("Cash available: " + str(Cash))

sendMessage("preloading done!")

#_________________________________________________________________________________________________________
#                                   FETCH LIVE DATA

symbols_str = "%2C".join(Stocklist["Ticker"].astype(str).tolist())

wait_until(13,50,10)


if(len(Stocklist)<1201):
    Stocklist = fetchData(symbols_str, Stocklist)

else:
    #TBD
    #Batches bilden
    
    symbols_str = "%2C".join(Stocklist["Ticker"].astype(str).tolist()[:1200])

    Stocklist = fetchData(symbols_str, Stocklist.head(1200))
    print("Liste war zu groß!!!" + len(Stocklist))
    
#_________________________________________________________________________________________________________
#                                        BUY & SELL

execute_buys_and_sells(Stocklist.head(20), Cash)

#_________________________________________________________________________________________________________
#                                      Postprocessing

Stocklist.to_csv("Stocklist_TEST_OUTPUT.csv", index=False, encoding="utf-8")

