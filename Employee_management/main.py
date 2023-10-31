
from utils.log import Log
from controller.authenticate import Authentication
import text_decoration

text_decoration.text_decorate()
log = Log()
Authentication().login()
