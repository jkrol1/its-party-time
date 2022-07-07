from flask.helpers import get_debug_flag

from app import create_app
from config import DevConfig, ProdConfig

app = create_app(DevConfig if get_debug_flag() else ProdConfig)
