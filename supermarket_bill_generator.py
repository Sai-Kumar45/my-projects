from datetime import datetime

name=input("Enyer your name: ")


items_list="""
Rice----Rs 50/kg
Oil-----Rs 80/kg
Sugar---Rs 20/kg
Salt----Rs 10/kg
pasta---Rs 150/kg
Dal-----Rs 110/kg
Badam---Rs 350/kg
Bru-----Rs 150/kg
"""

price=0
pricelist=[]
totalprice=0
finalprice=0
itemlist=[]
qtylist=[]
plist=[]


items={'rice':50,'oil':80,'sugar':20,'salt':20,'pasta':150,'dal':110,'badam':350,'bru':150}

    
option=int(input("To display items Select option 1: "))
if option == 1:
    print(items_list)

for i in range(len(items_list)):
    inp1=int(input("If you want to purchase press 1 or 2 for exit: "))
    if inp1==2:
          break
    if inp1==1:
        item=input("Enter your items: ")
        quantity=int(input("Enter your quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            itemlist.append(item)
            qtylist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst + totalprice 
                

        else:
            print("The entered item is out of stock")

    else:
        print("you entered the wrong option")

    inp=input("can i bill the items yes or no: ")
    if inp=='yes':
        pass
        if finalamount!=0:
            for i in range(len(pricelist)):
                print(i+1,itemlist[i],qtylist[i],plist[i])
            print("Total Price",'RS',totalprice)
            print("GST ",'RS',gst)
            print("Total Amount",'RS',finalamount)
