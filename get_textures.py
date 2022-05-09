#!/usr/bin/env python3
import sys
import os
import re
import json
import requests
import urllib.request
import tarfile
import hashlib
import tkinter
import multiprocessing

def run():
    root = tkinter.Tk()
    root.title('BeamNG.drive')
    label = tkinter.Label(root, text="BeamNG.drive will start shortly!")
    label.pack()

    root.mainloop()

proc = multiprocessing.Process(target=run, args=())
proc.start()

try:
    installation = str(sys.argv[1])
except:
    installation = '/.steam/root/steamapps/compatdata/284160/pfx/drive_c/users/steamuser/AppData/Local/BeamNG.drive/'

tags = []
hash_table = []
default = ['etk', 'jri', 'utah', 'derby', 'hirochi', 'industrial', 'gridmap_v2', 'small_island',]

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

try:
    for mod in repodb['mods']:
        mod_id = str(repodb['mods'][mod]['modData'].get('resource_id'))
        mod_title = str(repodb['mods'][mod]['modData'].get('title'))
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

proc.terminate()
quit()
