# cocinero.py
# Clase que simula a un cocinero que prepara pedidos

class Cocinero:
    def preparar_pedido(self, pedido):
        """
        Prepara un pedido recibido y devuelve su versión lista.
        :param pedido: Pedido generado por el cliente
        :return: Pedido marcado como listo
        """
        print(f"[Cocinero] Prepara: {pedido}")
        listo = f"{pedido} (listo)"
        return listo
