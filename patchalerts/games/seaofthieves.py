from util import loader
from wrappers.update import Update
from games.base_class import Game


class SeaOfThieves(Game):
    def __init__(self):
        super().__init__("Sea Of Thieves", homepage="https://www.seaofthieves.com")

    def scan(self):
        data = loader.soup("https://www.seaofthieves.com/de/release-notes/")
        header = data.find("div", {"class": "page-header"})
        _title = header.findChildren("p")[0].contents[0]
        _url = "https://www.seaofthieves.com/de/release-notes/" + _title
        updates = data.find("span", text="Updates").findParent("h2").findParent(
            "div").findNext("div").findChild("div").findChild("ul").find_all("li")
        _desc = self.create_description_from_updates(updates)
        yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color="#419178")

    def create_description_from_updates(self, updates):
        description = ""
        for update in updates:
            text = update.contents[0] + \
                update.contents[1].text + update.contents[2]
            description += text

        return description
