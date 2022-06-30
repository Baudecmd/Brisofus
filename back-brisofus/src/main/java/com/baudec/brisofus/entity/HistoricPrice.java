package com.baudec.brisofus.entity;

import java.util.Date;

public record HistoricPrice(int price, Date d, Item item) {
}
