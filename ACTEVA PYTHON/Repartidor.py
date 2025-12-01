# repartidor.py
# Clase que simula a un repartidor que entrega pedidos

class Repartidor:
    def entregar_pedido(self, pedido_listo):
        """
        Entrega el pedido que ya está listo.
        :param pedido_listo: Pedido preparado por el cocinero
        """
        print(f"[Repartidor] Entrega: {pedido_listo}")
