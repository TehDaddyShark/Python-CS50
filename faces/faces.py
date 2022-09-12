#first try worked but didn't meet the problem set critera
#def main():

    #convert = input(" ")

    #print(convert.replace(':)','🙂').replace(':(','😐'))

def main():
    #Grab input
    q = input("Happy? or Sad? ")
    #convert emoji 
    print(convert(q))#should print emoji's when main is called

def convert(_): #I'm using (_) incase I need to pass another varible other then "q" if the future
    #should take input change the emoji's then return the output 
    
    _ = _.replace(':)','🙂').replace(':(','😐')
    
    return _ #should return emoji's after being ran 

main()