package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.squareup.picasso.Picasso;

import java.io.ByteArrayOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;

public class DataViewHolder extends RecyclerView.ViewHolder {
    TextView nameTextview;
    ImageView imageView;
    Button button;
    Futbolista data;

    public DataViewHolder(@NonNull View itemView) {
        super(itemView);
        nameTextview = itemView.findViewById(R.id.name);
        imageView = itemView.findViewById(R.id.image);
        button = itemView.findViewById(R.id.button);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(itemView.getContext(), DetailActiviy.class);
                intent.putExtra("name", data.getName());
                intent.putExtra("desciption", data.getDescription());
                intent.putExtra("imageUrl", data.getImageUrl());
                itemView.getContext().startActivity(intent);
            }
        });
    }

    public void showData(Futbolista futbolista, Activity activity) {
        nameTextview.setText(futbolista.getName());
        loadImage(futbolista.getImageUrl(), activity);
        this.data = futbolista;
    }

    private Bitmap getBitMapFromUrl(String url) {
        Bitmap bitmap = null;
        InputStream inputStream;
        try {
            inputStream = new java.net.URL(url).openStream();
            bitmap = BitmapFactory.decodeStream(inputStream);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return bitmap;
    }

    private void loadImage(String url, Activity activity) {
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                Bitmap image = getBitMapFromUrl(url);
                activity.runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        imageView.setImageBitmap(image);
                    }
                });
            }
        });
        thread.start();
    }


}
