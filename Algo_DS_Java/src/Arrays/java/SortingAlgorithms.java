package InterviewPrep;

import java.io.*;
import java.util.*;

public class SortingAlgorithms {


    private int[] array;
    private int sorting;

    public SortingAlgorithms(int[] a, int s){    
        array = a;
        sorting = s;
    } 

    public SortingAlgorithms(){
        array = new int[10];
        sorting = 1;
    }

    // getter and setters
    public void setArray(int[] a){
        array = a;
    }

    public void setSorting(int s){
        sorting = s;
    }

    public int[] getArray(){
        return array;
    }

    public int getSort(){
        return sorting;
    }

    // arrayPrinter
    public void printArr(int s){
        if(s == 1){
            System.out.println("This Worked");
            this.insertionSort(array);
        } else if(s == 2){
            System.out.println("MergeSort call worked");
            this.mergeSort(array);
        } else if(s == 3){
            System.out.println("QuickSort call worked");
            this.quickSort(array, 0, array.length - 1);
        }
        for( int i = 0; i < array.length; i++)
        {
            System.out.print(array[i] + ",");
        }
        System.out.println("\n");
    }

    public int[] insertionSort(int[] arr){        
       int value, hole;
       for( int i = 1; i < arr.length; i++){ 
           value = arr[i];
           hole = i - 1; 
           while ((hole > -1) && (arr[hole]>value)){ 
               arr[hole + 1] = arr[hole];
               hole--;
           }
           arr[hole+1] = value;
       }
      return arr; 
    }

    public void mergeSort(int[] arr){
        // base case
        int n = arr.length;
        System.out.println("arr length " + n);
        if (n < 2){
            return;
        }
        
        // Time to split the arrays into two        
        int mid = n/2;
        int[] l = new int[mid];
        int[] r = new int[(n-mid)];
        for( int i = 0; i < mid; i++){
            l[i] = arr[i];
            System.out.print(l[i]);
        }
        System.out.println(" Left List");

        for( int j = 0; j < (n - mid); j++){
            r[j] = arr[mid + j];
            System.out.print(r[j]);
        }
        System.out.println(" Right List");
        
        // Now recurse till n < 2
//        System.out.println("this is the left list");
//        for(int w = 0; w < l.length; w++){
//            System.out.println(l[w]);
//        }
        mergeSort(l);
//        System.out.println("this is the right list");
//        for(int w = 0; w < r.length; w++){
//            System.out.println(r[w]);
//        }
        mergeSort(r);
        merge(l, r, arr);

    }
    
    public void merge(int[] l, int[] r, int[] a){
        // This first 6 lines creates variables to change
        int nL = l.length; 
        int nR = r.length;
        int i, j, k;
        i = 0; // this markes the smallest arr value in l
        j = 0; // this markes the esmallest arr value in r
        k = 0; // this markes the current place in A to fill 
                
        // this first while loops compares te first value
        // int l and r and fills smallest one
        while( i < nL && j < nR){ 
            // Compare l[i] to r[j]
            if(l[i] <= r[j]){
                System.out.println("this is Element " + l[i]);
                a[k] = l[i];
                i++;
                k++;
            } else if( r[j] < l[i]){
                System.out.println("this is Element " + r[j]);
                a[k] = r[j];
                j++;
                k++;
            }
        }
        // If there's just elements in l left
        while( i < nL){
            System.out.println("this is Element i " + l[i]);
            a[k] = l[i];
            i++;
            k++;
        }
        // If there's just elements in r left

        while( j < nR){
            System.out.println("this is Element j " + r[j]);           
            a[k] = r[j];
            j++;
            k++;
        }
 
    }

    public void quickSort(int[] arr, int start, int end){
        // base case
        if( start < end) {
            int pIndex;
            pIndex = partition(arr, start, end);
            quickSort(arr, start, pIndex - 1);
            quickSort(arr, pIndex + 1, end);
        }
    }
    
    public int partition(int [] arr, int start, int end){
        int pIndex, pivot;
        pIndex = start;
        System.out.println(end);
        pivot = arr[end];
        for( int i = start; i < end; i++){
           if( arr[i] <= pivot ){
               int temp = arr[i]; 
               arr[i] = arr[pIndex];
               arr[pIndex] = temp;
               pIndex++;
           } 
        }
        int temp = arr[end];
        arr[end] = arr[pIndex];
        arr[pIndex] = temp;
        System.out.println(pIndex);
        return pIndex;
    }

    public static void main(String args[])
    { 
       int rr[] = {3,5,2,1,8,7,4,6,9,2,0};
       SortingAlgorithms arr = new SortingAlgorithms(rr,3);   
       arr.printArr(3);
       int[] nArr = arr.getArray();
       for(int i = 0; i < nArr.length; i++){
           System.out.println(nArr[i]);
       }
    } 
}






