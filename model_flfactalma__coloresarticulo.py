# @class_declaration interna_coloresarticulo #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_coloresarticulo(modelos.mtd_coloresarticulo, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tallcol_barcode_coloresarticulo #
class tallcol_barcode_coloresarticulo(interna_coloresarticulo, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration coloresarticulo #
class coloresarticulo(tallcol_barcode_coloresarticulo, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.coloresarticulo_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
