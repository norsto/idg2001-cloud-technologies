from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_root():
    return 'hei'

if __name__ == '__main__':
    import subprocess
    subprocess.run(['uvicorn', '2025_my_api:app', '--reload'])