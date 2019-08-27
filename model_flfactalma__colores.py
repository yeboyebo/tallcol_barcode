# @class_declaration interna_colores #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_colores(modelos.mtd_colores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tallcol_barcode_colores #
class tallcol_barcode_colores(interna_colores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration colores #
class colores(tallcol_barcode_colores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.colores_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
