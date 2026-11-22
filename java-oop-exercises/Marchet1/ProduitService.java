package Marchet1;
import  java.util.ArrayList;
import java.util.List;

public class ProduitService implements Idao<Produit>{
 protected List<Produit> service=new ArrayList<>();
 @Override
    public void create(Produit o)throws InvalidPriceException{
        if(o.getPrix()<=0){
            throw new InvalidPriceException("price is invalide");
        }
        service.add(o);
    }
    @Override
    public Produit read(int id){
        for(Produit p:service){
            if(p.getId()==id){
                return p;
            }
        }
        return null;
    }
    @Override
    public void update(Produit o){
        for(Produit p:service){
            if(p.getId()==o.getId()){
                p.setNom(o.getNom());
                p.setPrix(o.getPrix());
            }
        }
    }
    @Override
    public void delete(int id){
        service.removeIf(p->p.getId()==id);
    } 
    public List<Produit> findAll(){
        return service;
    } 
    
}
