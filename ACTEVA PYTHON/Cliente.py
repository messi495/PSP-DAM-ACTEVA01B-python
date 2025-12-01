# cliente.py
# Clase que simula a un cliente que genera pedidos

class Cliente:
    def generar_pedido(self, numero):
        """
        Genera un pedido con el número recibido.
        :param numero: Número de pedido (1, 2, 3, ...)
        :return: Cadena con el identificador del pedido
        """
        pedido = f"Pedido-{numero}"
        print(f"[Cliente] Genera: {pedido}")
        return pedido
