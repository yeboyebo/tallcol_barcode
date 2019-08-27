
# @class_declaration tallcol_barcode #
from models.flfacturac import flfacturac_def
class tallcol_barcode(flfacturac):

    def tallcol_barcode_lineasTallaColor(self, model, oParam):
        response = {}
        if "referencia" in oParam and "campopadre" not in oParam:
            referencia = qsatype.FLUtil.sqlSelect(u"articulos", u"referencia", ustr(u"referencia = '", oParam['referencia'], u"'"))
            if referencia is None or referencia == u'':
                response["status"] = 1
                response["msg"] = "La referencia no existe"
                return response
            else:
                q = qsatype.FLSqlQuery()
                q.setTablesList(u"atributosarticulos")
                q.setSelect(u"atributosarticulos.barcode,atributosarticulos.talla,atributosarticulos.color, lineaspresupuestoscli.cantidad")
                q.setFrom(u"atributosarticulos inner join tallas on atributosarticulos.talla = tallas.codtalla left outer join lineaspresupuestoscli on atributosarticulos.barcode = lineaspresupuestoscli.barcode and lineaspresupuestoscli.idpresupuesto = " + str(model.pk))
                q.setWhere(u"atributosarticulos.referencia = '" + referencia + "' order by tallas.orden ASC")
                # q.setWhere(u"(UPPER(referencia) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(descripcion) LIKE '%" + oParam['val'].upper() + "%')")
                if not q.exec_():
                    response["status"] = 1
                    response["msg"] = "La referencia no tiene tallas asignadas"
                    return response
                if q.size() == 0:
                    response["status"] = 1
                    response["msg"] = "La referencia no tiene tallas asignadas"
                    return response
                response['status'] = -1
                response['data'] = {"referencia": oParam["referencia"]}
                response['params'] = []
                while q.next():
                    cantidad = 0
                    if q.value("lineaspresupuestoscli.cantidad") != None:
                        cantidad = q.value("lineaspresupuestoscli.cantidad")
                    response['params'].append({
                        "tipo": 16,
                        "required": True,
                        "verbose_name": q.value("atributosarticulos.talla") + " - " + q.value("atributosarticulos.color"),
                        "key": q.value("atributosarticulos.barcode"),
                        "value": cantidad,
                        "validaciones": None
                    })
                response['params'].append({
                        "tipo": 56,
                        "required": True,
                        "verbose_name": "Campo padre",
                        "key": "campopadre",
                        "value": "idpresupuesto",
                        "visible": False,
                        "validaciones": None
                    })
                response['params'].append({
                        "tipo": 56,
                        "required": True,
                        "verbose_name": "Tabla",
                        "key": "tabla",
                        "value": "lineaspresupuestoscli",
                        "visible": False,
                        "validaciones": None
                    })
                response['params'].append({
                        "tipo": 56,
                        "required": True,
                        "verbose_name": "Referencia",
                        "key": "referencia",
                        "visible": False,
                        "validaciones": None
                    })
                return response
        else:
            if not flfacturac_def.iface.creaLineasTallaColor(model.pk, oParam):
                return False
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def lineasTallaColor(self, model, oParam):
        return self.ctx.tallcol_barcode_lineasTallaColor(model, oParam)

