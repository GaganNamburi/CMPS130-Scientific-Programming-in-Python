def build_periodic_table(filename="periodic_table.txt"):
    input_file = open(filename, 'r')
    table = dict()
    for element in input_file:
        tokens = element.split()
        table[tokens[2]] = (tokens[1], int(tokens[0]), float(tokens[3]))
    return table

def search_by_symbol_name(dictionary,searchString):
    result = []
    for x in  dictionary:
        if x.find(searchString)!= -1:
           result.append(dictionary[x])
        elif dictionary[x][0].find(searchString)!= -1:  
           result.append(dictionary[x])
    return result

def search_by_atomic_mass(dictionary, min, max):
  result = []
  for x in dictionary:
    if dictionary[x] >= min and dictionary[x] <= max:
      result.append(dictionary[x])
  return result

#Initialize table
table = build_periodic_table()

choice = True
while choice:
    print("1) Search by symbol/name")
    print("2) Search by atomic mass")
    print("3) Molecular Mass Calculation")
    print("4) Quit")
    option=input("Please enter your choice: ")
    if option == "1":
      searchString=input("Enter the symbol/name to search: ")
      searchresult=[]
      searchresult=search_by_symbol_name(table,searchString)
      if not searchresult:
         print("Entered search symbol/name not found")
      else:
        print("Name     # Atomic mass")
        print("==================================")
        for i, j, k in searchresult:
          print(i, j, k)
        print("==================================")
    elif option == "2":
      low = float(input("Please enter minimum mass: "))
      high = float(input("Please enter maximum mass: "))
      massResult = search_by_atomic_mass(table, low, high)
    elif option == "3":
      print("\n enter molecular mass")
    elif option=="4":
      break
    else:
       print("\n Not Valid Choice")

