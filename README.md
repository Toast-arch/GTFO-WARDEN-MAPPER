# GTFO-WARDEN-MAPPER

GTFO WARDEN MAPPER is a GTFO log reading scripting meant for speedrunning.

It can be used with or without level specific packages that enhance log analyis and mapping output.

Without level specific json files, the tool will extract and highlight cell and cargo zones, key zones and "ri", and much more directly into your terminal.
If level specific json files are provided the tool can also create ID, PD, GLP, KEY, etc.. visual maps.

Seed learning is WIP and experimental.

REQUIREMENTS:
 - python3+
 - python PIL : install with "pip install pillow"

HOW TO USE :
- Run the script a couple seconds after the level has started (try again a couple seconds later still if no result or less than 6 valid IDs)
- Go to the _GENERATED images for results
- Run the script with --help option for more info