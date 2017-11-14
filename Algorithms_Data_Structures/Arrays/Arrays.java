import java.io.*;
import java.util.*;

public class Arrays{    

   // INstantiating classes
   private int[] array; 

   // Constructors
   public Arrays(int[] arr){
       array = arr;
   }

   public Arrays(){
       array = new int[10];
   }

   //Getter and Setters

   public int[] getArray(){
       return array;
   }

   public void setArray(int[] arr){
       array = arr;
   }
}
