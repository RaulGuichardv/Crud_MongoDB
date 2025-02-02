from bson import ObjectId
from fastapi import APIRouter, HTTPException
from config.db import client
from schemas.user import userEntity, usersEntity
from models.user import User

router = APIRouter(prefix="/user",
                   tags=["user"])

db_user = client["grupo"]["users"]

@router.get("/")
async def find_all_user():
    return usersEntity(db_user.find())
    


@router.get("/{id}")
async def find_user(id: str):
    return userEntity(db_user.find_one({"_id": ObjectId(id)}))
 


@router.post("/")
async def create_user(user: User):
    new_user = dict(user)
    del new_user["id"]
    id = db_user.insert_one(new_user).inserted_id
    print(type(id))
    new_user = db_user.find_one({"_id": id})
    return userEntity(new_user)


@router.put("/{id}", response_model=User)
async def update_user(id: str, user: User):
    db_user.update_one({"_id": ObjectId(id)}, {"$set": dict(user)})
    return userEntity(db_user.find_one({"_id": ObjectId(id)}))

@router.delete("/{id}")
async def delete_user(id: str):
    return userEntity(db_user.find_one_and_delete({"_id": ObjectId(id)}))