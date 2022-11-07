package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CatalogActivity extends AppCompatActivity {
    //Creamos una variable de tipo Button para poder trabajar con ella en java
    private Button navButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);
        //Asociamos el Button del xml al de java mediante el ID
        navButton = findViewById(R.id.navButton);
        //Creamos un intent para poder llamar a una actividad nueva
        Intent intent = new Intent(this, DetailActivity.class);

        navButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //Creamos un onClickListener para que cuando detecte que se pulsa el boton
                //entra ahí y comienza la actividad asociada al intent
                startActivity(intent);
            }
        });
    }
}