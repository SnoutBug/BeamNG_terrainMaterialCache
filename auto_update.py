import sys
import os
import re
import json
import requests
import urllib.request
import tarfile

try:
    installation = str(sys.argv[1])
except:
    installation = '/.steam/root/steamapps/compatdata/284160/pfx/drive_c/users/steamuser/AppData/Local/BeamNG.drive/'

tags = []
default = ['etk.tar.gz', 'jri.tar.gz', 'utah.tar.gz', 'derby.tar.gz', 'hirochi.tar.gz', 'industrial.tar.gz', 'gridmap_v2.tar.gz', 'small_island.tar.gz',]

path = os.path.expanduser("~") + installation

if not os.path.exists(path):
    print('Please make sure that you entered the right path\npython3 auto_update.py PATH_TO_/AppData/Local/BeamNG.drive/')
    quit()

with open(path + 'version.txt') as version_file:
  ver = version_file.read().split('.')

version = ver[0] + '.' + ver[1] + '/'
mods = path + version + 'mods/'
cache = path + version + 'temp/art/'

if not os.path.exists(cache + '/terrainMaterialCache'):
    os.makedirs(cache + '/terrainMaterialCache')

with open(mods + 'db.json') as file:
    repodb = json.load(file)

response = requests.get('https://api.github.com/repos/snoutbug/beamng_terrainmaterialcache/tags').json()

for tag in response:
    tags.append(str(tag['name']))

print('Starting to update.\nYou can always cancel the download by pressing CTRL + C')

for mod in repodb['mods']:
    mod_id = str(repodb['mods'][mod]['modData'].get('resource_id'))
    mod_title = str(repodb['mods'][mod]['modData'].get('title'))
    if mod_id in tags:
        print('Getting textures for ' + mod_title)
        url = 'https://github.com/SnoutBug/BeamNG_terrainMaterialCache/releases/download/' + mod_id + '/main.tar.gz'
        filename = mod_id + '.tar.gz'
        urllib.request.urlretrieve(url, filename)
        with tarfile.open(filename) as tar:
            tar.extractall(cache)
        os.remove(filename)

url = 'https://github.com/SnoutBug/BeamNG_terrainMaterialCache/releases/download/default/'
for map in default:
    print('Getting textures for ' + re.sub('\.tar.gz$', '', map))
    urllib.request.urlretrieve(url + map, map)
    with tarfile.open(map) as tar:
        tar.extractall(cache)
    os.remove(map)

print('All Done!')
