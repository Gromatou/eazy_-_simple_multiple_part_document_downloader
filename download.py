import requests
print = ("===============================================================================")
print = ("welcome to the multipart document downloader, the first program of Gromatou")
print = ("===============================================================================")
print = ("")

debut_url = input ("beginning of url : ")           #whe ask for alls values
fin_url = input ("end of url : ")
nombre_page = input ("number of pages : ")
extention = input ("file type : ")
page = 0                                            #whe begin with the first page
headers = {                                         #whe deffine the headers to send to the website about our user agent
    "User-Agent": "Chrome/51.0.2704.103",
}

def download_file(url_, nom_, headers):             #function to download the file
    response = requests.get(url_, headers=headers)  #whe ask the website for the file and get it
    if response.status_code == 200:                 #whe check if the answere is correct
        with open(nom_, "wb") as f:                 #whe make a file to write the file content in it
            f.write(response.content)               #whe write the file in it
    else:
        print(response.status_code)                 #whe print some debugs info if it fail
        print(url_)

for i in range(int(nombre_page)) :                  #the loop of download
    page += 1                                       #increase the page number
    url =  debut_url + str(page) + fin_url          #concatenate the url
    nom = "page " + str(page) + extention           #making the filename
    download_file(url, nom, headers)                #using our wonderfull download fucntion

