package Pairtable;

import java.util.List;

public class Apptable implements Iao<Integer> {
protected int [] appTable;
public Apptable (){
    this.appTable=new int[0];
}
public void add (int a)throws NomNotPair{
    if(a%2==1){
        throw new NomNotPair("NOT A PAIR");
    }
    else{
        int[] newTable =new int[this.appTable.length+1];
        for (int i = 0; i < this.appTable.length; i++) {
            newTable[i]=this.appTable[i];
        }
        newTable[this.appTable.length]=a;
        this.appTable=newTable;
    }
}
public boolean exist(int a)throws NomNotPair{
  if(a%2==1){
        throw new NomNotPair("NOT A PAIR");
       
    }
 else{
for (int i:this.appTable) {
    if(a==i){
        return  true;
    }
}
return false;
 }   
}
public int getindice(int a)throws NomNotPair{
    if(a%2==1){
        throw new NomNotPair("NOT A PAIR");
       
    }
 else{
    if(this.exist(a)){
        List<Integer> list= new java.util.ArrayList<>();
        for (int i = 0; i < this.appTable.length; i++) {
            if(this.appTable[i]==a){
                list.add(i);
            }
        }
       return list.get(list.size() - 1);
    }
}
    return -1;
}
public void show(){
    System.out.print("AppTable: ");
    for (int i : this.appTable) {
        System.out.print(i + " ");
    }
    System.out.println();
}
}
