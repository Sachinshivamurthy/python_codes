def IsValid(Inputstr):
  count=0
  for i in range(len(Inputstr)):
      if Inputstr[i] == "(":
          count+=1
      elif Inputstr[i] == ")":
          count-=1
      else:
          continue
  if count==0:
      return True
  return False
print(IsValid("(yes(|no(to(where),yes(here, there, yay))(blank is there always))
              ,there is some chance"))
