package com.crudExample.rest.service;

import com.crudExample.rest.dao.ProductDAO;
import com.crudExample.rest.model.Product;
import org.springframework.stereotype.Service;


@Service
public class ProductService {
    private final ProductDAO productDAO;

    ProductService(ProductDAO productDAO) {
        this.productDAO = productDAO;
    }

    public Product create(Product product) {
        return productDAO.save(product);
    }

    public Product update(Product productToUpdate) {

        Product product = productDAO.findByID(productToUpdate.getID());

        if (product == null) {
            throw new NullPointerException("Couldn't update it. The product doesnt exist.");
        }
        return productDAO.save(productToUpdate);
    }


    public Product findById(long id) {
        return productDAO.findByID(id);
}

    public void delete(long id) {
        productDAO.delete(findById(id));
    }
}
