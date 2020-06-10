from util import loader
from wrappers.update import Update
from games.base_class import Game
from bs4 import element


class Factorio(Game):
    def __init__(self):
        super().__init__("Factorio", homepage="https://factorio.com")



    def scan(self):
        _title = ""
        _url = ""
        _desc = ""
        data = loader.soup("http://forums.factorio.com/viewforum.php?f=3")
        items = data.find_all("li", {"class": "announce"})
        for item in items:
            _title = item.findChildren("a")[0].contents[0]
            if "Version" not in _title:
                continue
            _url = "https://forums.factorio.com" + item.findChild("a", {"class":"topictitle"})["href"][1:]
            _desc = self.get_description(_url)
            break
        yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color="#C97327")   
       

    def get_description(self, _url):
        data = loader.soup(_url)
        contents = data.find("div", {"class": "content"}).contents
        _desc = ""
        for item in contents:
            if type(item) is element.NavigableString:
                continue
            if item.text is None:
                continue
            if item.name is None:
                continue

            if item.name is "strong": 
                _desc = _desc + "**" + item.text + "** \n"
            else:
                _desc = _desc + item.text + "\n"
            
        return _desc
