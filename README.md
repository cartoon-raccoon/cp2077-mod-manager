# cyberpunk-mod-manager

This is a simple command-line mod manager for Cyberpunk 2077, meant to fill
the role of Vortex in a more transparent and simpler way. It provides Nexus
Mods API integration and file tracking, to make the process of installing
and tracking mods much easier than manually.

## Purpose

It is common practice within the Cyberpunk 2077 modding community to manually
manage one's mods. Normally, one would download the file manually, and extract
it into the game install directory by hand. However, uninstalling mods is still
a cumbersome process, and tracking them is also extremely error prone.
For example, to uninstall a mod, I would have to search up the mod on Nexus to
see what files it added, then delete each file manually. Additionally, when
looking through mods, I would have to remember to check the last updated time,
as some mods may not have been updated to be compatible with Update 2.12. Many
times have I downloaded a mod I liked, only to have it crash my game, or not
work, because I failed to check if it was compatible with 2.12.

Additionally, Linux users would not be able to use Vortex due to how Wine works,
leaving manual installation as the only option. This program aims to help them
with that.

## What this program does

This program attempts to automate the manual method of mod installation,
without the opaqueness and complexity of Vortex. At its core, all it does is
unpack the files, copy them to the correct directories in the game install
directory, and then store all the mod's associated data in an SQLite
database. It also has more advanced features such as update
tracking, and can detect if a mod was last updated before the release of
Update 2.12. Lastly, if the user is a premium user, it can also directly
download the file for the user (This is a Nexus API limitation).

If a mod has an unrecognized directory structure, the user still has the
option to manually install the mod, and tell the program all the files that were
installed and where they were installed, making it easier to uninstall the mod
down the line, if needed.

## What this program does not do

CPMM is designed for one purpose, and one purpose only: to help you
install and track your Cyberpunk mods. As such, it does not and will not
implement functionality outside of this scope, even if the Nexus API supports it,
such as endorsements, or listing trending mods.

Another limitation is dependency tracking. The Nexus API does not provide this
information, so it is on the user to make sure all dependencies are installed.
CPMM does provide some basic tracking functionality, such as checking if a
certain mod is installed.

## Usage

## Configuration

Currently, there are two required config keys:

- `ApiKey`: This is the API key used to access the Nexus Mods API.
- `GameDirectory`: This is where the game itself is installed.
