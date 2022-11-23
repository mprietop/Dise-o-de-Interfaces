package com.example.myothercatalog;

import org.json.JSONObject;

public class Futbolista {
    private String name;
    private String description;
    private String imageUrl;

    public Futbolista(JSONObject object) {
        this.name = name;
        this.description = description;
        this.imageUrl = imageUrl;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public String getImageUrl() {
        return imageUrl;
    }
}
