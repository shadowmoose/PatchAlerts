from util import loader
from wrappers.update import Update
from games.base_class import Game


class Valorant(Game):
    def __init__(self):
        super().__init__("Valorant", homepage="https://playvalorant.com")



    def scan(self):
        _title = ""
        _url = ""
        _desc = ""
        _imgurl = ""
        data = loader.soup("https://playvalorant.com/en-us/news/")
        items = data.find_all("div", {"class": "NewsArchive-module--newsCardWrapper--2OQiG"})
        for item in items:
            _title = item.findChildren("h5")[0].contents[0]
            if "Patch Notes" not in _title:
                continue
            _url = "https://playvalorant.com" + item.findChild("a")["href"]
            _desc = item.findChildren("p", {"class": "copy-02 NewsCard-module--description--3sFiD"})[0].contents[0]
            _imgurl = self.get_patchnote_highlight_picture(_url)
            break
        yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, image=_imgurl, color="#FF4654")   
       

    def get_patchnote_highlight_picture(self, _url):
        data = loader.soup(_url)
        main_div = data.find("div", {"class": "copy-02 NewsArticleContent-module--articleTextContent--2yATc"})
        imgurl = main_div.findChildren("img")[0]["src"]  
        return imgurl
