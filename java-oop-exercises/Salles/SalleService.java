package Salles;
import java.util.ArrayList;
import java.util.List;

public class SalleService implements IDao<SalleCl> {
    private List<SalleCl> salles=new ArrayList<>();
    @Override
    public boolean create(SalleCl o)throws NbreObjetsStockesDep10Exception {
        if (salles.size() >= 10) {
            throw new NbreObjetsStockesDep10Exception("Nombre d'objets stockés dépasse 10");
        }
        salles.add(o);
        return true;
    }

    @Override
    public boolean delete(SalleCl o) {
       if(salles.contains(o)){
           salles.remove(o);
           return true; 
        }
        return false;
    }

    @Override
    public boolean update(SalleCl o) {
        if(salles.contains(o)){
            o.setCode(0);
            o.setLibelle("updated"  );
            o.setId("000");
            return true;
        }
        return false;
    }

    @Override
    public SalleCl findById(int id) {
        if(id>=0 && id<salles.size()){
            return salles.get(id);
        }
        return null;
    }

    @Override
    public List<SalleCl> findAll() {
        if(!salles.isEmpty()){
            return salles;  
    }   
        return null;
    }

    
}
