import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request

fd = open("animelist.csv", "w", encoding="utf-8")
fd.write("main_title, official_title1, official_title2, type, start_date, end_date, tags, rating, average, review_rating\n")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
for o in range(1, 51):
    print(o)
    reg_url = "https://anidb.net/perl-bin/animedb.pl?show=anime&aid=" + str(o)
    req = Request(url=reg_url, headers=headers) 
    html = urlopen(req).read()
    page_soup=soup(html,"html.parser")

    table = page_soup.find("div", {"id": "tab_1_pane"} ).div.table.tbody
    trs = table.findAll("tr")

    try:
        main_title = trs[0].td.span.text.strip().replace(",", " ")
    except:
        main_title = "No title"

    try:
        official_title1 = trs[1].td.label.text.strip().replace(",", " ")
    except:
        official_title1 = "No title"

    try:
        official_title2 = trs[2].td.label.text.strip().replace(",", " ")
    except:
        official_title2 = "No title"
    
    try:
        type_ = trs[3].td.text.strip().replace(",", " ")
    except:
        type_ = "No type"
    
    try:
        start_date = trs[4].td.find("span", {"itemprop": "startDate"}).text.strip().replace(",", " ")
    except:
        start_date = "-1"

    try:
        end_date = trs[4].td.find("span", {"itemprop": "endDate"}).text.strip().replace(",", " ")
    except:
        end_date = "-2"

    try:
        tags = []
        taglist = trs[5].findAll("span", {"class":"tagname"})
        for t in taglist:
            tags.append(t.text)
        tags = ' | '.join(tags).strip().replace(",", " ")
    except:
        tags = "No tags"

    try:
        rating = trs[7].td.text.strip().replace(",", " ")
    except:
        rating = "-1"

    try:
        avg = trs[8].td.text.strip().replace(",", " ")
    except:
        avg = "-1"

    try:
        review_rating = trs[9].td.text.strip().replace(",", " ")
    except:
        review_rating = "-1"

    fd.write(main_title + "," + official_title1 + "," + official_title2 + "," + type_ + "," + start_date + "," + end_date + "," + tags + "," + rating + "," + avg + "," + review_rating + "\n")