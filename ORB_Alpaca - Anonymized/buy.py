import requests
import math

def buy(symbol: str, price: float, SL: float, amount: int):
    
    try:
        limit_price = str(round(price*20, 2))
        SL = str(round(SL, 2))
        price = str(round(price, 2))
        amount = str(amount)
        
        #API REQUEST
        url = "https://paper-api.alpaca.markets/v2/orders"

        payload = {
            "type": "limit",
            "time_in_force": "day",
            "take_profit": { "limit_price": limit_price },
            "stop_loss": {
                "stop_price": SL,
                "limit_price": SL
            },
            "symbol": symbol,
            "qty": amount,
            "side": "buy",
            "limit_price": price,
            "order_class": "bracket",
            "extended_hours": False
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "APCA-API-KEY-ID": "PKMSTQ6SAGZVGWQ9D34N",
            "APCA-API-SECRET-KEY": "uU57dokEzdmfxg6SRQh8hkuI4QC0SFE4oVbT23Wj"
        }
        response = requests.post(url, json=payload, headers=headers)
        
    except:
        print("Es gab einen TypeError:")

def sell(symbol: str, price: float, SL: float, amount: int):
    
    try:
        limit_price = str(round(price * 0.1 , 2))
        SL = str(round(SL, 2))
        price = str(round(price, 2))
        amount = str(amount)
        
        #API REQUEST
        url = "https://paper-api.alpaca.markets/v2/orders"

        payload = {
            "type": "limit",
            "time_in_force": "day",
            "take_profit": { "limit_price": limit_price },
            "stop_loss": {
                "stop_price": SL,
                "limit_price": SL
            },
            "symbol": symbol,
            "qty": amount,
            "side": "sell",
            "limit_price": price,
            "order_class": "bracket",
            "extended_hours": False
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "APCA-API-KEY-ID": "PKMSTQ6SAGZVGWQ9D34N",
            "APCA-API-SECRET-KEY": "uU57dokEzdmfxg6SRQh8hkuI4QC0SFE4oVbT23Wj"
        }

        response = requests.post(url, json=payload, headers=headers)
        
    except:
        print("Es gab einen TypeError:")
      


def execute_buys_and_sells(Stocklist_input, cash):    
    i = 0
    while(i<len(Stocklist_input)):
        #print(Stocklist.iloc[i]["opening Price"])
        #Fehler abfangen
        if(Stocklist_input.iloc[i]["opening Price"]!=None and Stocklist_input.iloc[i]["closing Price"]!=None and Stocklist_input.iloc[i]["5min. High"]!=None):
            #Wenn bullish LONG
            if(Stocklist_input.iloc[i]["closing Price"] > Stocklist_input.iloc[i]["opening Price"]):
                #try:
                    SL = round(Stocklist_input.iloc[i]["5min. High"] - 0.1*Stocklist_input.iloc[i]["ATR 14 days"],2)
                    #   amount = cash * 0.01 / ATR 14 * 0.1       (Amount = $-Amount)
                    Dollar_amount = (cash * 0.01) / (Stocklist_input.iloc[i]["ATR 14 days"] * 0.1)
                    amount = int(math.floor(Dollar_amount/Stocklist_input.iloc[i]["5min. High"]))
                
                    buy(Stocklist_input.iloc[i]["Ticker"],Stocklist_input.iloc[i]["5min. High"], SL, amount)
                    print("Kaufe " + str(amount) + "x " + Stocklist_input.iloc[i]["Ticker"],  "zu ", str(Stocklist_input.iloc[i]["5min. High"]))
                #except:
                    #print("Fehler beim KAUFEN von: ", Stocklist_input.iloc[i]["Ticker"])
                
            #Wenn bearish SHORT
            if(Stocklist_input.iloc[i]["closing Price"] < Stocklist_input.iloc[i]["opening Price"]):
                #try:
                    SL = round(Stocklist_input.iloc[i]["5min. Low"] + 0.1 * Stocklist_input.iloc[i]["ATR 14 days"],2)
                    #   amount = cash * 0.01 / ATR 14 * 0.1       (Amount = $-Amount)
                    Dollar_amount = (cash * 0.01) / (Stocklist_input.iloc[i]["ATR 14 days"] * 0.1)
                    amount = int(math.floor(Dollar_amount/Stocklist_input.iloc[i]["5min. High"]))
                    sell(Stocklist_input.iloc[i]["Ticker"],Stocklist_input.iloc[i]["5min. Low"], SL, amount)
                    print("Verkaufe " + str(amount) + "x " + str(Stocklist_input.iloc[i]["Ticker"]),  "zu ", str(Stocklist_input.iloc[i]["5min. Low"]))
                #except:
                    #print("Fehler beim VERKAUFEN von: ", Stocklist_input.iloc[i]["Ticker"])
        i+=1
    
    
    
#Cash = getCash()
#print(Cash)
#buy("AAPL", 214.31, 210.00, 2)
#sell("AAPL", 214.31, 218.10, 1)