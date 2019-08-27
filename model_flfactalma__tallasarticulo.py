# @class_declaration interna_tallasarticulo #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_tallasarticulo(modelos.mtd_tallasarticulo, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tallcol_barcode_tallasarticulo #
class tallcol_barcode_tallasarticulo(interna_tallasarticulo, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tallasarticulo #
class tallasarticulo(tallcol_barcode_tallasarticulo, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.tallasarticulo_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
