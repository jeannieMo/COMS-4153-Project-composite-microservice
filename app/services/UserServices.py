from app.services.service_factory import ServiceFactory
from fastapi.responses import JSONResponse
from fastapi import HTTPException
class UserService:
    def __init__(self) -> None:
        service = ServiceFactory()
        self.compo_resource = service.get_service("CompositeResource")
    
    def get_user(self, user_id:str, google_user:dict):
            print("calling the function ")
            data, status = self.compo_resource.get_user(user_id, google_user)
            if status == 200:
                return data
            else:
                raise HTTPException(status_code=status, detail=data)

    def get_all_users(self, google_user:dict):
        data, status = self.compo_resource.get_all_users(google_user)
        if status == 200:
             return data
        else:
            raise HTTPException(status_code=status, detail=data)

    def post_user(self, user_id: str, token:str):
        print("starting he request")
        data, status = self.compo_resource.post_user(user_id, token)
        if status == 200 or status == 201:
            return data
        else:
            raise HTTPException(status_code=status, detail=data)

    def delete_user(self, user_id: str, google_user:dict):
        data, status = self.compo_resource.delete_user(user_id, google_user)
        if status == 200 or status == 201:
            return data
        else:
            raise HTTPException(status_code=status, detail=data)