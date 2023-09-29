

from enum import Enum

from .Binners import FloorBinner,CeilingBinner,BoundaryWallBinner,MazeWallBinner,ImageBinner
import numpy as np
class BINNERS(Enum):
    #THE ORDER IS IMPORTANT BECAUSE I'M BAD AT CODING
    IMAGE_BINNER = ImageBinner.ImageBinner()
    FLOOR_BINNER = FloorBinner.FloorBinner()
    CEILING_BINNER = CeilingBinner.CeilingBinner()
    BOUNDARY_BINNER = BoundaryWallBinner.BoundaryWallBinner()
    PILLAR_BLUE_BINNER = MazeWallBinner.MazeWallBinner(center=(-4.95,0,-4.95))
    PILLAR_GREEN_BINNER = MazeWallBinner.MazeWallBinner(center=(4.95,0,-4.95))
    PILLAR_YELLOW_BINNER = MazeWallBinner.MazeWallBinner(center=(-4.95,0,4.95))
    PILLAR_RED_BINNER = MazeWallBinner.MazeWallBinner(center=(4.95,0,4.95))

BOUNDARY_TO_BINNER = {f"wall_{num :02d}" : BINNERS.BOUNDARY_BINNER.value for num in range(1,25)} # 25 walls in total from 1-24



#Blue : m_wall 6,10,21,29
#Green : m_wall 1,5,21,26
#Yellow : m_wall 7,8,12,20
#Red : m_wall 3,4,24,15

#this numbering is strange
PILLAR_TO_BINNER = dict([(f"m_wall_{num}",BINNERS.PILLAR_BLUE_BINNER.value) for num in (6,10,21,29)] +
                        [(f"m_wall_{num}",BINNERS.PILLAR_GREEN_BINNER.value) for num in (1,5,21,26)] +
                        [(f"m_wall_{num}",BINNERS.PILLAR_YELLOW_BINNER.value) for num in (7,8,12,20)] +
                        [(f"m_wall_{num}",BINNERS.PILLAR_RED_BINNER.value) for num in (3,4,24,15)])

# print(BINNERS.CEILING_BINNER.value)
OBJ_TO_BINNER = { "Ceiling" : BINNERS.CEILING_BINNER.value, 
                  "Ground" : BINNERS.FLOOR_BINNER.value,
                  "CueImage" : BINNERS.IMAGE_BINNER.value,
                  "HintImage" : BINNERS.IMAGE_BINNER.value
                  };OBJ_TO_BINNER.update(BOUNDARY_TO_BINNER);OBJ_TO_BINNER.update(PILLAR_TO_BINNER)

_BINNER_LIST = [e.value for e in BINNERS]
_SIZES = [np.prod(binner.bin_cache.shape) for binner in _BINNER_LIST]
_OFFSETS = [0]
for size in _SIZES :
    _OFFSETS.append(sum(_OFFSETS) + size)
_OFFSETS = _OFFSETS[0:len(_SIZES)]
BINNER_TO_BASE_OFFSET = {binner : offset for (binner,offset) in zip(_BINNER_LIST,_OFFSETS)}


_PILLARS = [pillar for pillar in (BINNERS.PILLAR_BLUE_BINNER.value,
                                                BINNERS.PILLAR_GREEN_BINNER.value,
                                                BINNERS.PILLAR_YELLOW_BINNER.value,
                                                BINNERS.PILLAR_RED_BINNER.value)]

def poster_matcher(point) :
    return _PILLARS[np.argmax(np.abs(point - np.array([pillar.center for pillar in _PILLARS])))]







