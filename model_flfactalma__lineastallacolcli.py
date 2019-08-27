# @class_declaration interna_lineastallacolcli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_lineastallacolcli(modelos.mtd_lineastallacolcli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tallcol_barcode_lineastallacolcli #
class tallcol_barcode_lineastallacolcli(interna_lineastallacolcli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineastallacolcli #
class lineastallacolcli(tallcol_barcode_lineastallacolcli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.lineastallacolcli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
