from sqlalchemy.orm import Session
from models.models import Device ,Schedule, User, Gpio

class DeviceRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, device: Device) -> Device:
        self.db.add(device)
        self.db.commit()
        self.db.refresh(device)
        return device
    
    def update(self, device: Device) -> Device:
        self.db.merge(device)
        self.db.commit()
        self.db.refresh(device)
        return device
    
    def find(self, id: int) -> Device:
        return self.db.query(Device).filter(Device.id == id).first()

    def delete_by_id(self, id: int) -> None:
        device = self.db.query(Device).filter(Device.id == id).first()
        if device is not None:
            self.db.delete(device)
            self.db.commit()

class ScheduleRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(self, schedule: Schedule) -> Schedule:
        self.db.add(schedule)
        self.db.commit()
        self.db.refresh(schedule)
        return schedule
    
    def update(self, schedule: Schedule) -> Schedule:
        self.db.merge(schedule)
        self.db.commit()
        self.db.refresh(schedule)
        return schedule
    

    def find(self, id: int) -> Schedule:
        return self.db.query(Schedule).filter(Schedule.id == id).first()

    def delete_by_id(self, id: int) -> None:
        schedule = self.db.query(Schedule).filter(Schedule.id == id).first()
        if schedule is not None:
            self.db.delete(schedule)
            self.db.commit()


class UserRepository:

    def __init__(self ,db: Session):
        self.db = db

    def save(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, user:User) ->User:
        self.db.merge(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    

    def find(self ,id: int) -> User:
        return self.db.query(User).filter(User.id == id ).first()

    def delete_by_id(self ,id: int) -> None:
        user = self.db.query(User).filter(User.id == id ).first()
        if user is not None:
            self.db.delete(user)
            self.db.commit()

class GpioRepository:

    def __init__(self , db:Session):
        self.db = db

    def save(self ,gpio:Gpio) -> Gpio:
        self.db.add(gpio)
        self.db.commit()
        self.db.refresh(gpio)
        return gpio

    
    def update(self, gpio:Gpio) -> Gpio:
        self.db.merge(gpio)
        self.db.commit()
        self.db.refresh(gpio)
        return gpio


    def find(self ,id: int) -> Gpio:
        return self.db.query(Gpio).filter(Gpio.id == id ).first()