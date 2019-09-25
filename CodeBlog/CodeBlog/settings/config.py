from .base import *

if os.environ['PROJECT_ENVIRONMENT'] == 'production':                          
   from .production import * 
else:
   from .dev import *  