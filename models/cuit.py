# -*- coding: utf-8 -*-

class IS_CUIT(object):
    def __init__(self, error_message='debe ser un CUIT válido en formato XX-YYYYYYYY-Z'):
        self.error_message = error_message
    def __call__(self, value):
        # validaciones mínimas
        if len(value) == 13 and value[2] == "-" and value[11] == "-":
            base = [5,4,3,2,7,6,5,4,3,2]
            cuit = value.replace("-","") # remuevo las barras
            # calculo el dígito verificador:
            aux = 0
            for i in xrange(10):
                aux += int(cuit[i])*base[i]
            aux = 11-(aux-(int(aux / 11)*11))
            if aux==11:
                aux = 0
            if aux==10:
                aux = 9
            if aux == int(cuit[10]):
                return (value, None)
        return (value, self.error_message)
    def formatter(self, value):
        return value
