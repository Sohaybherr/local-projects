package Marchet1;
public interface Idao<T> {
    void create(T entity) throws InvalidPriceException;
    T read(int id);
    void update(T entity);
    void delete(int id);

}
