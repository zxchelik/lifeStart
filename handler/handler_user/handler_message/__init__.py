from .menu_message import router as r1
from .digest import router as r2
from .sections import router as r3
from .faq import router as r4
from .call_menu_test import router as r5
from .other import router as r6
from ..handler_callback.menu_callback import router as r7
from  ..handler_callback.test import router as r8

routers = [r1, r2, r3, r4, r5, r6, r7,r8]
