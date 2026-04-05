/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencia01;
/**
 *
 * @author erenb
 */
public class Estudiante extends Persona{
   
    private int matricula;
    private float nota;

    public Estudiante(String nombre, int edad, int carnet, int matricula, float nota ) {
        super(nombre, edad, carnet);
        this.matricula = matricula;
        this.nota = nota;
    }
    public Estudiante(){
        super(); //llamada a la clase padre
    }

    @Override
    public String toString() {
        return super.toString()+"Estudiante{" + "matricula=" + matricula + ", nota=" + nota + '}' ;
    }
    
    
}
