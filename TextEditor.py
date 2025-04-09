from colorama import Fore,Style,init
init()
def main_func():
     print("1.open file")
     print("2.Write/replace the text")
     print("3.save file")
     print("4.close")

def open_file(filename):
     try:
          with open(filename,'r') as file:
               readfile=file.read()
               print(Fore.LIGHTYELLOW_EX)
               print('\t'+readfile+Style.RESET_ALL+'\n')
               return readfile
     except FileNotFoundError:
          print("File not found")
          return ""
def save_file(filename, readfile):
     with open(filename, 'w') as file:
          file.write(readfile)
          print(Fore.GREEN+"\n\tfile saved successfully\n"+Style.RESET_ALL) 
          
filename=input(Fore.LIGHTRED_EX+"Enter filename: "+Style.RESET_ALL)
filecontent=""
while True:
    main_func()
    choice=input("Enter a choice (1-4): ")
    if choice == '1':
         filecontent=open_file(filename)
    elif choice == '2':
          print("Write/Replace the text")
          filecontent=input(Fore.LIGHTGREEN_EX+ "\tEnter the text: "+ Style.RESET_ALL)
    elif choice == '3':
         save_file(filename,filecontent)
    elif choice == '4':
         print("close the file")
         break
    else:
         print("Invalid choice, please select from 1-4")
        
     