#1
market = ["yam", "tomato","onion"]
market.append("fish")
print(market)


#2
grades =[80 , 90 ,70]
grades.insert(1, 85)
print(grades)



#3
gadgets = [ "laptop","phone", "tablet","phone"]
gadgets.remove("phone")
print(gadgets)

#4
colors = ["red","blue","green"]
colors.clear()
print(colors)


#5
votes = ["yes","no","yes","yes","no"]
print(votes.count("yes"))   
print(votes)


#6
alphabets = ["a","b","c","d","e", "f"]
sliced = alphabets[2:5]
print(alphabets)


#7
students = ["kofi","Ama","yaw"]
students.reverse()
print(students)


#8
list_a = [1, 2]
list_b = [3, 4]
list_a.extend(list_b)
print(list_a)


#9
cities = ["Accra","Kumasi","Tamale"]
removed_city = cities.pop(2)
print(removed_city)
print(cities)


#10
items = ["pen","ruler","eraser"]
index = items.index("ruler")
print(index)


# SECTION 2
#1
student_info = ("Araba",20)
print(student_info)
print(type(student_info))


#2
tup = (1, 2, 3)
tup_list = list(tup)
tup_list.append(4)
tup = tuple(tup_list)
print(tup)

#3
given_data = (10, 20, 30, 40, 10)
print(given_data.count(10))

#4
tuple_colors = ("red", "blue", "green")
print(tuple_colors[1])


#5
tuple_coords = (5.6, -0.1)
lat, lon = tuple_coords
print("Latitude:", lat)
print("Longitude:", lon)

#6
nest = [(5,10)]
print(len(nest))

#7
Given_number = (10, 20, 30, 40, 50)
print(Given_number[-2:])

#8
my_list = [1, 2, ]
my_list_b = [3, 4]
my_list.extend(my_list_b)
print(my_list)

#9
my_tup = (1, 2, 3)
del my_tup()

#10
variable_x = (5)
variable_y = (5,)
print(type(variable_x))
print(type(variable_y))





