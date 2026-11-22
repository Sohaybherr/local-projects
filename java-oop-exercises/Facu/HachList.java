package Facu;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class HachList {
       protected List<Etudiant> list;
       protected HashMap <Etudiant, String> hach;
    public HachList(){
        this.hach=new HashMap<Etudiant,String>();
         this.list=new ArrayList<Etudiant>();
    }
    public void addEtudiant(Etudiant a){
    list.add(a);
    }
    public Etudiant findById(String id){
        for(Etudiant e:this.list){
        if(e.getId().equals(id)){
              return e;
        }
     } 
     return null;
    }
    public void linkEtudiantNum(String id,String num){
    Etudiant e=findById(id);
    if(e!=null){
    (this.hach).put(e, num);
    }
    else{
        System.out.println("Element not Found");
        return;
    }
    }
    public String getNumById(String id){
    Etudiant e=findById(id);
    if(e!=null){
        return this.hach.get(e);
    }
    return null;
    }
    public String getEtudiantInfo(String id){
        Etudiant e=findById(id);
        return e.toString()+", NumTel: "+this.hach.get(e);

    }
    public boolean linkedOrNot(String id){
           Etudiant e=findById(id);
    if(e!=null){
    return this.hach.containsKey(e);
    }
    else{
        System.out.println("NOt even found in list");
        return false;
    }
    }
    public void showall(){
        for (Etudiant e : this.list) {
            if(linkedOrNot(e.getId())){
                System.out.println("\n"+getEtudiantInfo(e.getId()));
            }
            else{
                System.out.println("\n"+e.toString()+" Not linked");
            } 
        }
    }
}
