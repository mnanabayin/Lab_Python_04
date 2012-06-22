#1
groceries = ['banana','strawberries','apples','bread']
print 'Initial groceries : ',groceries,'\n'
ans = raw_input('What do you want to add to the groceries? eg champagne: ')
groceries.append(ans)
print 'Altered groceries : \n',groceries

print '\n'
print "Messi decides he doesn't need bread : "
groceries.remove('bread')
print "Messi's groceries : \n",groceries
print '\n'
groceries.sort()
print 'Alphabetically sorted groceries : \n',groceries

print '\n\n'
#2
#a
store_data = {'Apples':'SPIC_APPLES','Bananas':'SPIC_BANANAS',
              'Bread':'SPIC_BREAD','Carrots':'SPIC_CARROTS',
              'Champagne':'SPIC_CHAMPAGNE','Strawberries':'SPIC_STRAWBERRIES'}
print store_data

item = raw_input('Choose the item you want to change price : ')
price = input('Enter price : ')
store_data[item] = price

print store_data

print '\nAdded chicken\n'

store_data['Chicken'] = 'SPIC_CHICKEN'

print store_data


#3
print '\n\n SOME LIST TO THE CEO'
always_in_stock = store_data.keys()
print tuple(always_in_stock)



print '\FIRST TUPLE FROM COMPANY TO CEO'
first_list = ('Gari','Tomato','Okro','Cassava')
print first_list,"\n"
print '\SECOND TUPLE FROM COMPANY TO CEO'
second_list = tuple(always_in_stock)
print second_list,"\n"
print '\FINAL TUPLE TO CEO'
final_list = first_list + second_list[:]

print final_list



#4
print '\n\n'
