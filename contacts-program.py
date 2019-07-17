conct=dict()
def add(conct):
  name=input("enter the name to add:")
  num=int(input("enter the number"))
  conct[name]=num
def delete(conct):
  name=input("enter the contact name to delete:")
  del conct[name]
def display(conct):
  print(conct)
def search(conct):
  name=input("enter the name:")
  if name in conct:
    print(conct[name])
  else:
    print("contact not there")
def update(conct):
  name=input("enter the name to update:")
  if name in conct:
    num=int(input("enter the number to update"))
    conct.update({name:num})
  else:
    print("name not found")
print("telephone directory")
while(1):
  print('''choose
          1.add new contact
          2.display
          3.search
          4.delete
          5.update''')
  n=int(input())
  if(n==1):
    add(conct)
  elif(n==2):
    display(conct)
  elif(n==3):
    search(conct)
  elif(n==4):
    delete(conct)
  elif(n==5):
    update(conct)
  elif(n==6):
    exit()
