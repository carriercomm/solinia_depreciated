# Copyright (C) 2004-2007 Prairie Games, Inc
# Please see LICENSE.TXT for details

#!/usr/bin/env python

from sqlite3 import dbapi2 as sqlite
import shutil
from twisted.internet import reactor
import traceback
import sha
import sys
import os

from serverdb import CREATE_PLAYER_BUFFER_SQL

sys.path.append(os.getcwd())

from mud.gamesettings import *


def ConvertWorldDBToCharacterDB():
    from mud.worldserver.charutil import ExtractCharactersThread
    from mud.common.dbconfig import SetDBConnection
    try:
        os.makedirs("./data/character")
    except:
        pass
    shutil.copyfile("%s/data/worlds/multiplayer.baseline/world.db"%GAMEROOT,"./data/character/character.db")
    conn = sqlite.connect("./data/character/character.db",isolation_level = None)
    cursor = conn.cursor()
    cursor.execute("BEGIN TRANSACTION;")
    cursor.executescript(CREATE_PLAYER_BUFFER_SQL)
    cursor.execute("END TRANSACTION;")
    cursor.close()
    conn.close()


def main():
    ConvertWorldDBToCharacterDB()


if __name__ == '__main__':
    print "Creating Character Database..."
    main()
    print "Done!"