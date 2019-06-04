package com.crudExample.exception.product;

import org.springframework.web.bind.annotation.ControllerAdvice;

import java.util.Date;

@ControllerAdvice
public class CustomRestError {
    public CustomRestError(Date date, String message, String description) {

    }
}
