package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ImageView;

public class DetailActivity extends AppCompatActivity {
    //Creamos una variable de tipo ImageView para poder trabajar con ella en java
    private ImageView imagePrenda;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);
        //Asociamos el ImageView del xml al de java mediante el ID
        imagePrenda = findViewById(R.id.imagePrenda);
        //Ponermos el ScaleType como Center crop
        ImageView.ScaleType centerCrop = ImageView.ScaleType.CENTER_CROP;
    }
}