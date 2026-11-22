package Salles;
import java.util.List;

public interface IDao<T> {

    boolean create(T o) throws NbreObjetsStockesDep10Exception;

    boolean delete(T o);

    boolean update(T o);

    T findById(int id);

    List<T> findAll();
}
