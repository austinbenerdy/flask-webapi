from dependency_injector import containers, providers

# Import Controllers
from controller.userController import UserController

# Import Services
from service.userService import UserService


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    """
    Here are design the factories that will build the objects
    to be used in dependency injection. 
    
    Unknown: If order matters here. I have the Controller below
    the Service that it depends on but I haven't tested the alternative
    """
    user_service = providers.Singleton(
        UserService
    )

    user_controller = providers.Singleton(
        UserController,
        user_service
    )

