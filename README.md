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
