from mud.world.defines import *
from genesis.dbdict import DBZone
from mud.world.zone import ZoneLink

zone = DBZone()
zone.name = "base"
zone.niceName = "Eden"
zone.missionFile = "base.mis"
zone.climate = RPG_CLIMATE_TEMPERATE
zone.immTransform = "51.7208 -309.756 131.755 0 0 -1 4.20118"

import spawns
import spawngroups
import items
import quests

ZoneLink(name = "base_to_landone",dstZoneName="landone",dstZoneTransform="31.1697 -274.647 126.7 1 0 0 0")
ZoneLink(name = "base_to_landtwo",dstZoneName="landtwo",dstZoneTransform="62.0553 -376.161 135.3 1 0 0 0")
