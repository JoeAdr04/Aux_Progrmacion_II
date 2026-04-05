/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencia01;

/**
 *
 * @author erenb
 */
public class Persona {
    protected String nombre; // accede la clase padre y la clase hija o subclases
    protected int edad;
    protected int carnet;

    public Persona(String nombre, int edad, int carnet) {
        this.nombre = nombre;
        this.edad = edad;
        this.carnet = carnet;
    }

    public Persona() {
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", edad=" + edad + ", carnet=" + carnet + '}';
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    public int getCarnet() {
        return carnet;
    }
    
    
}
