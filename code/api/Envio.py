import uuid

class Envio:
    def __init__(self,track_code,org,dst) -> None:
        self.__trackcode    = track_code
        self.__uuid         = str(uuid.uuid4())
        self.__org          = org
        self.__dst          = dst
        self.__entregado    = False
        pass

    def obtenerCodigo(self) -> str:
        return self.__trackcode
        
    def obtenerInformacion(self) -> str:
        return "Envio: {0}[{1}] -- {2} -> {3}. Entregado: {4}".format(self.__uuid,self.__trackcode,self.__org,self.__dst,self.__entregado)
    
    def obtenerDestino(self) -> str:
        return self.__dst

    def estadoEntrega(self) -> bool:
        return self.__entregado

    def envioEntregado(self):
        self.__entregado    = True

    def envioNoEntregado(self):
        self.__entregado    = False
    
    def __repr__(self) -> str:
        return "Envio: {0}[{1}] -- {2} -> {3}. Entregado: {4}".format(self.__uuid,self.__trackcode,self.__org,self.__dst,self.__entregado)