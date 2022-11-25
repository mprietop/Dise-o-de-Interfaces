package com.example.myothercatalog;

import android.content.Context;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.squareup.picasso.Picasso;

public class DetailActiviy extends AppCompatActivity {
    private TextView nameTextView;
    private ImageView imageView;
    private TextView descriptionTextView;
    private Context context;
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        nameTextView.findViewById(R.id.detailName);
        imageView.findViewById(R.id.detailImage);
        descriptionTextView.findViewById(R.id.detailDescription);

        nameTextView.setText(getIntent().getStringExtra("name"));
        descriptionTextView.setText(getIntent().getStringExtra("description"));
        Picasso.with(context).load(getIntent().getStringExtra("imageUrl")).into(imageView);

        //Me falta conseguir los datos espe
    }
}
