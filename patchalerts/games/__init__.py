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
from games.worldofwarcraft import WorldOfWarcraft
from games.gta import GTA5
from games.rocketleague import RocketLeague
from games.rdr2 import RDR2
from games.seaofthieves import SeaOfThieves
from games.valorant import Valorant
from games.factorio import Factorio


_all_games = [
	Battlerite(), LeagueOfLegends(), HuntShowdown(), PathOfExile(), Warframe(), PUBG(), Fortnite(),
	Hearthstone(), CSGO(), Overwatch(), DOTA2(), Diablo3(), DBD(), Runescape(), RainbowSix(), WorldOfTanks(),
	HOTS(), WorldOfWarcraft(), GTA5(), RocketLeague(), RDR2(), SeaOfThieves(), Valorant(), Factorio()
]


def all_games():
	return sorted(_all_games, key=lambda x: x.name, reverse=False)
