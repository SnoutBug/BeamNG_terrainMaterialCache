#!/usr/bin/env python3
import webbrowser
import subprocess
import sys
import os

home = os.path.expanduser( "~" )
sub_steampath = '?'
sub_steamuser = 'steamapps/compatdata/284160/pfx/drive_c/users/steamuser/'
sub_bin       = 'steamapps/common/BeamNG.drive/BinLinux/BeamNG.drive.x64'
sub_winlocal  = 'AppData/Local/BeamNG.drive/'
sub_nixlocal  = '.local/share/BeamNG.drive/'

map = str( sys.argv[1] )
args = ['?', '-level', map + '/']

sub_steampath = home + '/.steam/root/'
path = sub_steampath + sub_steamuser + sub_winlocal
if not os.path.exists( path ): #Flatpak?
    sub_steampath = home + '/.var/app/com.valvesoftware.Steam/.steam/root/'
    path          = sub_steampath + sub_steamuser + sub_winlocal
    if not os.path.exists( path ): #?
        print( 'Non-Steam is not supported right now...' )
        quit( )

#The path did not exist
if not os.path.exists( path ):
    quit( )

args[0] = sub_steampath + sub_bin

#Get the current version
with open( path + 'version.txt' ) as version_file:
  ver = version_file.read( ).split( '.' )
version = ver[0] + '.' + ver[1] + '/'


nix_cache = home + '/' + sub_nixlocal + version + 'temp/art/terrainmaterialcache'
#  Move already existing cache for fresh generation
try:
    os.rename( nix_cache, home + '/' + sub_nixlocal + version + 'temp/art/existing_terrainmaterialcache' )
except:
    pass


print( '[i] Launching BeamNG.drive on ' + map )
process = subprocess.Popen( args, stdout=subprocess.PIPE, stderr=subprocess.PIPE )

while True:
    realtime_output = process.stdout.readline( )

    if realtime_output == '' and process.poll( ) is not None:
        break

    if realtime_output:
        if '|I|LoadingManager|  ===== Terrain'     in str( realtime_output ):
            print( '\n[i] Generating textures started' )
            print( '    This may take a while. Go grab a cup of coffee...' )
        elif '|I|LoadingManager|     TerrainBlock' in str( realtime_output ):
            print( '[✔] Finished generating!' )
            process.terminate( )
            break
            
print( '\n[i] Moving files...' )
for f in os.listdir( nix_cache ):
    try:
        os.remove( path + version + 'temp/art/terrainMaterialCache/' + f )
    except:
        try:
            os.remove( path + version + 'temp/art/terrainMaterialCache/' + f.upper( ) )
        except:
            pass
        pass
    os.rename( nix_cache + '/' + f, path + version + 'temp/art/terrainMaterialCache/' + f )
os.rmdir( nix_cache )
try:
    os.rename( home + '/' + sub_nixlocal + version + 'temp/art/existing_terrainmaterialcache', nix_cache )
except:
    pass

print( '[✔] Finished moving files!' )

#os.system("xdg-open steam://rungameid/284160")
