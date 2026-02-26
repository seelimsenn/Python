website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

length = len(website)

result1 = len(course)
print(result1)

result2 = website[7:10]
print(result2)

result3 = website[22:25]
print(result3)
result3 = website[length-3:length]
print(result3)

result4 = course[0:15]
result4 = course[:15]
print(result4)
result4 = course[-15:]
print(result4)

result5 = course[::-1]
print(result5)

# s = '12345' * 5
# print(s[::5])

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"
result6 = "Benim adım " + name + " " + surname + ", yaşım " + str(age) + " ve mesleğim " + job
print(result6)
result6 = "Benim adım {} {} , yaşım {} ve mesleğim {}".format(name, surname, age, job)
print(result6)
result6 = f"Benim adım {name} {surname} , yaşım {age} ve mesleğim {job}"
print(result6)

s = "Hello world"
s = s[0:6] + "W" + s[7:]
print(s)

result8 = "abc" * 3
print(result8)