
from rpc import RpcRouter
class Router(RpcRouter):
    
    def __init__(self):
        self.url = 'team:router'
        self.enable_buffer = 100
        self.max_retries = 1
        self.actions = {}        
# ....
router = Router()

# Team
from .actions import TeamActions
router.actions['TeamActions'] = TeamActions()