# Introduccion a la Programacion orientada a Objetos

Antes de la **POO** (Programacion orientada a Objetos), programar era como dar una receta de cocina interminable (Programación Estructurada): si querías cambiar un ingrediente al final, a veces tenías que *reescribir toda la receta*.

La Poo nos permitira organiza el codigo en unidades independientes.

Imagina que realizas que se te solicita crear una aplicacion para una farmcia, una que permita administrar a los clientes, productos y realizar ventas. ¿Como te lo imaginarias? con lo visto hasta ahora talves podrias pensar en algo asi como:
```mermaid
flowchart TD
    A[Inicio] --> B[Mostrar menú]
    B --> C{Opción}

    C -->|1| D[Registrar cliente]
    D --> B

    C -->|2| E[Registrar producto]
    E --> B

    C -->|3| F[Realizar venta]
    F --> G[/Ingresar ID cliente/]
    G --> H{Cliente existe?}

    H -->|No| I[Mostrar error]
    I --> B

    H -->|Sí| J[/Ingresar ID producto/]
    J --> K{Producto existe y stock > 0?}

    K -->|No| L[Mostrar error]
    L --> B

    K -->|Sí| M[Ingresar cantidad]
    M --> N{Stock suficiente?}

    N -->|No| O[Mostrar error]
    O --> B

    N -->|Sí| P[Calcular total]
    P --> Q[Actualizar stock]
    Q --> R[Guardar venta]
    R --> S[Mostrar ticket]
    S --> B

    C -->|4| T[Mostrar ventas]
    T --> B

    C -->|0| U[Fin]
```