package com.baudec.brisofus.service;

import com.baudec.brisofus.entity.HistoricPrice;
import com.baudec.brisofus.entity.Item;
import com.baudec.brisofus.entity.PriceItem;
import com.baudec.brisofus.repository.ItemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@Service
public class HistoricPriceService {

    @Autowired
    ItemRepository itemRepository;

    public List<HistoricPrice> getHistoricPriceList(String itemName){
        Item item=itemRepository.findByName(itemName);

        return getHistoricPrice(item);

    }

    public List<HistoricPrice> getHistoricPrice(Item item){
        List<HistoricPrice> priceItemList=new ArrayList<HistoricPrice>();
        for(int i=30;i>=0;i--){
            Date d=new Date();
            d.setTime( d.getTime() - (long)i*1000*60*60*24 );
            int price=item.getCraftPriceAtADate(d);
            priceItemList.add(new HistoricPrice(price,d,item));
        }
        return priceItemList;
    }
}
