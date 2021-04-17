def computer_grade(score):
<<<<<<< HEAD
   print("The score entered must be an integer or a float")
   score = (float(input("Enter your score :")))
   if score<0:
      return("BAD SCORE")
   elif score>1:
      return ("BAD SCORE")
   elif score >=0.9:
      return ("A")
   elif score >=0.8:
      return ("B")
   elif score>=0.7:
      return ("C")
   elif score>=0.6:
      return ("D")
   elif score<0.6:
      return ("F")
   else:
      return ("BAD SCORE")
result = computer_grade("score")
print(result)
=======
   try:
    score = (float(input("Enter your score :")))
    if score<0:
      print("BAD SCORE")
    elif score>1:
      print("BAD SCORE")
    elif score >=0.9:
      print("A")
    elif score >=0.8:
      print("B")
    elif score>=0.7:
      print("C")
    elif score>=0.6:
      print("D")
    elif score<0.6:
      print("F")
    else:
      print("BAD SCORE")
   except:
    print("Bad score")
computer_grade("score")
>>>>>>> 4baa02f (charpter 4 exrcises are done)
