

from enum import Enum

from .Binners import FloorBinner,CeilingBinner,BoundaryWallBinner,MazeWallBinner,ImageBinner,NanBinner
import numpy as np
class BINNERS(Enum):
    #THE ORDER IS IMPORTANT HERE AND ONLY HERE BECAUSE I'M BAD AT CODING
    NAN_BINNER = NanBinner.NanBinner()
    CUE_BINNER = ImageBinner.ImageBinner()
    HINT_BINNER = ImageBinner.ImageBinner() #2 different instances for no real reason
    FLOOR_BINNER = FloorBinner.FloorBinner()
    CEILING_BINNER = CeilingBinner.CeilingBinner()
    BOUNDARY_BINNER = BoundaryWallBinner.BoundaryWallBinner()
    #Binning is in this specific or der for the pillars
    PILLAR_GREEN_BINNER = MazeWallBinner.MazeWallBinner(center=(4.95,0,-4.95))
    PILLAR_BLUE_BINNER = MazeWallBinner.MazeWallBinner(center=(-4.95,0,-4.95))
    PILLAR_RED_BINNER = MazeWallBinner.MazeWallBinner(center=(4.95,0,4.95))
    PILLAR_YELLOW_BINNER = MazeWallBinner.MazeWallBinner(center=(-4.95,0,4.95))

BOUNDARY_TO_BINNER = {f"wall_{num :02d}" : BINNERS.BOUNDARY_BINNER.value for num in range(1,25)} # 25 walls in total from 1-24



#Blue : m_wall 6,10,21,29
#Green : m_wall 1,5,21,26
#Yellow : m_wall 7,8,12,20
#Red : m_wall 3,4,24,15

#this numbering is strange
PILLAR_TO_BINNER = dict([(f"{dir}GreenWall_GreenPillar",BINNERS.PILLAR_GREEN_BINNER.value) for dir in ("PosX","NegZ","NegX","PosZ")] +
                        [(f"{dir}BlueWall_BluePillar",BINNERS.PILLAR_BLUE_BINNER.value) for dir in ("PosX","NegZ","NegX","PosZ")] +
                        [(f"{dir}RedWall_RedPillar",BINNERS.PILLAR_RED_BINNER.value) for dir in ("PosX","NegZ","NegX","PosZ")] +
                        [(f"{dir}YellowWall_YellowPillar",BINNERS.PILLAR_YELLOW_BINNER.value) for dir in ("PosX","NegZ","NegX","PosZ")])


OBJ_TO_BINNER = { "CueImage" : BINNERS.CUE_BINNER.value,
                  "HintImage" : BINNERS.HINT_BINNER.value,
                  "Ceiling" : BINNERS.CEILING_BINNER.value, 
                  "Ground" : BINNERS.FLOOR_BINNER.value
                  };OBJ_TO_BINNER.update(BOUNDARY_TO_BINNER);OBJ_TO_BINNER.update(PILLAR_TO_BINNER)

_BINNER_LIST = [e for e in BINNERS]
_SIZES = [np.prod(binner.value.bin_cache.shape) for binner in _BINNER_LIST]
_OFFSETS = [0] #bins are 0-indexed
for size in _SIZES :
    _OFFSETS.append(_OFFSETS[-1] + size)
_OFFSETS = _OFFSETS[0:len(_SIZES)]

BINNER_TO_BASE_OFFSET = {binner : offset for (binner,offset) in zip(_BINNER_LIST,_OFFSETS)}

#this one controls relative order of binning
PILLARS = [pillar for pillar in (BINNERS.PILLAR_GREEN_BINNER.value,
                                                BINNERS.PILLAR_BLUE_BINNER.value,
                                                BINNERS.PILLAR_RED_BINNER.value,
                                                BINNERS.PILLAR_YELLOW_BINNER.value)]

def poster_matcher(point) :
    dists_to_pillars =[np.sqrt(np.sum(np.square(np.array(point) - np.array(pillar.center)))) 
                       for pillar in PILLARS]
    
    return PILLARS[np.argmin(dists_to_pillars)]







