from person import Person

def from_data(data: str):
    people = []
    
    lines = data.strip().split('\n')[1:]
    for line in lines:
        person_info = line.strip().split(',')[1:]
        people.append(Person(*person_info))

    return people