# BeamNG_terrainMaterialCache
Cached Texture files for BeamNG

Hack to fix the Black Terrain found after the 0.24 release on Linux

Still looking for a proper solution

## Usage
```Bash
mkdir ~/.local/share/Steam/steamapps/compatdata/284160/pfx/drive_c/users/steamuser/AppData/Local/BeamNG.drive/0.24/temp/art
mkdir ~/.local/share/Steam/steamapps/compatdata/284160/pfx/drive_c/users/steamuser/AppData/Local/BeamNG.drive/0.24/temp/art/terrainMaterialCache
wget https://github.com/SnoutBug/BeamNG_terrainMaterialCache/releases/download/1.0/terrainMaterialCache.tar.gz
tar -xvf terrainMaterialCache.tar.gz
mv terrainMaterialCache/* ~/.local/share/Steam/steamapps/compatdata/284160/pfx/drive_c/users/steamuser/AppData/Local/BeamNG.drive/0.24/temp/art/terrainMaterialCache/
rm terrainMaterialCache.tar.gz
rm -d terrainMaterialCache
```

### You created a map using a PBR terrain and want to contribute
Delete all files in `%localappdata%\BeamNG.drive\0.24\temp\art\terrainMaterialCache`

Load up your map and only your map

Copy all files inside of `%localappdata%\BeamNG.drive\0.24\temp\art\terrainMaterialCache` into an archive

Upload the archive

Use this link for further steps

https://github.com/SnoutBug/BeamNG_terrainMaterialCache/issues/new?assignees=&labels=enhancement&template=contribute.md&title=
