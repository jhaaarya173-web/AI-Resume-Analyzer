import database

def search(name):

    rows = database.get_all()

    result = []

    for row in rows:

        if name.lower() in row[1].lower():

            result.append(row)

    return result