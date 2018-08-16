def tiptip(price):
    if price > 100:
        tip = round(price/20, 2)
    else:
        tip = round(price/10, 2)
    return tip

foods= ['Radish Soup(RS)', 'Truffel Pie(TP)', 'Pesto Pasta(PP)', 'African Samosas(AS)', 'Pita Bread(PB)']
prices= [80,120,75,150,20]
titles= ['foods','prices']
data= [titles] + list(zip(foods, prices))
shortfood=['RS','TP','PP','AS','PB']

print("RESTUARANT MENU:")
for i, d in enumerate(data):
    line = '|'.join(str(x).rjust(20) for x in d)
    print(line)
    if i ==0:
        print('-' * len(line))

order=input("Please place your order using one of the shorthands above, for example RS for Radish Soup: ")
def valuecheck(fooditem, shortf, price):
    for i in range(len(shortf)):
        if fooditem == shortf[i]:
            return price[i]

cost = valuecheck(order,shortfood,prices)
tip=tiptip(cost)

print("Your order will be {} SEK and we recommend you to tip {} SEK".format(cost,tip))
total=round(cost+tip,2)
print("This brings your total to {} SEK".format(total))