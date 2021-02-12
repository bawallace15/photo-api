from fastapi import FastAPI, File, UploadFile
import os
import yaml

app = FastAPI()

def updateYaml(filepath):
    with open('/photo-app/piclist.yml', 'r') as f:
        piclist = yaml.safe_load(f)
    piclist['order'].append(filepath)
    with open('/photo-app/piclist.yml', 'w') as f:
        yaml.dump(piclist, f)

@app.get('/get-pics')
def getPictures():
    return os.listdir('/photo-app')

@app.post('/send-pics')
async def postPictures(image: UploadFile = File(...)):
    file_name = f'/photo-app/{image.filename}'
    with open(file_name,'wb+') as f:
        f.write(image.file.read())
        f.close()
    updateYaml(f'/photo-app/{image.filename}')
    print(os.listdir('/photo-app'))
