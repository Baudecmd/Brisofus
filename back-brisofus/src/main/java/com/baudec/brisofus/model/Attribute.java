package com.baudec.brisofus.model;

public class Attribute {
    String nom;
    int min;
    int max;

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }

    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }

    public Attribute(String nom, int min, int max) {
        this.nom = nom;
        this.min = min;
        this.max = max;
    }
}
