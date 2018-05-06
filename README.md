# PatchAlerts
[![Build Status](https://travis-ci.org/shadowmoose/PatchAlerts.svg?branch=master)](https://travis-ci.org/shadowmoose/PatchAlerts)[![Coverage Status](https://coveralls.io/repos/github/shadowmoose/PatchAlerts/badge.svg?branch=master)](https://coveralls.io/github/shadowmoose/PatchAlerts?branch=master)

**Tired of hopping into a game, only to find that you've missed the latest nerf? Want to make sure you and your friends are updated on the meta, or know when that server restart is coming?**

This simple tool aims to do all that. When run, it will generate a single configuration file, which you can use to toggle off/on any of the supported games. 

It will then scan the patch notes for those games. If it finds a new update, it will link it in your selected Discord channel using whatever [webhook](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks) you provide in the configuration.


-----------------
## Supported Games:

PatchAlerts supports most of the largest games out there! Here's a full list:

|  | Supported Games |
| ----- | ------------- |
| [<img src="https://i.imgur.com/dDIezWP.png" width="48">](https://www.battlerite.com/) | [Battlerite](https://www.battlerite.com/) |
| [<img src="https://i.imgur.com/wlhfzUT.png" width="48">](http://blog.counter-strike.net/) | [CS:GO](http://blog.counter-strike.net/) |
| [<img src="https://i.imgur.com/h1ExdFI.png" width="48">](http://www.dota2.com) | [DOTA 2](http://www.dota2.com) |
| [<img src="https://i.imgur.com/C9cNY2O.png" width="48">](https://us.diablo3.com/en/) | [Diablo 3](https://us.diablo3.com/en/) |
| [<img src="https://i.imgur.com/9Hz2BnX.png" width="48">](https://www.epicgames.com/fortnite/) | [Fortnite](https://www.epicgames.com/fortnite/) |
| [<img src="https://i.imgur.com/fpsVoeK.png" width="48">](https://playhearthstone.com/) | [Hearthstone](https://playhearthstone.com/) |
| [<img src="https://i.imgur.com/SnQ6cRD.png" width="48">](https://www.huntshowdown.com/) | [Hunt: Showdown](https://www.huntshowdown.com/) |
| [<img src="https://i.imgur.com/fyMlBLW.png" width="48">](https://leagueoflegends.com/) | [League of Legends](https://leagueoflegends.com/) |
| [<img src="https://i.imgur.com/Wp2Xlvw.png" width="48">](https://playoverwatch.com/) | [Overwatch](https://playoverwatch.com/) |
| [<img src="https://i.imgur.com/KmmoncG.png" width="48">](https://playbattlegrounds.com/) | [PUBG](https://playbattlegrounds.com/) |
| [<img src="https://i.imgur.com/4FYaeCh.png" width="48">](https://pathofexile.com) | [Path of Exile](https://pathofexile.com) |
| [<img src="http://i.imgur.com/lh5YKoc.png" width="48">](https://www.warframe.com/) | [Warframe](https://www.warframe.com/) |

*Depending on my free time and interest, I may expand the list of supported games or alert methods. If you have one you'd like added, please open a request.*

-----------------


## Requirements:

It runs in [python 3](https://www.python.org/downloads/), and has no UI. It's perfect for throwing onto your own server somewhere, scheduled to run as often as you like. 

The only alert method currently supported is via Discord Webhook, which is a simple way to grant posting access without adding a whole user to your server. You'll need to create a hook in your [Discord Channel Settings](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks). You simply need to edit the URL created by the webhook into the configuration file (```build/config.yml```), like so:
```
alerts: 
    Discord: 
        webhook: [paste link here]
```

While you're in there, make sure to set ```enabled: True``` for whatever Alerts and Games you want active.




