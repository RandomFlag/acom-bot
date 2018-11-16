import requests

def findIMG (ComicURL, Page):
    baseUrl = "/upload/!c/"
    f_raw = requests.post(ComicURL  + str(Page), data = {'ageRestrict':'18'})  
    f = f_raw.text
    ind_b = (f.find (baseUrl))
    ind_e = (f.find (".", ind_b))
    final_url = f[ind_b: ind_e + 4]
    return ("https://acomics.ru" + final_url)
