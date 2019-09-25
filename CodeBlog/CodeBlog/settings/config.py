from .base import *

if os.environ['PROJECT_ENVIRONMENT'] == 'production':                          
   from .prod import * 
else:
   from .dev import *  