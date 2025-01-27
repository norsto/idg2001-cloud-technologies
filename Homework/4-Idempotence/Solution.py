db = [
    {'id': 1, 'message': 'hello'},
    {'id': 2, 'message': 'hi'},
    {'id': 3, 'message': 'howdy'},
]
print(db)


# Simple way
new_dict = {'id': 4, 'message': 'hey'}


##########################
## Non-idempotent solution
##########################

# db.append(new_dict)


##########################
## Idempotent solution
##########################

# Check if id exists in database.
def in_db(d):
    for db_d in db:
        if db_d['id'] == d['id']:
            return True
    return False

# Add only if id does not exists in database.
def secure_add(d):
    # Already exists?
    while not in_db(d):
        db.append(d)


# Example run
secure_add(new_dict)
print(db)

secure_add(new_dict)
print(db)

secure_add(new_dict)
print(db)

secure_add({'id': 5, 'message': 'hey'})
print(db)
