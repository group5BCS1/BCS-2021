def computer_grade(score):
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