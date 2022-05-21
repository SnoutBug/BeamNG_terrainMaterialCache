#!/usr/bin/env python3
import sys
import os
import re
import json
import requests
import urllib.request
import tarfile
import hashlib

home = os.path.expanduser("~")
steam = 'steamapps/compatdata/284160/pfx/drive_c/users/steamuser'
game = '/AppData/Local/BeamNG.drive/'

custom = False

tags = []
hash_table = []
#Names of default maps in the GitHub repo
default = ['etk', 'jri', 'utah', 'derby', 'hirochi', 'industrial', 'gridmap_v2', 'small_island',]

try:
    path = str(sys.argv[1])
    custom = True
except:
    path = home + '/.steam/root/' + steam + game
    if not os.path.exists(path): #Flatpak?
        path = home + '/.var/app/com.valvesoftware.Steam/.steam/root/' + steam + game
        if not os.path.exists(path): #Wine?
            path = home + '/.wine/drive_c/users/' + os.getlogin() + game

#The path did not exist
if not os.path.exists(path):
    print('\nWas looking for:')
    if not custom:
        print(' 1. STEAM .deb\n 2. STEAM flatpak\n 3. WINE  "' + path + '"\nbut found nothing.')
        print('\nTry adding the equivalent of %LOCALAPPDATA%\LOCAL\BEAMNG.DRIVE as a parameter\n or try the troubleshooting section of the guide.')
    else:
        print(' "' + path + '"\nbut found nothing.')
        print('Verify that your path leads to %LOCALAPPDATA%\LOCAL\BEAMNG.DRIVE')
    print('\n')
    quit()

#Get the current version to find the correct folder (I can see this breaking - would be better to use latest.lnk)
with open(path + 'version.txt') as version_file:
  ver = version_file.read().split('.')
version = ver[0] + '.' + ver[1] + '/'

#Path of mods folder
mods = path + version + 'mods/'

#Path to extract the cache to
cache = path + version + 'temp/art/'

#Create folders if missing
if not os.path.exists(cache + '/terrainMaterialCache'):
    os.makedirs(cache + '/terrainMaterialCache')

#Get installed mods
with open(mods + 'db.json') as file:
    repodb = json.load(file)

#Get supported maps from GitHub
response = requests.get('https://api.github.com/repos/snoutbug/beamng_terrainmaterialcache/tags').json()

#tag = mod_id
for tag in response:
    tags.append(str(tag['name']))

print('\n\nStarting to update.\nYou can always cancel the download by pressing CTRL + C')
print('\nLooking for modded maps...')

#Generate Hashes for existing .dds
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

for dds in os.listdir(cache + 'terrainMaterialCache/'):
    hash_table.append(md5(cache + 'terrainMaterialCache/' + dds) + '  ' + dds)

#If a used mod is supported by the repo, then only download the textures when there is at least one
#   texture missing or changed
try:
    for mod in repodb['mods']:
        try:
            mod_id = str(repodb['mods'][mod]['modData'].get('resource_id'))
            mod_title = str(repodb['mods'][mod]['modData'].get('title'))
        except:
            continue
        if mod_id in tags:
            print('Verifying ' + mod_title)
            hash_url = 'https://github.com/SnoutBug/BeamNG_terrainMaterialCache/releases/download/' + mod_id + '/md5.txt'
            hash_filename = mod_id + '_md5.txt'
            urllib.request.urlretrieve(hash_url, hash_filename)
            with open(hash_filename) as hash_file:
                hashes = hash_file.read().splitlines()
            os.remove(hash_filename)
            for hash in hashes:
                if not hash in hash_table:
                    print('  > Downloading Files...')
                    url = 'https://github.com/SnoutBug/BeamNG_terrainMaterialCache/releases/download/' + mod_id + '/main.tar.gz'
                    filename = mod_id + '.tar.gz'
                    urllib.request.urlretrieve(url, filename)
                    with tarfile.open(filename) as tar:
                        tar.extractall(cache)
                    os.remove(filename)
                    break #continue with next mod

    #Same as mods but with different naming conventions
    print('\nLooking for default maps...')
    url = 'https://github.com/SnoutBug/BeamNG_terrainMaterialCache/releases/download/default/'
    for filename in default:
        print('Verifying ' + filename)
        hash_url = url + filename + '_md5.txt'
        hash_filename = filename + '_md5.txt'
        urllib.request.urlretrieve(hash_url, hash_filename)
        filename = filename + '.tar.gz'
        with open(hash_filename) as hash_file:
            hashes = hash_file.read().splitlines()
        os.remove(hash_filename)
        for hash in hashes:
            if not hash in hash_table:
                print('  > Downloading Files...')
                urllib.request.urlretrieve(url + filename, filename)
                with tarfile.open(filename) as tar:
                    tar.extractall(cache)
                os.remove(filename)
                break #continue with next map

    print('All Done!')

#Remove all partially downloaded files when cancelled
except KeyboardInterrupt:
    try:
        os.remove(filename)
    except OSError:
        pass
    try:
        os.remove(hash_filename)
    except OSError:
        pass
    print('\nYou cancelled the download.')

quit()
