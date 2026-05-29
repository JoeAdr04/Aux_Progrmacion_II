/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package excepciones;

/**
 *
 * @author erenb
 */
public class SaldoInsuficienteException  extends Exception{

    public SaldoInsuficienteException(int saldo, int retiro) {
        super(retiro + "es mayor que "+ saldo);
    }
    
    
}
