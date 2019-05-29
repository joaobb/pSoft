package com.crudExemple.rest.controller;

import com.crudExemple.rest.model.Product;
import com.crudExemple.rest.service.ProductService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping({"/v1/products"})
public class ProductController {

    private ProductService productService;

    ProductController(ProductService productService) {
        this.productService = productService;
    }

    @GetMapping(value = "/{ìd}")
    @ResponseBody
    public ResponseEntity<Product> findById(@PathVariable long id) {
        Product product = productService.findById(id);

        if (product == null) {
            throw new NullPointerException("Product not found");
        }

        return new ResponseEntity<Product>(product, HttpStatus.OK);
    }

    @PostMapping(value = "/")
    @ResponseBody
    public ResponseEntity<Product> create(@RequestBody Product product) {
        Product newProduct = productService.create(product);

        if (newProduct == null) {
            //Error 500?
            throw new InternalError("Something went wrong");
        }
        return new ResponseEntity<Product>(newProduct, HttpStatus.CREATED);
    }

    @DeleteMapping(value = "/{id}")
    public ResponseEntity delete(@PathVariable long id) {
        try {
            productService.delete(id);
            return new ResponseEntity(HttpStatus.OK);
        } catch (Exception e) {
            throw new InternalError("Something went wrong");
        }
    }

    @PutMapping(value = "/")
    public ResponseEntity<Product> update(@RequestBody Product product) {
        try  {
            Product updated = productService.update(product);
            return new ResponseEntity<>(updated, HttpStatus.OK);
        } catch (Exception e) {
            throw new InternalError("Something went wrong");
        }
    }
}
