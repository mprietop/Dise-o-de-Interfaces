package com.example.mycatalog;

import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;

import android.os.Bundle;
<<<<<<< HEAD
=======
import android.widget.ImageView;
import android.widget.Toolbar;
>>>>>>> temp-branch2

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);
<<<<<<< HEAD
=======
        //Asociamos el ImageView del xml al de java mediante el ID
        imagePrenda = findViewById(R.id.imagePrenda);
        //Ponermos el ScaleType como Center crop
        ImageView.ScaleType centerCrop = ImageView.ScaleType.CENTER_CROP;

>>>>>>> temp-branch2
    }
}