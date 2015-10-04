number_of_pages = 12
list_of_pages = []
list = []
if number_of_pages%4 == 0:
	middle_page = number_of_pages/2
else:
	print "need " + str(number_of_pages%4) + "more pages"


for n in range(middle_page+1, number_of_pages+1):
	list_of_pages.insert(0, n)
	
location = 0
n = 0
while n < middle_page:
	n = n+1
	location=location+1
	list_of_pages.insert(location, n)
	n = n+1
	list_of_pages.insert(location+1, n)
	location = location+3
print list_of_pages

20,1,2,19,18,3,4,17,16,5,6,15,14,7,8,13,12,9,10,11