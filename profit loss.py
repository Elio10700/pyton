#profit or loss

cp = float(input("Enter the cost price of the product: "))
sp = float(input("Enter the selling price of the product: "))

if sp > cp:
    print (f"the profit we got is${sp-cp}")
else:
    print (f"the loss we got is${cp-sp}")