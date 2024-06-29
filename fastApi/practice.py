from fastapi import FastAPI,Query,Path,Body,Cookie , Header, Request,status,Form,File,UploadFile, HTTPException

from enum import Enum
from uuid import UUID
from typing import Optional,Literal,Union 
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,HttpUrl,EmailStr
from datetime import datetime, time, timedelta

app = FastAPI()

'''
Part 1-6 
'''

# @app.get("/", description= "This is our first route")
# async def root():
#     return {"message" : "Hello world"}


# @app.post("/", description= "this is our post route")
# async def post():
#     return {"message" : "hello from the post route"}

# @app.put("/")
# async def put():
#     return {"message" : "hello from the put route"}


# @app.get("/users")
# async def list_users():
#     return {"message" : "list users route"}


# @app.get("/users/{user_id}")
# async def get_users(user_id : str ):
#     return {"user_id" : user_id}

# @app.get("/users/me")
# async def get_current_user():
#     return {"message" : "This is the current user"}


# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dairy"     # class variables

# @app.get("/foods/{food_name}")
# async def get_food(food_name : FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {"food_name" : food_name, "message": "you are healthy"}
    
#     if food_name.value == 'fruits':
#         return  {
#             "food_name" : food_name,
#             "message" : " Wow you are eating fruits cool."
#         }
#     return {
#         "food_name" : food_name ,
#         "message" : "Nice food"
#     }



# fake_item_db = [{"item_name" : "Foo"} , {"item_name" : "Bar"} , {"item_name" : "Baz"} ]


# @app.get("/items")
# async def list_tems(skip: int = 0, limit : int = 10):
#     return fake_item_db[skip : skip + limit]

# @app.get("/items/{item_id}")
# async def get_item(item_id: str, q: Optional[str] = None):
#     if q :
#         return {"item_id" : item_id, "q" : q}
#     return {"item_id" : item_id}

# @app.get("/items/{item_id}")
# async def get_item(item_id: str, q: str | None, short: bool = False):
#     item = {"item_id" : item_id}
#     if q :
#         item.update({"q" : q})
#     if not short:
#         item.update(
#             {
#             "description" : "Lorem ipsum"
#             }
#         )
#     return item



# class Item(BaseModel):
#     name:str
#     description : str | None = None
#     price : float
#     tax : float

# @app.post("/items")
# async def create_item(item: Item) :
#     item_dict = item.dict()
#     if item.tax : 
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax" : price_with_tax})
#     return item_dict

# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id : int, item : Item, q : str | None = None    ):
#     result = {"item_id" : item_id, **item.dict()}
#     if q :
#         result.update({"q" : q})
#     return result


# @app.get("/items")
# async def read_items(q: list[str] | None = Query(None)):
#     results = {"items" : [{ "item_id" : "Foo"} , {"item_id"   : "Bar"}  ]   }
#     if q :
#         results.update( {"q" : q})
#     return results

# @app.get("/items_hidden/hidden")
# async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema= False)    ):
#     if hidden_query : 
#         return {"hidden_query" : hidden_query}
#     return {"hidden_query" : "Not found"}


# @app.get("/items_validation/{item_id}")
# async def read_items_validation(
#     item_id : int = Path(..., title= " The ID of the item to get" , ge=10), 
#     q:str | None = Query(None, alias= "item-query")
#     ):
#     results = {"item_id" : item_id}
#     if q:
#         results.update({"q" : q})
#     return results

'''
Part 7 Body - Multiple Parameters
'''


# app =FastAPI()

# class Item(BaseModel):
#     name : str
#     description: str | None = None
#     price : float
#     tax : float | None = None

# class User(BaseModel):
#     username : str
#     full_name : str | None = None

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(..., title= " The ID of the item to get" , ge = 0 , le = 150),
#     q: str | None = None,
#     item : Item | None = None,
#     user : User | None = None,
#     number : int = Body(...)
# ):

#     results = {"item_id" : item_id}
#     if q :
#         results.update({"q" : q})
#     if item :
#         results.update({"item" : item})
#     if user :
#         results.update({"user" : user})
#     if number :
#         results.update({"number" : number})
#     return results

'''
Part 8 -> Body- Fields
'''

# app = FastAPI()

# class Item(BaseModel):
#     name : str
#     description: str | None = Field( 
#         None , description ="the description of the item", max_length = 50
#         )
#     price : float = Field(..., gt = 0, description= " The price must be greater than zero")
#     tax : float | None = None
                                    
                                    
# @app.put("/items/{item_id}")
# async def update_item(item_id : int, item : Item = Body(... , embed= True)):
#     results = {"item_id" : item_id, "item" : item}
#     return results


'''
part 9 -> Body - Nested Models 
'''

# app = FastAPI()

# class Item2(BaseModel):
#     discount_rate : int
#     inflation_rate : int
#     url : HttpUrl

# class Item(BaseModel):
#     name : str
#     description : str | None = None
#     price : float | None = None
#     tax : float | None = None
#     tags: set[str] = set()
#     item2 : Item2 | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id : int, item : Item ):
#     results = {"item_id" : item_id, "item" : item}
#     return results

'''
Part-10 Declare Request Body Example data
'''

# app = FastAPI()

# class Item(BaseModel):
#     name : str | None = None
#     description : str | None = None
#     price : float | None = None
#     tax : float | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id : int, item : Item = Body(..., example= {
#     "name" : "Item name",
#     "description" : "Item description",
#     "price" : 20,
#     "tax" : 3



