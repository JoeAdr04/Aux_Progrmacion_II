
package excepciones;

import java.util.Scanner;


public class Excepciones {


    public static void main(String[] args) {
        Scanner te =  new Scanner(System.in);
        int sal;
        int ret;
        try{
            System.out.println("Ingrese su saldo: ");
            sal = te.nextInt();
            System.out.println("Cuanto va a retirar : ");
            ret = te.nextInt();
            
            if(ret > sal){
                throw new SaldoInsuficienteException(sal, ret);
                
            }
        }
        catch(SaldoInsuficienteException e){
            System.out.println("Saldo insuficiente " + e);
            System.out.println("Se retirara todo"); 
        }
        catch(Exception j){
            System.out.println("fallaste en : "+j);
        }
        finally{
            sal = 0;
            System.out.println("tu nuevo saldo es "+ sal);
        }
        
    }
    
}
