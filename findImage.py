import requests

def findIMG (ComicURL, Page):
    baseUrl = "/upload/!c/"
    f_raw = requests.post(ComicURL  + str(Page), data = {'ageRestrict':'18'})  
    f = f_raw.text
    ind_b = (f.find (baseUrl))
    ind_e = (f.find (".", ind_b))
    final_url = f[ind_b: ind_e + 4]
    return ("https://acomics.ru" + final_url)

def lastPage(ComicURL):
    f_raw = requests.post(ComicURL, data = {'ageRestrict':'18'})  
    f = f_raw.text
    ind_b = (f.find ('<span class="issueNumber">'))
    ind_b = (f.find ('/', ind_b))
    ind_e = (f.find ('<', ind_b))
    final_url = f[ind_b + 1: ind_e]
    return (final_url)
