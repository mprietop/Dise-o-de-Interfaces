package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class Futbolista {
    private String name;
    private String description;
    private String imageUrl;

    public Futbolista(JSONObject object) throws JSONException {
        this.name = object.getString("name");
        this.description = object.getString("description");
        this.imageUrl = object.getString("image_url");
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
