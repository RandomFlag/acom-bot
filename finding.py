import requests
def findCom (ComicSR):
    baseUrl = 'https://acomics.ru/~'   
    f_raw = requests.get('https://acomics.ru/search?keyword=' + ComicSR)
    f = f_raw.text
    fb = 1
    urls = []
    names = []
    for i in range(1, 10):
        for c in range (1,4):
            ind = f.find(baseUrl, fb)
            inde = (f.find ("</a>", ind))
            if c == 2:
                f_temp = f[ind : inde]
                u_inde = f_temp.find('\"')
                url_temp = f_temp[0 : u_inde]
                if len(url_temp) > 0 :
                    urls.append (url_temp)
                    n_ind = f_temp.find(">") + 1
                    name_temp = f_temp[n_ind : len(f_temp)]
                    names.append (name_temp)
            fb = inde 
    return urls, names

