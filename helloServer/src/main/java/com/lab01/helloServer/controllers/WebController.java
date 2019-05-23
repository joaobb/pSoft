package com.lab01.helloServer.controllers;

import com.lab01.helloServer.Utils;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.HashMap;
import java.util.Map;

@Controller
public class WebController {

    @GetMapping("/hello")
    public String hello(@RequestParam(name="name", required=false, defaultValue="Txutxucador") String name, Model model) {
        model.addAttribute("name", name);
        return "hello";
    }

    @GetMapping("/time")
    public String time(Model model) {
        model.addAttribute("time", (Utils.getTime()));
        return "time";
    }

    @GetMapping("/greeting")
    public String greeting(@RequestParam(name="name", required=false, defaultValue="Txutxucador") String name, Model model) {
        model.addAttribute("name", name);
        model.addAttribute("time", Utils.getSaudacao());
        return "greetings";
    }
}
