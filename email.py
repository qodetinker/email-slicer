# Read items from a list. Accounting for all data types if possible
x = ['goku@dbz.com', 2, 3.14, 'vegeta@super.com', 'pquach', True]

def slice(alist):
  user_name = []
  domain_name = []  
  for x in alist:
    try:
      if '@' in x:
        email_slicer = x.split('@')
        #print(email_slicer)
        user_name.append(email_slicer[0])
        domain_name.append(email_slicer[1])
    except TypeError:
      continue
  return 'Usernames: {0} \nDomains: {1}'.format(user_name, domain_name)

print(slice(x))
