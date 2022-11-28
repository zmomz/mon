import telegram
from config import telegram_token, chat_id
import yfinance as yf
from datetime import datetime

# telegram_bot = telegram.Bot(telegram_token)
messages = []



def is_unique(symbol, side):
    """
    - returns True if the symbol with the same side is not registered already in 
      the above messages list, and otherwise returns False. 
    - it also updates the messages list of the current status.

    messages list should look something like this ...

    messages = [{symbol:"AAPL", time: "2022-11-28 19:09:28.571212", side: "long"},
                {symbol:"GOOG", time: "2022-11-29 23:01:10.312345", side: "short"},
                ....]
    """

def get_price(symbol, timeframe, period):
   
    data = 0
    """
    use yfinance to get the candle data of the inputed ticker (symbol)
    and return the data
    """
    return data

def stoploss(data, side, signal_price):
    pass

def find_targets(data, side, signal_price, k):
    pass

def create_message(side, symbol, signal_price, targets, leverage, stoploss):
    pass
    """
    dynamically create a message string that look like this:
    # if side = Long
    message =

    '''
    (ISOLATE)
    LONG / SPOT 
    LEVERAGE: 5x
    • AAPL •

    Entry Price: 145
    STOPLOSS: 142 
    TARGET 

    150 
    154 
    160 
    '''
    or this:
    elif side = Short
    message =
    '''
    (ISOLATE)
    SHORT 
    LEVERAGE: 5x
    • AAPL •

    Entry Price: 145
    STOPLOSS: 150 
    TARGET 

    143 
    140 
    137 
    '''
        * notice the differance between long & short sides,
         targets are ascending when side is Long, and stoploss is smaller than entry price,
         while if side is Short, targets are descending and stoploss is bigger than entry price.
    """


def send_message(text):
    """
    setup the telegram bot using the chat_id, and the telegram_token
    then use the bot to send the message to the telegram group
    ... all configurations must be set in the config.py file
    """
    pass
