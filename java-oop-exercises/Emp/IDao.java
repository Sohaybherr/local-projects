package Emp;

import java.util.List;

public interface IDao<T> {
void create(T o)throws SalaireInvalidException;
T read(String id);
void update(T o);
void delete(String id);
List<T> findAll();
}
