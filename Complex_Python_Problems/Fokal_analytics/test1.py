def Buysell(list_dates, list_stock_prices):
    print("Buy on "+str(list_dates[0])+" for "+str(list_stock_prices[0]))
    j=0
    lis=[]
    for i in range(len(list_stock_prices)):
        if list_stock_prices[j]>list_stock_prices[i]:
            z=i
            prof=list_stock_prices.index(max(list_stock_prices[j:i]))
            print("sell on "+str(list_dates[prof])+" for "+str(list_stock_prices[prof]))
            print("Buy on "+str(list_dates[z])+" for "+str(list_stock_prices[z]))
            prof=list_stock_prices.index(max(list_stock_prices[z:len(list_stock_prices)]))
            break
    else:
        z=list_stock_prices.index(max(list_stock_prices))
        print("sell on "+str(list_dates[z])+" for "+str(list_stock_prices[z]))
        print("Buy on "+str(list_dates[z+1])+" for "+str(list_stock_prices[z+1]))
        prof=list_stock_prices.index(max(list_stock_prices[z+1:len(list_stock_prices)]))
    print("sell on "+str(list_dates[prof])+" for "+str(list_stock_prices[prof]))
    return

Buysell(["2017-01-01", "2017-01-02","2017-01-03","2017-01-04","2017-01-05", "2017-01-06","2017-01-07","2017-01-08"], [25,28,26,37,29,10,100,200])
Buysell(["2017-01-01", "2017-01-02","2017-01-03","2017-01-04","2017-01-05", "2017-01-06"], [50,20,30,70,100,40])


        



