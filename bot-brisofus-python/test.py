import time
from src.map_tile import Game, MapPoint


game =Game(MapPoint.HDV_RESSOURCE_BONTA)

time.sleep(1)
game.goToMap(MapPoint.ATELIER_CORDONNIER)