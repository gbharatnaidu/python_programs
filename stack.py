stack=[]
def push(stack):
  val=input("enter the value to push into the stack")
  stack.append(val)
def pop(stack):
  if len(stack):
    stack.pop()
  else:
    print("stack is empty cant remove the element")
def peek(stack):
  print("the last elemennt is",stack[len(stack)-1])
def display(stack):
  if len(stack):
    print("the elements are",end=" ")
    for i in range(len(stack)):
      print(stack[i],end=" ")
  else:
    print("stack is empty no elements to display")
while(1):
  n=int(input('''1.push
                 2.pop
                 3.peek
                 4.display
                 5.exit'''))
  if(n==1):
    push(stack)
    display(stack)
  elif(n==2):
    pop(stack)
    display(stack)
  elif(n==3):
    peek(stack)
  elif(n==4):
    display(stack)
  elif(n==5):
    exit()
