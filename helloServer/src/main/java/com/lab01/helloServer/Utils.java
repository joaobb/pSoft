package com.lab01.helloServer;

import java.time.LocalTime;

public class Utils {

    public static String getTime() {
        return (LocalTime.now() + "").split("\\.")[0];
    }

    public static String getSaudacao() {
        return (LocalTime.now().getHour() > 18 ? "a noite" : (LocalTime.now().getHour() > 12 ? "a tarde" : "m dia"));
    }
}
