def test_recipe(food_1, food_2):
    foodcombo=("{} with {}".format(food_1,food_2))
    return foodcombo


food1=input("Please input a food ")
food2=input("please input a side ")
dishname=test_recipe(food1,food2)
print("Today the restuarant is serving {}.".format(dishname))