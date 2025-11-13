import json
from typing import Literal

import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel
app = FastAPI()


@app.get("/test")
def base_endpoint():
    return { "msg":" hi from test"}

@app.get("/test/{name}")
def base_endpoint2(name:str):
    with open("names.txt", 'r',encoding="utf-8") as f:
        f.readlines()
    with open("names.txt", 'a',encoding="utf-8") as f:
        f.write(f"{name}\n")
    return {"msg":"saved user"}

class Caesar_items(BaseModel):
    text: str
    offset: int
    mode: Literal["encrypt","decrypt"]

@app.post( "/caesar" )
def caesar_cipher_endpoint(items: Caesar_items ):
    if items.mode=="encrypt":
        result=encrypt(items.text,items.offset)
        return { "encrypted_text" :{result} }
    else:
        result=decrypt(items.text,items.offset)
        return {"decrypted_text": {result}}

@app.get("/fence/encrypt")
def fence_cipher_endpoints(text):
    result=rail_fence_cipher(text)
    return { "encrypted_text": {result} }

@app.post("/fence/decrypt")
def fence_cipher(text:str):
    result=fence_cipher1(text)
    return { "decrypted": {result} }





def encrypt(text,offset):
    arr=['a','b','c','d','e','f','j','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    word=""
    j=0
    for i in text:
        temp=i
        while temp!=arr[j]:
            j+=1
        word+=arr[(j+offset)%26]
    return word

def decrypt(text,offset):
    arr=['a','b','c','d','e','f','j','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    word=""
    j=0
    for i in text:
        temp=i
        while temp!=arr[j]:
            j+=1
        word+=arr[(j-offset)%26]
    return word


def rail_fence_cipher(text):
    f=text.replace(' ','')
    text_z=''
    text_ez=''
    for i in range(len(f)):
        if i%2==0:
            text_z+=f[i]
        else:
           text_ez+=f[i]
    return text_z+text_ez

def fence_cipher1(text):
    result=""
    lens=len(text)//2
    text_z =text[:lens]
    text_ez=text[lens:]
    for i in range (lens):
        result+=text_z[i]
        result+=text_ez[i]
    return result









if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)