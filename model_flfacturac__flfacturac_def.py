
# @class_declaration tallcol_barcode #
class tallcol_barcode(flfacturac):

    def tallcol_barcode_creaLineasTallaColor(self, pk, oParam):
        response = {}
        datos = ""
        sumCantidad = 0
        pvp = 0
        iva = 0.0
        recargo = 0.0
        descripcion = ""
        referencia = oParam['referencia']
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"atributosarticulos")
        q.setSelect(u"atributosarticulos.barcode,atributosarticulos.talla,atributosarticulos.color,articulos.pvp,articulos.descripcion,articulos.codimpuesto,impuestos.iva,impuestos.recargo")
        q.setFrom(u"atributosarticulos inner join articulos on atributosarticulos.referencia = articulos.referencia inner join impuestos on articulos.codimpuesto = impuestos.codimpuesto")
        q.setWhere(u"atributosarticulos.referencia = '" + referencia + "'")

        if not q.exec_():
            response["status"] = 1
            response["msg"] = "La referencia no tiene tallas asignadas"
            return response

        if not qsatype.FLUtil.sqlDelete(u"lineastallacolcli", ustr(u"tabla = '", oParam['tabla'], u"' AND campopadre = '", oParam['campopadre'], u"' AND valorcampopadre = '", pk, u"'")):
            return False

        while q.next():
            if q.value("barcode") in oParam and oParam[q.value("barcode")] != None and oParam[q.value("barcode")] != 0 and oParam[q.value("barcode")] != '0':
                datos = datos + q.value("atributosarticulos.barcode") + u"," + q.value("atributosarticulos.talla") + u"," + q.value("atributosarticulos.color") + u"," + str(oParam[q.value("barcode")]) + u"," + str(q.value("articulos.pvp")) + u";"
                sumCantidad += int(oParam[q.value("barcode")])
                pvp = q.value("articulos.pvp")
                descripcion = q.value("articulos.descripcion")
                iva = q.value("impuestos.iva")
                recargo = q.value("impuestos.recargo")

        datos = datos[:len(datos) - 1]
        curLineasTC = qsatype.FLSqlCursor(u"lineastallacolcli")
        curLineasTC.setModeAccess(curLineasTC.Insert)
        curLineasTC.refreshBuffer()

        curLineasTC.setValueBuffer("usuario", qsatype.FLUtil.nameUser())
        curLineasTC.setValueBuffer("tabla", oParam['tabla'])
        curLineasTC.setValueBuffer("campopadre", oParam['campopadre'])
        curLineasTC.setValueBuffer("valorcampopadre", pk)
        curLineasTC.setValueBuffer("descripcion", descripcion)
        curLineasTC.setValueBuffer("referencia", referencia)
        curLineasTC.setValueBuffer("cantidad", sumCantidad)
        curLineasTC.setValueBuffer("pvpunitario", pvp)
        curLineasTC.setValueBuffer("iva", iva)
        curLineasTC.setValueBuffer("recargo", recargo)
        curLineasTC.setValueBuffer("datos", datos)

        if not curLineasTC.commitBuffer():
            return False

        idBuffer = curLineasTC.valueBuffer(u"id")
        curLineasTC.select(ustr(u"id = ", idBuffer))

        if not curLineasTC.first():
            return False

        curLineasTC.setModeAccess(curLineasTC.Browse)
        curLineasTC.refreshBuffer()
        qsatype.FactoriaModulos.get('formRecordalbaranescli').iface.generarLineasTC(curLineasTC)
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def creaLineasTallaColor(self, pk, oParam):
        return self.ctx.tallcol_barcode_creaLineasTallaColor(pk, oParam)

