package Emp;

import java.util.ArrayList;
import java.util.List;

public class Employeservice implements IDao<Employe>{
    protected List<Employe> employs=new ArrayList<>();
    @Override 
    public void create(Employe o)throws SalaireInvalidException{
      if(o.getSal()<3000){
         throw new SalaireInvalidException("moins que min");
      }  
      else{
        employs.add(o);
      }
    }
    @Override
    public Employe read(String id){
        for(Employe e:employs){
            if(e.getId().compareTo(id)==0){
                return e;
            }
        }
      System.out.println("Item not found");
        return null;
    }
    @Override
    public void update(Employe o){
        for(Employe e:employs){
            if(e.getId().compareTo(o.getId())==0){
                e.setNom(o.getNom());
                e.setSal(o.getSal());
                return;
            }
        }
        System.out.println("Item not found");
    }
    @Override
    public  void delete(String id){
         for(Employe e:employs){
            if(e.getId().compareTo(id)==0){
                this.employs.remove(e);
                return;
            }
    }
    System.out.println("Item not found");
    }
    @Override
  public List<Employe> findAll(){
   return employs;
  } 
  public List<Employe> orderID(){
     return employs.stream().sorted((a,b)->a.compId(b)).toList();
  }
   public List<Employe> orderSal(){
     return employs.stream().sorted((a,b)->a.compSal(b)).toList();
  }
   public List<Employe> orderNom(){
     return employs.stream().sorted((a,b)->a.compNom(b)).toList();
  }
    

}
