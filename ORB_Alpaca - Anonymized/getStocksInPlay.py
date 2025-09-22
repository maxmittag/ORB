import pandas as pd
import getKPIs as getKPI

# Leeres DataFrame mit diesen Spalten
#Stocklist = pd.DataFrame(columns=["Ticker", "opening Price", "ATV 14 days / day", "ATR 14 days", "ORV 14 days", "ORV 5 min.", "rel. ORV"])
#Stocklist.loc[len(Stocklist)] = ['AAPL', None, 0, 0, 0, 0, 0]
#print(Stocklist)

# Preprocessing
def filterStocksInPlay_preOpen(Stocklist):
    #fetch Ticker Symbols #shortened_stocklist_full_processed
    df = pd.read_csv('stocklist_full_processed.csv', header=None, names=['Symbols'])
    #Durch Ticker iterieren
    i=0
    
    for ticker in df['Symbols']:
        #Fill 14 days daily ATV
        try:
            Daily_ATV_14days = getKPI.get_Daily_ATV_14days(ticker)
            #Fill ATR 14 days
            ATR_14Days = getKPI.get_ATR_14days(ticker)
            #get 14 days 5-min. ORV
            historic_ORV = getKPI.get_historical_Average_ORVolume(ticker)
            if(Daily_ATV_14days > 1000000 and ATR_14Days > 0.5):
                Stocklist.loc[len(Stocklist)] = [ticker, None, None, None, None, Daily_ATV_14days, ATR_14Days, historic_ORV, None, None]
            
                
        except Exception as e:
            print(f"{ticker}: Fehler ({e}) - übersprungen.")
            continue
        if((i % 20)==0):
            print(round(((i/len(df))*100),2), "% preloading done")
            #print(Stocklist)
        i+=1
    # 2.Average Trading Volume above 1M/day
    # 3.ATR (14 days) > 0.50$

    #Add in output: output_df.loc[len(output_df)] = ['AAPL']
    return Stocklist




















def filterStocksInPlay(Tickerlist):
    output_df = pd.DataFrame({'ticker symbol'})
    # 1.Price above 5$
    # 2.Average Trading Volume above 1M/day
    # 3.ATR (14 days) > 0.50$
    # 4.Relative Volume > 100%
    #
    #
    #
    #
    #Add in output: output_df.loc[len(output_df)] = ['AAPL']
    return