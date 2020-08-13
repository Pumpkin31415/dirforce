import requests

#create a variable to store the url
url = input('Enter the url in https://example.com format : ')
#have the user specify the location of the file
fileLocation = input('Enter the location of the directories list : ')
#output what we are doing
print('Scanning ' + url)
r = requests.get(url)
#check to make sure the url is valid
if r.status_code <= 399 or r.status_code >=500:
    
   #make a for loop to check all directories in the file
    with open (fileLocation , 'rt') as directoryFile:
        for eachLine in directoryFile:
            r = requests.get(url + '/' + eachLine)
            if r.status_code <=399 or r.status_code >=500:
                print('/' + eachLine + ' returned code: ' + str(r.status_code))
            p
else: 
        print('ERROR: URL MAY NOT BE VALID. URL STATUS CODE: ' + str(r.status_code)): ' + str(r.status_code))
