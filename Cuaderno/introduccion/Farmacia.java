package Cuaderno.introduccion;

import java.util.*;

public class Farmacia {

    static ArrayList<Map<String, Object>> clientes = new ArrayList<>();
    static ArrayList<Map<String, Object>> productos = new ArrayList<>();
    static ArrayList<Map<String, Object>> ventas = new ArrayList<>();
    static Scanner sc = new Scanner(System.in);

    static void registrarCliente() {
        System.out.print("ID Cliente: ");
        String id = sc.nextLine();
        System.out.print("Nombre: ");
        String nombre = sc.nextLine();

        Map<String, Object> cliente = new HashMap<>();
        cliente.put("id", id);
        cliente.put("nombre", nombre);
        clientes.add(cliente);
    }

    static void registrarProducto() {
        System.out.print("ID Producto: ");
        String id = sc.nextLine();
        System.out.print("Nombre: ");
        String nombre = sc.nextLine();
        System.out.print("Precio: ");
        double precio = Double.parseDouble(sc.nextLine());
        System.out.print("Stock: ");
        int stock = Integer.parseInt(sc.nextLine());

        Map<String, Object> producto = new HashMap<>();
        producto.put("id", id);
        producto.put("nombre", nombre);
        producto.put("precio", precio);
        producto.put("stock", stock);
        productos.add(producto);
    }

    static Map<String, Object> buscarCliente(String id) {
        for (Map<String, Object> c : clientes) {
            if (c.get("id").equals(id)) return c;
        }
        return null;
    }

    static Map<String, Object> buscarProducto(String id) {
        for (Map<String, Object> p : productos) {
            if (p.get("id").equals(id)) return p;
        }
        return null;
    }

    static void realizarVenta() {
        System.out.print("ID Cliente: ");
        String cid = sc.nextLine();
        Map<String, Object> cliente = buscarCliente(cid);

        if (cliente == null) {
            System.out.println("Cliente no existe");
            return;
        }

        System.out.print("ID Producto: ");
        String pid = sc.nextLine();
        Map<String, Object> producto = buscarProducto(pid);

        if (producto == null || (int) producto.get("stock") <= 0) {
            System.out.println("Producto no disponible");
            return;
        }

        System.out.print("Cantidad: ");
        int cantidad = Integer.parseInt(sc.nextLine());

        int stock = (int) producto.get("stock");

        if (cantidad > stock) {
            System.out.println("Stock insuficiente");
            return;
        }

        double precio = (double) producto.get("precio");
        double total = cantidad * precio;

        producto.put("stock", stock - cantidad);

        Map<String, Object> venta = new HashMap<>();
        venta.put("cliente", cliente.get("nombre"));
        venta.put("producto", producto.get("nombre"));
        venta.put("cantidad", cantidad);
        venta.put("total", total);

        ventas.add(venta);

        System.out.println("Venta realizada. Total: " + total);
    }

    static void mostrarVentas() {
        for (Map<String, Object> v : ventas) {
            System.out.println(v);
        }
    }

    public static void main(String[] args) {
        while (true) {
            System.out.println("\n1. Registrar cliente");
            System.out.println("2. Registrar producto");
            System.out.println("3. Realizar venta");
            System.out.println("4. Mostrar ventas");
            System.out.println("0. Salir");

            String op = sc.nextLine();

            switch (op) {
                case "1": registrarCliente(); break;
                case "2": registrarProducto(); break;
                case "3": realizarVenta(); break;
                case "4": mostrarVentas(); break;
                case "0": return;
            }
        }
    }
}