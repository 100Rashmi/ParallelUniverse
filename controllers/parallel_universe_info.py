import uuid
from operator import and_

from sqlalchemy import func

from db.db_connection import db_connection
from db.models import Person, Family, Universe


def create_person(body):
    person_id = body["person_id"]
    power = body["power"]
    universe_id = body["universe_id"]
    family_id = body["family_id"]

    # insert data into person table
    person = Person()
    person.person_id = person_id
    person.family_id = family_id
    person.power = power
    person.universe_id = universe_id

    db_session = db_connection().get_session()
    create_family_if_not_exist(family_id, db_session)
    create_universe_if_not_exist(universe_id, db_session)

    db_session.add(person)
    try:
        db_connection().commit()
        return True
    except Exception as ex:
        print ex
        db_session.rollback()


def create_family_if_not_exist(family_id, db_session):
    family_info = db_session.query(Family).filter(Family.family_id == family_id).first()
    if not family_info:
        # insert data into family table
        family = Family()
        family.family_id = family_id
        db_session.add(family)
        try:
            db_connection().commit()
        except Exception as ex:
            print ex


def create_universe_if_not_exist(universe_id, db_session):
    universe_info = db_session.query(Universe).filter(Universe.universe_id == universe_id).first()
    if not universe_info:
        # insert data into universe table
        universe = Universe()
        universe.universe_id = universe_id
        db_session.add(universe)
        try:
            db_connection().commit()
        except Exception as ex:
            print ex


def families_for_universe(universe_id):
    db_session = db_connection().get_session()
    families = db_session.query(Person.family_id).filter(Person.universe_id == universe_id).all()
    family_ids = set()
    for family in families:
        family_ids.add(family[0])

    return list(family_ids)


def check_power_for_same_family_identifier():
    db_session = db_connection().get_session()
    data = db_session.query(Person.family_id, Person.universe_id, func.sum(Person.power)).group_by(Person.family_id,
                                    Person.universe_id).order_by(Person.family_id).all()

    family_power_map = {}
    for entry in data:
        if entry[0] in family_power_map:
            (family_power_map[entry[0]]).append([entry[1], str(entry[2])])
        else:
            family_power_map[entry[0]] = [[entry[1], str(entry[2])]]

    res_map = {}
    for key in family_power_map:
        values = family_power_map[key]
        j = 0
        for i in range(1,len(values)):
            if int(values[j][1]) != int(values[i][1]):
                res_map[key] = family_power_map[key]
                break
            j+=1

    return res_map


def balance_families():
    res_map = check_power_for_same_family_identifier()
    if res_map:
        for key in res_map:
            values = res_map[key]
            j = 0
            for i in range(1, len(values)):
                max_power = max(int(values[j][1]),int(values[i][1]))
                if int(values[i][1]) != max_power:
                    diff_power = max_power - int(values[i][1])
                    universe = values[i][0]
                else:
                    diff_power = max_power - int(values[j][1])
                    universe = values[j][0]

                j += 1
                if diff_power:
                    body = {'person_id':str(uuid.uuid4()) ,'power': diff_power, 'universe_id':universe , 'family_id':  key}
                    create_person(body)










