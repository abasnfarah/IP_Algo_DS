//package InterviewPrep;

import java.io.*;
import java.util.*;

public class ArrayStack{

    //Local variables
    private int arrStack[];
    private int top = -1;
    private int size = 0;


    //Constructors
    public ArrayStack(int data){
        arrStack = new int[5];
        this.push(data);
    }

    public ArrayStack(){
        arrStack = new int[5];
    }


    //Return array stack
    public int[] getStack(){
        return arrStack;
    }

    public int getSize(){
        return size;
    }

    //stack print
    public void printStack(){    

        for( int i = top; i >= 0; i--){
            System.out.println( "|| " + arrStack[i] + " ||");
        }

    } 

    //Methods
    
    //Overflow control
    public int[] overFlow(int[] oldArr){
        
        int l = oldArr.length;
        int n = l*2;

        int newArr[] = new int[n];
        
        // now to fill new array
        for(int i = 0; i < l; i++){
            newArr[i] = oldArr[i];
        }

        return newArr;
    }

    //Push
    public boolean push(int data){
        
        top++;
        size++;

        if(top >= arrStack.length){
            arrStack = overFlow(arrStack);

            arrStack[top] = data;

            return true; 

        } else{
            
            arrStack[top] = data;

            return true;

        }

    }

    //Pop
    public int pop(){
        
        if(size == 0){

            throw new IndexOutOfBoundsException();

        } else{

            int var = arrStack[top]; 
            top--;
            size--;
            return var;

        }

    } 

    //top
    public int top(){
        
        if(size == 0){

            throw new IndexOutOfBoundsException();

        } else {

            return arrStack[top];

        }

    }

    //Main
    public static void main(String args[]){

        ArrayStack s = new ArrayStack();
        s.push(1);
        s.push(2);
        s.push(3);
        s.push(4);
        s.printStack();
        System.out.println();         
    }



}







