# PatchAlerts
[![Tests](https://github.com/shadowmoose/PatchAlerts/workflows/Test/badge.svg)](https://github.com/shadowmoose/PatchAlerts/actions)
[![Coverage Status](https://coveralls.io/repos/github/shadowmoose/PatchAlerts/badge.svg?branch=master)](https://coveralls.io/github/shadowmoose/PatchAlerts?branch=master)
[![Docker Build Status](https://img.shields.io/docker/build/shadowmoose/patchalerts.svg)](https://hub.docker.com/r/shadowmoose/patchalerts/)


**Tired of hopping into a game, only to find that you've missed the latest nerf? Want to make sure you and your friends are updated on the meta, or know when that server restart is coming?**

This simple tool aims to do all that. When run, it will generate a single configuration file, which you can use to toggle off/on any of the supported games. 

It will then scan the patch notes for those games. If it finds a new update, it will link it in your selected Discord channel using whatever [webhook](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks) you provide in the configuration.


-----------------
## Supported Games:

PatchAlerts supports quite a few popular games! Here's a full list:

|  | Supported Games | | |
| ----- | ------------- |----- | ------------- |
| [![Battlerite](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/Battlerite.png)](https://www.battlerite.com/) | [Battlerite](https://www.battlerite.com/) |[![CS:GO](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/CSGO.png)](http://blog.counter-strike.net/) | [CS:GO](http://blog.counter-strike.net/) |
| [![DOTA 2](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/DOTA2.png)](http://www.dota2.com) | [DOTA 2](http://www.dota2.com) |[![Dead By Daylight](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/DeadByDaylight.png)](http://deadbydaylight.com) | [Dead By Daylight](http://deadbydaylight.com) |
| [![Diablo 3](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/Diablo3.png)](https://us.diablo3.com/en/) | [Diablo 3](https://us.diablo3.com/en/) |[![Factorio](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/Factorio.png)](https://factorio.com) | [Factorio](https://factorio.com) |
| [![Fortnite](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/Fortnite.png)](https://www.epicgames.com/fortnite/) | [Fortnite](https://www.epicgames.com/fortnite/) |[![Grand Theft Auto 5](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/GrandTheftAuto5.png)](https://www.rockstargames.com/V/) | [Grand Theft Auto 5](https://www.rockstargames.com/V/) |
| [![Hearthstone](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/Hearthstone.png)](https://playhearthstone.com/) | [Hearthstone](https://playhearthstone.com/) |[![Heroes of the Storm](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/HeroesoftheStorm.png)](https://heroesofthestorm.com) | [Heroes of the Storm](https://heroesofthestorm.com) |
| [![Hunt: Showdown](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/HuntShowdown.png)](https://www.huntshowdown.com/) | [Hunt: Showdown](https://www.huntshowdown.com/) |[![League of Legends](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/LeagueofLegends.png)](https://leagueoflegends.com/) | [League of Legends](https://leagueoflegends.com/) |
| [![Overwatch](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/Overwatch.png)](https://playoverwatch.com/) | [Overwatch](https://playoverwatch.com/) |[![PUBG](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/PUBG.png)](https://playbattlegrounds.com/) | [PUBG](https://playbattlegrounds.com/) |
| [![Path of Exile](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/PathofExile.png)](https://pathofexile.com) | [Path of Exile](https://pathofexile.com) |[![Rainbow Six Siege](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/RainbowSixSiege.png)](https://rainbow6.ubisoft.com/siege/en-us/) | [Rainbow Six Siege](https://rainbow6.ubisoft.com/siege/en-us/) |
| [![Red Dead Redemption 2](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/RedDeadRedemption2.png)](https://www.rockstargames.com/reddeadredemption2/) | [Red Dead Redemption 2](https://www.rockstargames.com/reddeadredemption2/) |[![Rocket League](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/RocketLeague.png)](https://www.rocketleague.com) | [Rocket League](https://www.rocketleague.com) |
| [![Runescape](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/Runescape.png)](https://runescape.com/) | [Runescape](https://runescape.com/) |[![Sea Of Thieves](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/SeaOfThieves.png)](https://www.seaofthieves.com) | [Sea Of Thieves](https://www.seaofthieves.com) |
| [![Valorant](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/Valorant.png)](https://playvalorant.com) | [Valorant](https://playvalorant.com) |[![Warframe](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/Warframe.png)](https://www.warframe.com/) | [Warframe](https://www.warframe.com/) |
| [![World of Tanks](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/WorldofTanks.png)](https://worldoftanks.com) | [World of Tanks](https://worldoftanks.com) |[![World of Warcraft](https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/WorldofWarcraft.png)](https://worldofwarcraft.com/) | [World of Warcraft](https://worldofwarcraft.com/) |


*Depending on my free time and interest, I may expand the list of supported games or alert methods. If you have one you'd like added, please open a request.*
*This project is not in any way affiliated with or supported by these games, or their owners.*

-----------------

## Docker:

[PatchAlerts has a Docker build!](https://hub.docker.com/r/shadowmoose/patchalerts/)

If you have Docker installed, it's the simplest way to get started using PatchAlerts.

To download & launch PatchAlerts in Docker, which will scan for new patch notes on a CRON schedule provided, it's as simple as:

```sudo docker run -d --name PatchAlerts -v /build:/build shadowmoose/patchalerts -s '*/30 * * * *'```

Simply edit the ```config.yml``` file it generates in the data directory. No restart is necessary.

See [below](#setup) for more configuration information.

## Non-Docker Requirements:

If you're running PatchAlerts locally without Docker, you'll need Python installed.

It runs in [Python 3](https://www.python.org/downloads/), and has no UI. 

## Setup:

PatchAlerts is perfect for throwing onto your own server somewhere, scheduled to run as often as you like. 

The only alert method currently supported is via Discord Webhook, which is a simple way to grant posting access without adding a whole user to your server. You'll need to create a hook in your [Discord Channel Settings](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks). You simply need to edit the URL created by the webhook into the configuration file (```build/config.yml```), like so:
```
alerts: 
    Discord: 
        webhook: [paste link here]
```

While you're in there, make sure to set ```enabled: True``` for whatever Alerts and Games you want active.
