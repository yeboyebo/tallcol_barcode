
# @class_declaration tallcol_barcode_presupuestoscli #
class tallcol_barcode_presupuestoscli(flfacturac_presupuestoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    @helpers.decoradores.accion(aqparam=["oParam"])
    def lineasTallaColor(self, oParam):
        return form.iface.lineasTallaColor(self, oParam)

