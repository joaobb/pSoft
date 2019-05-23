package com.lab01.helloServer.controllers;

public class Greeting {
    private String name;

    private String greeting;

    Greeting(String name, String greeting) {
        this.name = name;
        this.greeting = greeting;
    }

    public String getName() {
        return name;
    }

    public String getGreeting() {
        return greeting;
    }

}
