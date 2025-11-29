class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self):
        return f"<Person {self.name} ({self.age})>"


def create_person_list(people_data: list) -> list:
    Person.people = {}
    person_instances = []

    for data in people_data:
        p = Person(data['name'], data['age'])
        person_instances.append(p)

    for data in people_data:
        current_person = Person.people[data['name']]

        wife_name = data.get('wife')
        if wife_name:
            current_person.wife = Person.people[wife_name]

        husband_name = data.get('husband')
        if husband_name:
            current_person.husband = Person.people[husband_name]

    return person_instances