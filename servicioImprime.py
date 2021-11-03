class ServicioImprime:
    def __init__(self, serv1={}, serv2={}):
        self._servicioA = serv1
        self._servicioB = serv2
    
    @property
    def servicioA(self):
        return self._servicioA

    @servicioA.setter
    def setServicioA(self,servicioA):
        self._servicioA=servicioA

    @property
    def servicioB(self):
        return self._servicioB

    @servicioB.setter
    def setServicioB(self,servicioB):
        self._servicioB=servicioB

    def imprimir(self):
        self.servicioA.enviar()
        self.servicioB.pdf()
