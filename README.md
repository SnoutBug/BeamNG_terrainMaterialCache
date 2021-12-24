# BeamNG_terrainMaterialCache
Cached Texture files for BeamNG

Hack to fix the Black Terrain found after the 0.24 release on Linux

Still looking for a proper solution

Massive thanks to Bauer33333 for providing the pre-generated textures for this transplant.

## Usage
### Default Maps
```Bash
mkdir ~/.steam/root/steamapps/compatdata/284160/pfx/drive_c/users/steamuser/AppData/Local/BeamNG.drive/0.24/temp/art
cd "$_"
url=github.com/SnoutBug/BeamNG_terrainMaterialCache/releases/download/default/
wget ${url}etk.tar.gz
wget ${url}jri.tar.gz
wget ${url}utah.tar.gz
wget ${url}derby.tar.gz
wget ${url}hirochi.tar.gz
wget ${url}industrial.tar.gz
wget ${url}gridmap_v2.tar.gz
wget ${url}small_island.tar.gz
ls *.tar.gz | xargs -n 1 tar -xvf
rm *.tar.gz
cd ~/
```
### BeamNG Repository (Mods)
 1. Look at the URL of your map (eg. www.beamng.com/resources/natural-playground.18030/)
 2. Copy the number behind the period (18030) to the following URL like this: www.github.com/SnoutBug/BeamNG_terrainMaterialCache/releases/tag/18030
 3. If the page exists, you will find a one-liner in the release's description which you can then use to downlad the textures

## Contribute
### You created a map using a PBR terrain and want to contribute
Delete all files in `%localappdata%\BeamNG.drive\0.24\temp\art\terrainMaterialCache`

Load up your map and only your map

Copy all files inside of `%localappdata%\BeamNG.drive\0.24\temp\art\terrainMaterialCache` into an archive

Upload the archive

Use this link for further steps

https://github.com/SnoutBug/BeamNG_terrainMaterialCache/issues/new?assignees=&labels=enhancement&template=contribute.md&title=
