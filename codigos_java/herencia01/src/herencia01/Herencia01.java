/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package herencia01;

/**
 *
 * @author erenb
 */
public class Herencia01 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Estudiante e1 = new Estudiante("joel", 123, 456, 789, 100);
        System.out.println(e1);
        Maestro m1 = new Maestro("jhon", 321, 654, 9,"programacion");
        System.out.println(m1);
        System.out.println(m1.nombre);
        Trabajador t1 = new Trabajador();
        System.out.println(t1);
        System.out.println(t1.getEdad());
        System.out.println(m1.getEdad());
        System.out.println(e1.getEdad());
        
    }
}
