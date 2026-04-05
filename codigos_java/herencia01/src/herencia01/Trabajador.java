/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencia01;

/**
 *
 * @author erenb
 */
public class Trabajador extends Persona{
    private int nit;
    private String sindicato;

    public Trabajador(int nit, String sindicato, String nombre, int edad, int carnet) {
        super(nombre, edad, carnet);
        this.nit = nit;
        this.sindicato = sindicato;
    }

    public Trabajador() {
        super();
        
    }

    @Override
    public String toString() {
        return super.toString()+"Trabajador{" + "nit=" + nit + ", sindicato=" + sindicato + '}';
    }
    
    
    
}
