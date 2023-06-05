# DonkeyFileShare

This repo holds files and info needed to use [Donkey](https://github.com/theTwist84/ManagedDonkey)

### Dev Generated Files
- `maps\tag_list.csv`
	- This is being worked on and updated all the time.

- `maps\info\*.mapinfo`
	- You can acquired these via [MCC](https://store.steampowered.com/app/976730/) or [Halo 3 Mod Tools - MCC](https://store.steampowered.com/app/1695791/) and [Halo 3: ODST Mod Tools - MCC](https://store.steampowered.com/app/1695794/).
	- Eventually I'll create a project to generate these from a file.

- `maps\info\*.campaign`
	- You can acquired these via [MCC](https://store.steampowered.com/app/976730/) or [Halo 3 Mod Tools - MCC](https://store.steampowered.com/app/1695791/) and [Halo 3: ODST Mod Tools - MCC](https://store.steampowered.com/app/1695794/).
	- Eventually I'll create a project to generate these from a file.

### User Generated Files
- `game_variants\*.bin`
	- You can acquired these via [MCC](https://store.steampowered.com/app/976730/).
	- You can generate these with `net_build_game_variant` in [Donkey](https://github.com/theTwist84/ManagedDonkey) ~or [Halo 3 Mod Tools - MCC](https://store.steampowered.com/app/1695791/)~ the tools crash (343 pls fix).

- `hopper_game_variants\*.bin`
	- You can acquired these via [MCC](https://store.steampowered.com/app/976730/).

- `map_variants\*.mvar`
	- You can generate these with `net_build_map_variant` in [Donkey](https://github.com/theTwist84/ManagedDonkey)

## Other Files
- `init.txt`
	- This is just like the one you can find in the tools but it uses [Donkey](https://github.com/theTwist84/ManagedDonkey) commands, some commands are the same between [Donkey](https://github.com/theTwist84/ManagedDonkey) and the tools

- `preferences.txt`
	- The user can use any filename and load that file via `load_preferences_from_file <filename.txt>`
	- This is being worked on and updated all the time.
	- Eventually I'll create a command to generate this.

- `customization.txt`
	- The user can use any filename and load that file via `load_customization_from_file <filename.txt>`
	- This is being worked on and updated all the time.
	- If no customization file exists a `customization_info.txt` will be created
