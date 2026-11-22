package models;

import java.util.ArrayList;

public class Datagrp{
  public static class Data {
        public String name;
        public int age;
        public String address;
        public void setdata(String name, int age, String address) {
            this.name = name;
            this.age = age;
            this.address = address;
        }
      }
        ArrayList<Data> dataList;
        public Datagrp(){
          dataList = new ArrayList<>();
        }
        
      
    public void addElement(int index, String name, int age, String address) {
        Data newData = new Data();
        newData.setdata(name, age, address);
        dataList.add(index, newData);
    }
    
      public void sort(){
       dataList.sort((d1, d2) -> Integer.compare(d1.age, d2.age));
    }
        public void display(){
            for(int i=0;i<dataList.size();i++){
              
                System.out.println("-------------------"+"\n"+"Name: "+dataList.get(i).name);
                System.out.println("Age: "+dataList.get(i).age);
                System.out.println("Address: "+dataList.get(i).address);
            }
            System.out.println("-------------------");
      }
        }
        