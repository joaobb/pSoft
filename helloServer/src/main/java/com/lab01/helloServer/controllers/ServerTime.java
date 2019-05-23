package com.lab01.helloServer.controllers;

import com.lab01.helloServer.Utils;

public class ServerTime {
    private String time;

    ServerTime() {
        this.time = Utils.getTime();
    }

    public String getTime() {
        return this.time;
    }
}
