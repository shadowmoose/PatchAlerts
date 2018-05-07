from games.battlerite import Battlerite
from games.leagueoflegends import LeagueOfLegends
from games.huntshowdown import HuntShowdown
from games.pathofexile import PathOfExile
from games.warframe import Warframe
from games.pubg import PUBG
from games.fortnite import Fortnite
from games.hearthstone import Hearthstone
from games.csgo import CSGO
from games.overwatch import Overwatch
from games.dota2 import DOTA2
from games.diablo import Diablo3
from games.deadbydaylight import DBD
from games.runescape import Runescape
from games.rainbowsix import RainbowSix
from games.worldoftanks import WorldOfTanks
from games.heroesofthestorm import HOTS

_all_games = [
	Battlerite(), LeagueOfLegends(), HuntShowdown(), PathOfExile(), Warframe(), PUBG(), Fortnite(),
	Hearthstone(), CSGO(), Overwatch(), DOTA2(), Diablo3(), DBD(), Runescape(), RainbowSix(), WorldOfTanks(),
	HOTS()
]


def all_games():
	return sorted(_all_games, key=lambda x: x.name, reverse=False)
