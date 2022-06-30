package com.baudec.brisofus.entity;

import lombok.*;

import javax.persistence.*;

@Getter
@Setter
@Entity
public class ItemResource{


    @OneToOne (cascade = CascadeType.ALL)
    public Item resourceItem;

    public int quantite;

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    public int id;


    public ItemResource(Item resourceItem, int quantite, int id) {
        this.resourceItem = resourceItem;
        this.quantite = quantite;
        this.id = id;
    }

    public ItemResource() {
    }

    public Item getResourceItem() {
        return resourceItem;
    }

    public void setResourceItem(Item resourceItem) {
        this.resourceItem = resourceItem;
    }

    public int getQuantite() {
        return quantite;
    }

    public void setQuantite(int quantite) {
        this.quantite = quantite;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
}

