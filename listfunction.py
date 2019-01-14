#working with list functions which allows us to modify

lucky_numbers =[42,8,15,16,23,2]
friends = ["laila","kaham","Jimmy","Shiro"]

#friends.extend(lucky_numbers)
friends.append("Suki")

print(friends)

friends.insert(1,"Selima")
print(friends)

friends.remove("kaham")
print(friends)

print(friends.index("Selima"))

friends.append("Selima")
print(friends)
print(friends.count("Selima"))
print("\n\n")
print(friends.sort())
lucky_numbers.sort()
print(lucky_numbers.sort())
print(lucky_numbers.reverse())

friends2 = friends.copy()
print(friends2)