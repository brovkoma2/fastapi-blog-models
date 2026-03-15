from typing import List, Optional
from sqlalchemy.orm import Session

from src.models import Location


class LocationRepository:

    def get_all(self, session: Session, skip: int = 0, limit: int = 10) -> List[Location]:
        return session.query(Location).offset(skip).limit(limit).all()

    def get_by_id(self, session: Session, location_id: int) -> Optional[Location]:
        return session.query(Location).filter(Location.id == location_id).first()

    def get_by_name(self, session: Session, name: str) -> Optional[Location]:
        return session.query(Location).filter(Location.name == name).first()

    def create(self, session: Session, name: str) -> Location:
        location = Location(name=name)
        session.add(location)
        session.flush()
        return location

    def update(self, session: Session, location: Location, name: str) -> Location:
        location.name = name
        return location

    def delete(self, session: Session, location: Location) -> None:
        session.delete(location)