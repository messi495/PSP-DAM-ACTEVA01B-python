# gestor_restaurante.py
# Clase principal que coordina Cliente -> Cocinero -> Repartidor

from Cliente import Cliente
from Cocinero import Cocinero
from Repartidor import Repartidor

class GestorRestaurante:
    def __init__(self):
        self.cliente = Cliente()
        self.cocinero = Cocinero()
        self.repartidor = Repartidor()

    def iniciar(self, num_pedidos):
        """
        Inicia la simulación del restaurante.
        :param num_pedidos: Número de pedidos a procesar
        """
        print("[Gestor] Simulación iniciada.")

        for i in range(1, num_pedidos + 1):
            # 1) Cliente genera pedido
            pedido = self.cliente.generar_pedido(i)

            # 2) Cocinero lo prepara
            listo = self.cocinero.preparar_pedido(pedido)

            # 3) Repartidor lo entrega
            self.repartidor.entregar_pedido(listo)

        print("[Gestor] El restaurante ha cerrado.")


if __name__ == "__main__":
    gestor = GestorRestaurante()
    gestor.iniciar(5)  # Cambia el número si quieres más o menos pedidos
