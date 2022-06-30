package com.baudec.brisofus.entity;

import java.util.Date;

public record HistoricComparePrice(int price,Long averagePrice,Item item,double ratio) {
}
