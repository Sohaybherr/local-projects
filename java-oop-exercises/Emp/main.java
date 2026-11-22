package Emp;

import java.util.Scanner;

public class main {
    public static void main(String[] args){
        int i =1;
         Employeservice es = new Employeservice();
        while (i!=0) {
            // get user input and perform operations based on choice 
       System.out.println("enter the right option:\n");
       System.out.println("0: exit\n");
       System.out.println("1: create an employee\n");
       System.out.println("2: read an employee\n"); 
         System.out.println("3: update an employee\n");
           System.out.println("4: delete an employee\n");
             System.out.println("5: display all employees\n");
             System.out.println("6: display all employees ordered by ID\n");
             System.out.println("7: display all employees ordered by Name\n");
             System.out.println("8: display all employees ordered by Salary\n");
            
            Scanner sc = new Scanner(System.in);
            i = sc.nextInt();
            switch(i){
                case 0:
                    System.out.println("exiting...");
                    break;
                case 1:
                    System.out.println("enter  name and salary:");
                    String nom = sc.next();
                    Double sal = sc.nextDouble();
                    Employe e = new Employe( nom, sal);
                    try{
                        es.create(e);
                        System.out.println("employee created successfully");
                    }catch(SalaireInvalidException ex){
                        System.out.println(ex.getMessage());
                    }
                    break;
                case 2:
                    System.out.println("enter id to read:");
                    String readId = sc.next();
                    Employe emp = es.read(readId);
                    if(emp != null){
                        System.out.println(emp.toStrig());
                    }
                    break;
                case 3:
                    System.out.println("enter id name and salary to update:");
                    String upId = sc.next();
                    String upNom = sc.next();
                    Double upSal = sc.nextDouble();
                    Employe upEmp = new Employe(upNom, upSal);
                    upEmp.setID(upId);
                    es.update(upEmp);
                    break;
                case 4:
                    System.out.println("enter id to delete:");
                    String delId = sc.next();
                    es.delete(delId);
                    break;
                case 5:
                    es.findAll().forEach(emp1 -> System.out.println("++++++++++++++++\n" + emp1.toStrig()));
                    break;
                case 6:
                    es.orderID().forEach(emp1 -> System.out.println("++++++++++++++++\n" + emp1.toStrig()));
                    break;
                case 7:
                    es.orderNom().forEach(emp1 -> System.out.println("++++++++++++++++\n" + emp1.toStrig()));
                    break;
                case 8:
                    es.orderSal().forEach(emp1 -> System.out.println(emp1.toStrig()));
                    break;
                default:
                    System.out.println("invalid option");
            }
    }
}}
