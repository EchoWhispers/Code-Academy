from sqlalchemy import create_engine, UniqueConstraint, Table, ForeignKey,  Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



engine = create_engine("sqlite:///projects.sqlite") #nurodom vieta kur db sukurs

Base = declarative_base()

parent_child_association_table = Table(
    "parent_child",
    Base.metadata,
    Column("parent_id", Integer, ForeignKey("parent.id")),
    Column("child_id", Integer, ForeignKey("child.id")),
    UniqueConstraint("parent_id", "child_id", name = "parent_child_uc"))#neleidzia dublikuoti id)
class Parent(Base):
    __tablename__ = "parent"
    id = Column(primary_key = True)
    name = Column("name")
    surname = Column ("surname")
    child_id = Column(Integer, ForeignKey("child.id"))
    child = relationship("Child", secondary = parent_child_association_table, back_populates = "parents")


class Child(Base):
    __tablename__ = "child"
    id = Column(primary_key=True)
    name = Column("name")
    surname = Column("surname")
    school = Column( "school")
    parents = relationship("Parent", secondary = parent_child_association_table, back_populates = "child")

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()


child = Child(name = "Petras", surname = "Petraitis", school = "nera")
parent = Parent(name = "jonas", surname = "jonaitis", child = child) #pridedam vaika

print(parent.name)
print(parent.surname)
print(parent.child.name)
print(parent.child.surname)
print(parent.child.school)

session.add(child)


child = session.get(Child, 1) #traukiam vaika is saraso taip ir teva galim traukt is parent
parent = session.get(Parent, 1) #traukiam teva
#child.parents.remove(child.parent[0]) #atkabinamt id jei nereikia

session.commit()