from generate_image import generate_image
from instagram_bot import login_user
from random import randint

prompts=[]
with open('prompts.txt','r') as file:
    prompts=file.readlines()

PROMPT=prompts[randint(0,len(prompts)-1)]

generate_image(
    f'Hey. This is a picture of me. Can you generate an image of me {PROMPT} ' +
    'and also generate a cool instagram caption'
)

cl=login_user()
caption=''
with open('generated_text.txt','r',encoding='utf-8') as file:
    caption=str(file.read()).split('**Cool Instagram Caption:**')[-1].split('\n')[-1]

media=cl.photo_upload(
    'generated_image.jpg',
    caption=caption
)

print('Success')