import yfinance as yf
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


# Historical ORVolume 5 min.
def get_historical_Average_ORVolume(ticker):
    # Fetch 5-min-Data for 14 days
    df = yf.download(ticker, period='14d', interval='5m', progress=False)
    df = df.tz_convert('America/New_York')
    df_first5 = df.between_time('09:30', '09:34')
    Vol_Sum_14Days = df_first5['Volume'].sum()
    Historical_Average_ORVolume = Vol_Sum_14Days/14
    return round((Historical_Average_ORVolume.iloc[0]),2)


# Historical Average Trading Volume Daily 14 days
def get_Daily_ATV_14days(ticker):
    df = yf.download(ticker, period='14d', interval='1d', progress=False)
    #print(df['Volume'])
    Vol_Sum_14Days = df['Volume'].sum()
    Historical_Average_Daily_Volume = Vol_Sum_14Days/14
    return round((Historical_Average_Daily_Volume.iloc[0]),2)   


def get_ATR_14days(ticker):
    # Load Data with explicit Columns
    data = yf.download(ticker, period="16d", progress=False)[['High', 'Low', 'Close']]
    data = data.iloc[::-1]
    
    i = 0
    TRsum = 0
    while i<14:
        #print(data.iloc[i])
        #Current High — Current Low
        TR1 = data.iloc[i]['High'] - data.iloc[i]['Low']
        #|Current High — Previous Close|
        TR2 = abs(data.iloc[i]['High'] - data.iloc[i+1]['Close'])
        #|Current Low — Previous Close|
        TR3 = abs(data.iloc[i]['Low'] - data.iloc[i+1]['Close'])
        
        TRsum += max([TR1.sum(), TR2.sum(), TR3.sum()])
        i+=1
    return round((TRsum/14), 2)

#print(get_historical_Average_ORVolume("AAPL"))