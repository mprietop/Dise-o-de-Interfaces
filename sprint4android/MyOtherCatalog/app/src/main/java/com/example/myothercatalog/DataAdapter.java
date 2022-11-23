package com.example.myothercatalog;

import android.app.Activity;
import android.graphics.Bitmap;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.List;

public class DataAdapter extends RecyclerView.Adapter<DataViewHolder> {
    private List<Futbolista> allData;
    private Activity activity;

    public DataAdapter(List<Futbolista> lista, Activity activity) throws JSONException {
        this.allData = lista;
        this.activity = activity;
    }

    @NonNull
    @Override
    public DataViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View cellView = inflater.inflate(R.layout.cell_layout, parent, false);
        return new DataViewHolder(cellView);
    }

    @Override
    public void onBindViewHolder(@NonNull DataViewHolder holder, int position) {
        Futbolista dataInPositionToBeRendered = allData.get(position);
        holder.showData(dataInPositionToBeRendered, activity);
    }

    @Override
    public int getItemCount() {
        return allData.size();
    }
}
