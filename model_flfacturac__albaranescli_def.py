
/** @delete_class flfacturac */

# @class_declaration flfacturac #
from YBLEGACY.constantes import *


class flfacturac(interna):

    def flfacturac_getDesc(self):
        return None

    def __init__(self, context=None):
        super().__init__(context)

    def getDesc(self):
        return self.ctx.flfacturac_getDesc()

class tallcol_barcode(flfacturac):

    def tallcol_barcode_lineasTallaColor(self, model, oParam):
        print("entra")
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def lineasTallaColor(self, model, oParam):
        return self.ctx.tallcol_barcode_lineasTallaColor(model, oParam)

