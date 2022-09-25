from pydantic import BaseModel

class Todo (BaseModel):
    id : int
    item : str


    # class config:
    #     Schema_extra = {
    #         "Example":{
    #             "id":1,
    #             "item": "Example schema!"
    #         }
    #     }