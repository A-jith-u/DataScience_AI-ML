
user=0
start=False
while user!="quit":
    user=input(">")
    
 
    if user=="start":
      if start==False:
       print("car started... Ready to go!")
       start=True
      elif start==True:
         print("The car is already started")
    elif user=="stop":
      if start==True:
       print("Car stopped")
       start=False
      elif start==False:
        print("The car is already stopped")
    elif user=='quit':
       break
    elif user=="help":
       print('''start - to start the car
stop - to stop the car
quit - to exit ''')
    else:
      print("I don't understand that...")
    