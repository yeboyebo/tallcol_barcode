
# @class_declaration tallcol_barcode_albaranescli #
class tallcol_barcode_albaranescli(flfacturac_albaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    @helpers.decoradores.accion(aqparam=["oParam"])
    def lineasTallaColor(self, oParam):
        return form.iface.lineasTallaColor(self, oParam)

