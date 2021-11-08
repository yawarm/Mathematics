"""
Importing necessary libraries.
 - numpy: used to store values ​​in lists
 - talib: perform necessary calculations
 - binance: must be imported in order to take positions using binance
 - websocket: used to retrieve information about relevant crypto from binance
"""

import json, websocket, talib
import numpy as np
from binance.client import Client
from binance.enums import *
import config


#------------------------------------------------------------------------

"""
Defines required sizes. 
These are divided into two, constants and variables. 
Constants do not need to be changed, 
while variables must be adjusted according to use.
"""

#Constants

can_buy: bool = False #can buy tells whether one can buy or not
closes: list = [] #list of closing values
in_position: bool = False #Tells if you are in a position or not.
client = Client(config.API_KEY, config.API_SECRET) #create a client, using your binance api-key and api-secret-key
cycle: int = 0 #keeps track of how many closes there have been since the code started running
minimal_data_basis: int = 6 #for the calculations to make sense, we must have enough data-points. This variable makes sure of that.

#Variables
""" 
Initialize variables under
"""
trade_quantity: int = None #the position size (number of shares)
timeframe: int = None #timeframe
trade_symbol: str = None #crypto-pair (must be available in Binance)
SOCKET: str = f"wss://stream.binance.com:9443/ws/{trade_symbol}@kline_{timeframe}m" #Socket


#------------------------------------------------------------------------

"""
This is the function used to place an order.
Takes in parameters:
 - side: Buy/Sell
 - quantity: number of shares
 - symbol: crypto-pair
 - order_type: is a constant (can change if wanted), is set to market order.
"""
def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET) -> bool:
    global trade_quantity 
    try:
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
    except Exception as e:
        print(f"an exception occured - {e}")

        """ The error below can appear quite often. 
        An effective solution has proven to be to reduce the size of purchases. """

        if e == "an exception occured - APIError(code=-2010): Account has insufficient balance for requested action.":
            trade_quantity -= 0.12
    
    
        return False #return false if order was not executed
    return True #return true if order was executed


""" 
on_open is used to open the connection to the socket and binance
on_close is used to close the connection to the socket and binance
 """
def on_open(ws) -> None:
    print("opened connection")


def on_close(ws) -> None:
    print("closed connection")

"""
This is for all practical purposes the main function. 
Executes purchase logic, and provides a summary.
"""
def on_message(ws, message) -> None:
    global closes, prev_trend, in_position, trend, cycle, timeframe, can_buy

    json_message = json.loads(message) #reads out information from socket
    candle = json_message["k"] #reads out information about the current candle
    is_candle_closed = candle["x"] #reads out a bool, whether the candle is closed or not
    close = candle["c"] #close price of current candelstick

    if is_candle_closed:
        cycle += 1 #increments cycle number
        closes.append(float(close)) #add current closing price to list
        npcloses = np.array(closes) #add current closing price to a numpy array

        """
        Summary
        None of these lines are necessary, so comment out as desired.
        The lines below give a clear summary of the previous candle.
        Can be nice to uncomment while testing the code.
        """
        # print("\n")
        # print("SUMMARY: ")
        # print(f"candle closed at {close}")
        # print(f'in position: {in_position}')
        # print(f'can buy: {can_buy}')
        # print(f'cycle nr.: {cycle}')
        # print(f'time from start: {cycle*timeframe}')
        # print("\n")
        """
        The line below is a more compact summary with more information. 
        When using this, fully comment out the summary lines above.
        """
        #print(json_message)

        """
        The code below sells if you are in a position in the moment a new candle opens.
        """
        if in_position:
            # order logic
            order_succeeded = order(SIDE_SELL, trade_quantity, trade_symbol) #executes market sell order
            """
            While testing the code, uncomment the first two lines below, and comment the last three lines below
            While running the code, uncomment the last three lines below, and comment the first two lines below
            """
            in_position = False
            can_buy = False 
            # if order_succeeded:
            #     in_position = False
            #     can_buy = False

        ema2 = talib.EMA(npcloses, 2) #calculates exponential moving average with weight 2
        sma5 = talib.SMA(npcloses, 5) #calculates simple moving average with weight 5

        if cycle > minimal_data_basis:
            if (ema2[-1] >= sma5[-1]) and (sma5[-2] >= ema2[-2]): #if this condition is true, we will allow the code to take a long position
                can_buy = True
        
        """ The code below goes long if the condition above is met"""
        if cycle > minimal_data_basis:
            del closes[0] #this line is implemented to make the code run faster in the long run, by reducing the array sizes.
            if can_buy:
                # order logic
                order_succeeded = order(SIDE_BUY, trade_quantity, trade_symbol) #executes market buy order
                """
                While testing the code, uncomment the first line below, and comment the last two lines below
                While running the code, uncomment the last two lines below, and comment the first line below
                """
                in_position = True
                # if order_succeeded: 
                #     in_position = True


"""
run code
the code runs 'forever' - as long as it is not terminated manually
"""
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()