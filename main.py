from servicioImprime import ServicioImprime
from servicioEnvio import ServicioEnvio
from servicioPDF import ServicioPDF


if __name__ == "__main__":
    servi1 = ServicioEnvio()
    servi2 = ServicioPDF()

    miServi = ServicioImprime(servi1, servi2)
    miServi.imprimir()
