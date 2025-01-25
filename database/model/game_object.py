from sqlalchemy import Column, DateTime, String, Integer, Boolean, func
from database._db import Base

class GameObject(Base):
    __tablename__ = 'game_object'

    id                  = Column(Integer, primary_key=True)
    map_id              = Column(Integer)
    x                   = Column(Integer)
    y                   = Column(Integer)
    width               = Column(Integer)
    height              = Column(Integer)
    frameX              = Column(Integer)
    frameY              = Column(Integer)
    speed_monotic               = Column(Integer)
    moving              = Column(Boolean)
    img_src             = Column(String(length=100))
    next_move_monotonic = Column(float)
    idle_time_monotonic = Column(float)
    player              = Column(Boolean)
    static              = Column(Boolean)

    def json(self):
        return {
            'id'     : self.id,
            'map_id' : self.map_id,
            'x'      : self.x,      
            'y'      : self.y,      
            'width'  : self.width, 
            'height' : self.height,
            'frameX' : self.frameX, 
            'frameY' : self.frameY, 
            'speed_monotic'  : self.speed_monotic,  
            'moving' : self.moving, 
            'img_src': self.img_src,
            'next_move_monotonic': self.next_move_monotonic,
            'idle_time_monotonic': self.idle_time_monotonic,
            'player' : self.player,
            'static' : self.static,
        }