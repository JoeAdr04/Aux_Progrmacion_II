/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencia01;


public class Maestro extends Persona{
    private int horasTrabajo;
    private String materia;

    public Maestro(String nombre, int edad, int carnet, int horasTrabajo, String materia) {
        super(nombre, edad, carnet);
        this.horasTrabajo = horasTrabajo;
        this.materia = materia;
    }

    public Maestro() {
        super();
    }

    @Override
    public String toString() {
        return "Maestro{" + "nombre=" + super.nombre + ", edad=" + super.edad + ", carnet=" + super.carnet + ", horasTrabajo=" + horasTrabajo + ", materia=" + materia + '}';
    }
    
    
}
