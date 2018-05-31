# from_one_to_seven  = ('1111111')
# print (from_one_to_seven[6:7])
# print (from_one_to_seven[5:7])
# print (from_one_to_seven[4:7])
# print (from_one_to_seven[3:7])
# print (from_one_to_seven[2:7])
# print (from_one_to_seven[1:7])
# print (from_one_to_seven)

# mylist = {
# 0 : '******\n*    *\n*    *\n*    *\n*    *\n*    *\n******',
# 1 : '    * \n  * * \n *  * \n    * \n    * \n    * \n******',
# 2 : '  *** \n *   * \n    *  \n   *   \n  *    \n *****',
# 3 : '******\n     *\n   ***\n   ***\n     *\n******',
# 4 : '*    *\n*    *\n*    *\n******\n     *\n     *',
# 5 : '***** \n*     \n**   \n****  \n    * \n**** ',
# 6 : ' **** \n*     \n*     \n***** \n*    *\n **** \n',
# 7 : ' **** \n*    *\n    * \n   *  \n   *  \n   *  \n',
# 8 : ' **** \n*    *\n* ** *\n* ****\n*    *\n **** \n',
# 9 : '  *** \n *   *\n *   *\n  ****\n     *\n     *\n'
# }


# w =  int(input("What is number?"))

# if w < 10:
# 	print(mylist.get(w))
# elif w >= 10:
# 	wstr = str(w)
# 	for x in wstr:
# 		x = int(x)
# 		print(mylist.get(x))
# 		print ('------')


# i = ''
# for x in range(7):
#     i = i + '1'
#     print(i)

# count_str = 20
# for i in range(1, 21):
# 	if not i % 2:
# 		print(('{}'.format(i)) * 10)
# 	else:
# 		print('1' * 10)


hour = int(input('Введи часы: '))
minute = int(input('Введи минуты: '))

if hour >= 12:
	hour -= 12
	print(hour)
hours_strelka = (hour * 60 + minute) * 0.5
print(hours_strelka)
minute_strelka = minute * 6
print(minute_strelka)
ost_ugol = minute_strelka - hours_strelka

print(ost_ugol)