import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    turtle.bgcolor("black")
    t.color("yellow")
    tree(brlen,t)
    myWin.exitonclick()

brlen=int(input("Enter the length of the branch:"))
main()








    
  
            
    
