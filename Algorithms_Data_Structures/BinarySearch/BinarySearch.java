package InterviewPrep;

import java.io.*;
import java.util.*;

public class BinarySearch {

    // global variables 
    private int[] array;
    
    // instantiaion methods
    public BinarySearch(int[] arr){
        array = arr;
    }

    public BinarySearch(){
        array = new int[10];
    }

    // getter and setters 
    public int[] getArray(){
        return array;
    }

    // sort
    public int sort(int x){

        int value;
        value = this.BinarySearch(array, array.length, x);
        return value;

    }
    public void setArray(int[] arr){
        array = arr;
    }

    public void swag(){
	System.out.println("Hello there Buddy");
    }

    
    // BinarySearch

    public int BinarySearch(int[] arr, int n, int x){
        System.out.println(n + " " +  x);
        int start = 0;
        int end = n - 1; 
        int mid = 0;
        while(start <= end){
            System.out.println("mid: before " + mid);           
            mid = start + (end - start) / 2;  

            if( arr[mid] == x){
                System.out.println("mid: after " + mid);
                return mid;

            } else if(x < arr[mid]){

                end = mid - 1;
                
            } else if(x > arr[mid]){

                start = mid + 1;

            } 
        }
        
        return -1;
    }


    public static void main(String[] args){

        int[] arr = {1,3,5,6,8,9,16,17,22,33,45,47};
        BinarySearch sortBruv = new BinarySearch(arr);  
        int sortThing;
        sortThing = sortBruv.sort(16);
	sortBruv.Worked

        if(sortThing != -1){
            System.out.println("Found your item at index: " + sortThing);
        } else {
            System.out.println("Didn't find it; Error: " + sortThing);
        }  
    }


}
