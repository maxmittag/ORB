import pandas as pd
import yfinance as yf

# CSV einlesen
df = pd.read_csv("stocklist_full.csv", header=None, names=['Symbols'])

# Liste für die gefilterten Symbole
filtered_symbols = []
i = 0
# Jede Zeile durchgehen
for symbol in df["Symbols"]:
    print(i, "/4606")
    hist = yf.download(symbol, period="1d", interval="1d", progress=False)[['Close']]
    # Vortagesschlusskurs holen
    if(hist["Close"].iloc[0].sum()>=3.5):
        filtered_symbols.append(symbol)
    i+=1

# Als DataFrame speichern
filtered_df = pd.DataFrame({"Symbol": filtered_symbols})

# Neue CSV schreiben
filtered_df.to_csv("shortened_stocklist_full_2.csv", index=False)