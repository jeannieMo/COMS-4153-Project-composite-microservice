from app.services.service_factory import ServiceFactory
from fastapi.responses import JSONResponse
class UserService:
    def __init__(self) -> None:
        service = ServiceFactory()
        self.compo_resource = service.get_service("CompositeResource")
    
    def get_user(self, user_id:str, google_user:dict):
            print("calling the function ")
            return self.compo_resource.get_user(user_id, google_user)
    
    def get_all_users(self, params:dict):
        return self.compo_resource.get_all_users(params)

    def post_user(self, user_id: str, token:str):
        print("starting he request")
        return self.compo_resource.post_user(user_id, token)

    def delete_user(self, user_id: str, google_user:dict):
        return self.compo_resource.delete_user(user_id, google_user)