# })):
#     results = {"item_id" : item_id, "item" : item}
#     return results

'''
Part 11, Extra Data Types
'''
# @app.put("/items/{item_id}")
# async def read_items(
#     item_id: UUID,
#     start_date: datetime | None = Body(None),
#     end_date: datetime | None = Body(None),
#     repeat_at: time | None = Body(None),
#     process_after: timedelta | None = Body(None),
# ):
#     start_process = start_date + process_after
#     duration = end_date - start_process
#     return {
#         "item_id": item_id,
#         "start_date": start_date,
#         "end_date": end_date,
#         "repeat_at": repeat_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration,
#     }

'''
Part 12 Cookie and header parameter
'''
# @app.get("/items")
# async def read_items(
#     cookie_id: str | None = Cookie(None),
#     accept_encoding: str | None = Header(None),
#     sec_ch_ua: str | None = Header(None),
#     user_agent: str | None = Header(None),
#     x_token: list[str] | None = Header(None),
# ):
#     return {
#         "cookie_id": cookie_id,
#         "Accept-Encoding": accept_encoding,
#         "sec-ch-ua": sec_ch_ua,
#         "User-Agent": user_agent,
#         "X-Token values": x_token,
#     }


'''
Part 13 Response Model
'''

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float = 10.5
#     tags: list[str] = []
 

# @app.post("/items/", response_model=Item)
# async def create_item(item: Item):
#     return item


# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None


# class UserIn(UserBase):
#     password: str


# class UserOut(UserBase):
#     pass


# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user


'''
Part 14 : Extra Models
'''
 
# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None

# class UserIn(UserBase):
#     password: str
    
# class UserOut(UserBase):
#     pass

# class UserInDB(UserBase):
#     hashed_password: str

# def fake_password_hasher(raw_password: str):
#     return f"supersecret{raw_password}"

# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password) # **user_in.dict() will extract the key value pairs and pass them to UserInDB
#     print("User 'saved'.")
#     return user_in_db

# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved


# class BaseItem(BaseModel):
#     description: str
#     type: str


# class CarItem(BaseItem):
#     type = "car"


# class PlaneItem(BaseItem):
#     type = "plane"
#     size: int


# items = {
#     "item1": {"description": "this is a car", "type": "car"},
#     "item2": {
#         "description": "this is an aeroplane",
#         "type": "plane",
#         "size": 5,
#     },
# }


# @app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
# async def read_item(item_id: Literal["item1", "item2"]):
#     return items[item_id]


# class ListItem(BaseModel):
#     name: str
#     description: str


# list_items = [
#     {"name": "Foo", "description": "There comes my hero"},
#     {"name": "Red", "description": "It's my aeroplane"},
# ]


# @app.get("/list_items/", response_model=list[ListItem])
# async def read_items():
#     return items


# @app.get("/arbitrary", response_model=dict[str, float])
# async def get_arbitrary():
#     return {"foo": 1, "bar": "2"}

'''
Part 15 - Response Status Codes
'''
 
# @app.post("/items/", status_code= status.HTTP_201_CREATED)
# async def create_item(name: str):
#     return {"name": name}


# @app.delete("/items/{pk}", status_code= status.HTTP_204_NO_CONTENT)
# async def delete_item(pk: str):
#     print("pk", pk)
#     return pk


# @app.get("/items/", status_code= status.HTTP_302_FOUND)
# async def read_items_redirect():
#     return {"hello": "world"}


'''
part 16 - Form Fields
'''

# @app.post("/login/")
# async def login(username : str = Form(...), password : str = Form(...)):
#     print("password", password)
#     return {"username" : username}

# class User(BaseModel):
#     username : str
#     password : str

# @app.post("/login-json/")
# async def login_json(user : User):
#     return user


'''
Part 17 - Request files
'''

# @app.post("/files/")
# async def create_file(file : bytes = File(...)):
#     return{"file" : len(file)}

# @app.post("/uploadfile/")
# async def create_upload_file(
#     files : list[UploadFile] = File(..., description= " multiple files")
#     ):
#     return {"filename" : [file.filename for file in files]}

'''
Part 18- Request files and forms
'''

# @app.post("/files/")
# async def create_file(
#     file: bytes = File(...),
#     fileb: UploadFile = File(...),
#     token: str = Form(...),
#     hello: str = Body(...),
# ):
#     return {
#         "file_size": len(file),
#         "token": token,
#         "fileb_content_type": fileb.content_type,
#         "hello": hello,
#     }


'''
Part 19 - 
'''

# items = {
#     "A" : "B",
#     "C" : "D"
# }

# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Item not found")
    


# class exceptionClass(Exception):
#     def __init__(self, name: str):
#         self.name = name


# @app.exception_handler(exceptionClass)
# async def exceptionClass_handler(request: Request, exc: exceptionClass):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.name} occured"},
#     )

# @app.get("/error_checker/{name}")
# async def read_name(name : str):
#     if name == "wrong" :
#         raise exceptionClass(name = name)
#     return {"name" : name}


'''
Part 20 Path Configuration 

'''
 
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()


# @app.post("/items/", response_model=Item, tags=["Category 1"] )
# async def create_item(item: Item):
#     return item


# @app.get("/items/", response_model=Item, tags=["Category 1"] )
# async def create_item(item: Item):
#     return item

# @app.put("/items/", response_model=Item, tags=["Category 2"] )
# async def update_item(item: Item):
#     return item