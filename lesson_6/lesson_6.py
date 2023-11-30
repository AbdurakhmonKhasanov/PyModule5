from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:1@localhost:5432/postgres')

base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    fullname = Columna("fullname", VARCHAR(255))
    username = Columna("username", VARCHAR(255), unique = True)
    password= Columna("password", VARCHAR(10), CheckConstraint("length(password)>4"))
    join_at = Columna("fullname", TIMESTAMP(timezone = True , default= current_timestamp))


class Address(Base):
    __tablename__ = "addresses"
    id = Column("id", Integer , autoincrement=True, primary_key = True)
   country = Columna("country", VARCHAR(100))


students = select(Student).where(Student.id==2)
students = session.execute(students)
for i in students :
    print(i)













