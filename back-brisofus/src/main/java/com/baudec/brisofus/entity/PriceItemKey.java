package com.baudec.brisofus.entity;

import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;

import javax.persistence.Embeddable;
import java.io.Serializable;
import java.util.Date;
import java.util.Objects;

public class PriceItemKey implements Serializable {
    Item item;
    Date date;

    public PriceItemKey() {
    }

    public PriceItemKey(Item item, Date date) {
        this.item = item;
        this.date = date;
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

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        PriceItemKey that = (PriceItemKey) o;
        return Objects.equals(item, that.item) && Objects.equals(date, that.date);
    }

    @Override
    public int hashCode() {
        return Objects.hash(item, date);
    }
}
