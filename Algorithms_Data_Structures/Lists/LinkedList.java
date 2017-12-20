package InterviewPrep;

import java.io.*;
import java.util.*;

public class LinkedList<E> {
    
    // Making Node class for List
    public class Node<E> { 

        // Global Variables
        public E data; 
        public Node<E> next;

        // Constructors
        public Node(){
            next = null;
        }
        public Node(E newData){
            data = newData;
            next = null;
        }

        public Node(E newData, Node<E> newNext){
            data = newData;
            next = newNext;
        }


        //getter and setters
        public E getData(){
            return data;
        }

        public Node<E> getNext(){
            return next;
        }

        public void setData(E newData){
            data = newData;
        }

        public void setNext(Node<E> newNext){
            next = newNext;
        }
    }

    // Global variable
    private Node<E> head;
    private Node<E> tail;
    private int size;
    
    public LinkedList(){
        head = null;
        tail = null;
        size = 0;
    }

    public LinkedList(LinkedList<E> newList){
        head = newList.getHead();
        tail = newList.getTail();
        size = newList.size();
    }

    public LinkedList(Node<E> node){
        head = node;
        
        Node<E> pointer = node;
        Node<E> tracer = null;
        int count = 0;

        while( pointer != null){
            count++;
            tracer = pointer;
            pointer = pointer.getNext();
    }

        tail = tracer;
        size = count;
    }

    public LinkedList(E data){
        head = new Node<E>(data);
        tail = head;
        size = 1;
    }


    //getter and setters
    public Node<E> getHead(){
        return head;
    }

    public Node<E> getTail(){
        return tail;
    }

    public int size(){
        return size;
    }


    
    //Methods 
    public void printList(){
        System.out.println("Printing list ..");

        Node<E> ptr = head;
        
        while(ptr != null){
            System.out.print("| " + ptr.getData() + " | ==> ");
            ptr = ptr.getNext();
        }
        System.out.println();
    }

    public void add(E data){
        if(head == null){
            head = new Node(data);
            tail = head;
            size = 1;
        } else {

            Node<E> newNode = new Node<E>(data);
            tail.setNext(newNode);
            tail = tail.getNext();
            size++;

        }
    }

    public void add(Node<E> N){
        if(head == null){
            head = N;
            
            Node<E> ptr = N;
            Node<E> trc = null;
            int count = 0;

            while( ptr != null){
                count++;
                trc = ptr;
                ptr = ptr.getNext();
            }

            tail = trc;
            size = count;
        } else {
            tail.setNext(N);
            tail = tail.getNext();
            size++;
        }
    }

    public void insert(int index, E data){
        if(index > this.size() || index < 0){

            System.out.println("Index is out of Bounds, List has " + this.size() + " elements");

        } else { 

            Node<E> ptr = head;
            Node<E> trl = null;
            int count = index;

            while( count > 0 && ptr != null){

                count--;
                trl = ptr;
                ptr = ptr.getNext();

            }

            if(index == this.size()){

                this.add(data);
                return;

            } else if(index == 0){

                Node<E> newNode = new Node<E>(data);
                newNode.setNext(head);
                head = newNode;
                size++;
                return;

            } else {

                Node<E> newNode = new Node<E>(data);
                newNode.setNext(ptr);
                trl.setNext(newNode);
                size++;
                return;

            }
        }
    }

    public E get(int index){

        // Check if index is out of bounds
        if(index < 0 || index >= this.size()){
            System.out.println("Index is Out of Bounds");
            return null;
        } else {

            Node<E> ptr = head;
            int count = index;

            while(count > 0 && ptr != null){

                count--;
                ptr = ptr.getNext();

            } 

            E value = ptr.getData();

            return value;

        }
    }

    public boolean remove(int index){
        // Check if index is out of bounds
        if(index < 0 || index >= this.size()){

            return false;

        } else {

            Node<E> ptr = head;
            Node<E> trl = null;
            int count = index;

            while(count > 0 && ptr != null){
                count--;
                trl = ptr;
                ptr = ptr.getNext();
            }

            if(index == 0){
                head = head.getNext();
                return true;
            } else {
                trl.setNext(ptr.getNext());
                return true;
            }
            
        }

    }
    public static void main(String[] args){

        LinkedList<Integer> l = new LinkedList<Integer>(1);
        l.add(2);
        l.add(4);
        l.printList();
        l.insert(2,3);
        l.printList();
        l.insert(0,0);
        l.printList();
        System.out.println();
        System.out.println("This is the 3rd element: " + l.get(3));
        l.remove(4);
        l.printList();

    }

    

}










