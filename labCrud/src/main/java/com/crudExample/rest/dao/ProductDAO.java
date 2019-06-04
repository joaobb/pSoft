package com.crudExample.rest.dao;

import com.crudExample.rest.model.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.io.Serializable;

@Repository //Indicates to Spring, that this will the interface for the connection with the DB
public interface ProductDAO<T, ID extends Serializable> extends JpaRepository<Product, Long> {

    Product save(Product product);
    Product findByID(long id);

}
