# PSP-DAM-ACTEVA01B-python
Este proyecto es una simulación sencilla de un flujo de pedidos en un restaurante usando Programación Orientada a Objetos en Python.​

## Descripción del proyecto
El sistema modela a tres actores principales de un restaurante (cliente, cocinero y repartidor) y una clase gestora que coordina todo el proceso de un pedido. Cada pedido se genera, se prepara y finalmente se entrega, mostrando por pantalla # cada paso del flujo.​

## Estructura de archivos
cliente.py: Contiene la clase Cliente, encargada de generar pedidos numerados como Pedido-1, Pedido-2, etc.

cocinero.py: Contiene la clase Cocinero, que recibe un pedido y lo marca como listo añadiendo el texto (listo).

 repartidor.py: Contiene la clase Repartidor, que recibe un pedido listo y simula su entrega.

 gestor_restaurante.py: Clase principal GestorRestaurante que coordina la interacción entre cliente, cocinero y repartidor y ejecuta la simulación.

 Clases y responsabilidades
## Cliente:

 Método generar_pedido(numero): crea una cadena con el identificador del pedido y la muestra por pantalla.

## Cocinero:

 Método preparar_pedido(pedido): simula la preparación del pedido y devuelve la versión marcada como lista.

## Repartidor:

Método entregar_pedido(pedido_listo): simula la entrega del pedido listo mostrando un mensaje.

## GestorRestaurante:

 Constructor: instancia un cliente, un cocinero y un repartidor.

 Método iniciar(num_pedidos): recorre del 1 a num_pedidos generando, preparando y entregando cada pedido en orden.

## Cómo ejecutar la simulación
 Asegúrate de tener todos los archivos (cliente.py, cocinero.py, repartidor.py, gestor_restaurante.py) en el mismo directorio.​

 Desde la terminal, ejecuta:

 bash
 python gestor_restaurante.py
 Por defecto se ejecuta gestor.iniciar(5), que procesa 5 pedidos consecutivos; puedes cambiar ese número en el bloque if __name__ == "__main__": para simular más o menos pedidos.
