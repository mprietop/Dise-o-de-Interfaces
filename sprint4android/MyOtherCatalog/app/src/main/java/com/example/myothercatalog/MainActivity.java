package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import android.app.Activity;
import android.content.Context;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private RecyclerView recyclerView;
    private RequestQueue queue;
    private Context context = this;
    private Button button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.recyclerView);
        getData();
        //button = findViewById(R.id.button);

    }

    public void getData() {
        Activity activity = this;
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/mprietop/Dise-o-de-Interfaces/main/API-REST/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        List<Futbolista> lista = new ArrayList<>();
                        try {
                            for(int i = 0; i < response.length(); i++){
                                JSONObject object = response.getJSONObject(i);
                                Futbolista futbolista = new Futbolista(object);
                                //Log.i("datos", futbolista.getName());
                                lista.add(futbolista);
                            }
                            DataAdapter dataAdapter = new DataAdapter(lista, activity);
                            recyclerView.setAdapter(dataAdapter);
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }

                        recyclerView.setHasFixedSize(true);
                        recyclerView.setLayoutManager(new LinearLayoutManager(context));

                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(activity, "Error accediendo a la API", Toast.LENGTH_SHORT).show();
                    }
                }
        );
        queue = Volley.newRequestQueue(context);
        queue.add(request);
    }
}