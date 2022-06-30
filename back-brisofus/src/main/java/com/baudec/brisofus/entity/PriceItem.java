package com.baudec.brisofus.entity;

import org.assertj.core.util.DateUtil;

import javax.persistence.*;
import java.io.Serializable;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@Entity
public class PriceItem {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    long id;
    int price;
    int hdvPrice;

    @ManyToOne
    Item item;
    Date date;


    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }


    public PriceItem(int price, Item item,Date d) {
        this.price = price;
        this.item = item;
        this.hdvPrice=0;

        this.date = d;    }


    public PriceItem(int price, Item item,int hdvPrice) {
        this.price = price;
        this.item = item;
        this.hdvPrice=hdvPrice;
        SimpleDateFormat formatter= new SimpleDateFormat("yyyy-mm-dd");
        this.date = new Date(System.currentTimeMillis());    }

    public PriceItem(int price, Item item,Date date,int id,int hdvPrice) {
        this.price = price;
        this.item = item;
        this.date = date;
        this.id=id;
        this.hdvPrice=hdvPrice;
    }

    public PriceItem(int price, Item item) {
        this.price = price;
        this.item = item;
        SimpleDateFormat formatter= new SimpleDateFormat("yyyy-mm-dd");
        this.date = new Date(System.currentTimeMillis());    }


    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public Item getItem() {
        return item;
    }

    public void setItem(Item item) {
        this.item = item;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public PriceItem() {

    }

    public int getHdvPrice() {
        return hdvPrice;
    }

    public void setHdvPrice(int hdvPrice) {
        this.hdvPrice = hdvPrice;
    }

    @Override
    public String toString() {
        return "PriceItem{" +
                "price='" + price + '\'' +
                ", item='" + item + '\'' +
                ", date='" + date +'\'' +
                '}';
    }


}
