package com.baudec.brisofus.service;

import com.baudec.brisofus.entity.HistoricComparePrice;
import com.baudec.brisofus.entity.Item;
import com.baudec.brisofus.entity.ItemFilter;
import com.baudec.brisofus.entity.PriceItem;
import com.baudec.brisofus.repository.ItemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

@Service
public class ItemService {

    @Autowired
    ItemRepository itemRepository;

    @Autowired
    PriceItemService priceItemService;


    public Item getItem(String name){
        return itemRepository.findByName(name);
    }
    public ArrayList<Item> getAllItem(){
        return (ArrayList<Item>) itemRepository.findAll();
    }

    public Item addItem(Item item){
        return itemRepository.save(item);
    }

    public ArrayList<HistoricComparePrice> getAllItemWithFilter(ItemFilter filter) {
        List<Item> itemList=itemRepository.getAllItemByFilter(filter);
        List<HistoricComparePrice> priceItemList=new ArrayList<HistoricComparePrice>();
        for (Item item:itemList
             ) {if(!item.getListAttribute().isEmpty() && item.containsAllAttribute(filter.getListAttribute()) && item.containsType(filter.listType) )
            {
                HistoricComparePrice historicComparePrice=null;
                PriceItem price=priceItemService.getLastPriceCraft(item.getName());
                if(price.getPrice() != 0)
                 historicComparePrice= new HistoricComparePrice(price.getPrice(),item.average14days(),item,Double.valueOf(price.getPrice())/ item.average14days());
                priceItemList.add(historicComparePrice);
           }

        }

        return (ArrayList<HistoricComparePrice>) priceItemList;

    }
}
