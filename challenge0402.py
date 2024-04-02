def getYear():
   num = 0 #initialize num
   while num <= 2000 or num >= 2021:
      num = int(input("ask for number between 2000 and 2021:"))
   return num #outside loop

def main():
   #num in the main function is independent of num in getYear
   num = getYear()
   print ("The year is", num)

if __name__ == "__main__":
   main()