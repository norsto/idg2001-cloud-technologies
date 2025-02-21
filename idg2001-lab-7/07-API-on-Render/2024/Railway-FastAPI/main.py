from fastapi import FastAPI


app = FastAPI()

@app.get("/info")
async def root():
    try:
        import os
        message = {
            "greeting": "Hello, World!",
            "message": "Welcome to FastAPI!",
            "pwd": str(os.getcwd()),
            "listdir": str(os.listdir()),
            "listdir..": str(os.listdir("..")),
            "listdir/": str(os.listdir("/")),
            "env": str(os.environ)
        }
    except Exception as e:
        message = {
            "info": "Error",
            "error": str(e)
        }

    # message = {"hi": "there"}
    return message


# Simulated database
CONTACT_DB = [
    {'item_id': 0, 'name': 'Paul'},
    {'item_id': 1, 'name': 'Mary'},
    {'item_id': 2, 'name': 'John'}
]


# Simple get
@app.get('/')
def read_root():
    return {'Hello': 'World! :D'}

# Simple post
@app.post('/users')
def create_root(item: dict):
    item['item_id'] = 3  # Do whatever update.
    return item  # Return updated thingy.


@app.get('/items')
def read_items():
    return CONTACT_DB


@app.get('/items/{item_id}')
def read_item(item_id: int, q = None):
    for item in CONTACT_DB:
        if item['item_id'] == item_id:
            return item
    return {'item_id': item_id, 'error': 'Item not found'}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: dict):
    # item['item_id'] = len(CONTACT_DB)
    item['item_id'] = item_id
    CONTACT_DB.append(item)
    return item


@app.post('/items')
def create_item(item: dict):
    item['item_id'] = len(CONTACT_DB)
    CONTACT_DB.append(item)
    return item


@app.delete('/items/{item_id}')
def delete_item(item_id: int):
    for index, item in enumerate(CONTACT_DB):
        if item['item_id'] == item_id:
            item_id = item['item_id']
            del CONTACT_DB[index]
            return {'item_id': item_id, 'len': len(CONTACT_DB)}
    return {'item_id': item_id, 'error': 'Item not found'}
