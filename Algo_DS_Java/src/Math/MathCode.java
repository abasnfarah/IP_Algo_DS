package InterviewPrep;

import java.io.*;
import java.util.*;

public class MathCode {


    // Global variables
    public int var;


    // Constructors 
    public MathCode(){

        var = 0;

    }    

    public MathCode(int imput){

        var = imput;

    }


    //Getter and Setters
    public int getVar(){

        return var;

    }

    public void setVar(int newVar){
        var = newVar;
    }


    // Returns all factors for a given N
    public int[] allFactors(int N){
        
        // arr keeps track of all N % i  == 0 factors
        // err keeps track of all n/i factors 
        // array keeps track of all arr err pairs 
        ArrayList arr = new ArrayList();
        ArrayList err = new ArrayList();
        int[] array; 

        // have to typeCast Math.sqrt(N) becasue it returns a Double data type
        // We need an Int to compare i to in java
        for(int i = 1;(int) i < Math.sqrt(N); i++){
            
            if (N % i == 0){

                arr.add(i);

                if( (double) i != Math.sqrt(N)){ 

                    err.add(N/i);

                }

            }

        }

       // now we have to merge the two arrays to have a sorted list of Factors 
       for(int i = err.size() - 1; i >= 0; i--){
           arr.add(err.get(i));
       }

       // now to convert ArrayList into int[] Array to return;

       array = new int[arr.size()];

       for(int i = 0; i < arr.size(); i++){
            array[i] = (int) arr.get(i);
       }

       return array;

    
    }

    public boolean isPrime(int N){

        ArrayList arr = new ArrayList();

        // if N <= 1 then N is not prime
        if( N <= 1){
            return false;
        }

        // This loops from 2 till sqrt(N) to check if N is divisable by I
        // If divisable N is not a prime number
        for(int i = 2; i < (int) Math.sqrt(N); i++){
            
            if( N % i == 0){ // N is divisable by i

                return false;

            }

        }
        
        // If N is only divisable by 1 and N then N is prime
        return true;

    }

    // This takes a integer and returns an array of all primes less then N
    public int[] sieve(int N){
        
        ArrayList arr = new ArrayList(N + 1);
        ArrayList err = new ArrayList();
        int[] array;

        for(int i = 0; i < N + 1; i++){
            arr.add(1);
        }

        arr.set(0, 0);
        arr.set(1, 0);

        for(int i = 2; i <= Math.sqrt(N); i++){

            if( (int) arr.get(i) == 1){
                for(int j = 2; j*i <= N; j++){
                    arr.set(j*i, 0);
                }
            }
        } 

        for(int i = 0; i < arr.size(); i++){
            if( (int) arr.get(i) == 1){
                err.add(i);
            }
        }

        array = new int[err.size()];

        for(int i = 0; i < err.size(); i++){
            array[i] = (int) err.get(i);
        }

        return array;
    }


    public static void main(String[] args){
        
        MathCode swag = new MathCode();
        Scanner input = new Scanner(System.in);
        Scanner newInput = new Scanner(System.in);

        int[] arr;
        int prime;
        int sieve;

        arr = swag.allFactors(200);
        
        for(int i = 0; i < arr.length; i++){
            System.out.print(" |" + arr[i] + "| ");
            System.out.println();
        }

        System.out.print("Enter input to check if prime: ");
        prime = input.nextInt();
        System.out.println("isPrime: " + swag.isPrime(prime));

        System.out.print("Enter a number and I'll give you all primes less then the number you give me: ");
        sieve = input.nextInt();
        input.close();
        arr = swag.sieve(sieve);
        for(int i = 0; i < arr.length; i++){
            System.out.print(" |" + arr[i] + "| ");
            System.out.println();
        }
    } 
         
}






