
from rpc.base import RpcRouter
class Router(RpcRouter):
    
    def __init__(self):
        self.url = 'dashboard:router'
        self.enable_buffer = 100
        self.max_retries = 1
        self.actions = {}        
# ....
router = Router()

# Team
from team.actions import TeamActions
router.actions['TeamActions'] = TeamActions()