import requests
debut_url = input ("quel est le debut de l'url a telecharger ?  ")
fin_url = input ("quel est la fin de l'url ?  ")
nombre_page = input ("combien de pages ?  ")
extention = input ("quel est l'extention ?  ")
page = 0
headers = {
    "User-Agent": "Chrome/51.0.2704.103",
}
merger = PdfFileMerger()
pdfs = ['page 10.pdf']


def download_pdf(url_, nom_, headers):
    # Send GET request
    response = requests.get(url_, headers=headers)
    # Save the PDF
    if response.status_code == 200:
        with open(nom_, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)
        print(url_)

for i in range(int(nombre_page)) :
    page += 1
    url =  debut_url + str(page) + fin_url
    nom = "page " + str(page) + extention
    download_pdf(url, nom, headers)
    pdfs.append(nom)

