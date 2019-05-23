package com.lab01.helloServer.controllers;

import com.lab01.helloServer.Utils;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RestApiController {

    @RequestMapping(value="/greetingRest", produces = "application/json")
    public Greeting greeting(@RequestParam(value="name", defaultValue = "Txutxucador") String name) {
        return new Greeting(name, Utils.getSaudacao());
    }

    @RequestMapping("/timeRest")
    public ServerTime time() {
        return new ServerTime();
    }

}
