name = ' SAS2py '

print('===>find ', name.find('p', 0, 5))
print('===>index ', name.index('2'))
print('py' in name)
print('===>capitalize ',name.capitalize())
print('===>count ',name.count('p'))
print('===>len ',len(name))
print('===>startswith ',name.startswith('S'))
print('===>endswith ',name.endswith('y'))
print('===>isalpha ',name.isalpha())
print('===>isalnum ',name.isalnum())
print('===>isnumeric ',name.isnumeric())
print('===>isspace ', name.isspace())
print('===>split ', name.split('2'))
print('===>strip ', name.strip())
print('===>lstrip ', name.lstrip())
print('===>rstrip ', name.rstrip())
print('===>replace', name.replace('2', '4'))
print('===>ord', ord('S'))
print('===>chr', chr(83))



###String Formatting 
user_name = 'Bindhu'
print(f'Hello {user_name}')
print('Hello {}'.format(user_name))
print('Hello ' + user_name)


