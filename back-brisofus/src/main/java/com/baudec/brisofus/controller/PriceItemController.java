package com.baudec.brisofus.controller;

import com.baudec.brisofus.entity.HistoricPrice;
import com.baudec.brisofus.entity.PriceItem;
import com.baudec.brisofus.entity.PriceItemRep;
import com.baudec.brisofus.repository.ItemRepository;
import com.baudec.brisofus.service.HistoricPriceService;
import com.baudec.brisofus.service.ItemService;
import com.baudec.brisofus.service.PriceItemService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@CrossOrigin(origins = "*")
@RestController
public class PriceItemController {

    @Autowired
    PriceItemService priceItemService;

    @Autowired
    HistoricPriceService historicPriceService;

    @Autowired
    ItemService itemService;

    @PostMapping(value="/priceItem",produces = "application/json")
    public PriceItem updatePriceItem(@RequestBody PriceItemRep priceItemRep){
        System.out.println("priceItemUPDATE");
        System.out.println(priceItemRep);
       PriceItem priceItem=priceItemService.addPriceItem(priceItemRep);
       if(priceItem==null) return null;
       return priceItem;
    }

    @GetMapping(value="/priceCraftItem/name/{name}",produces = "application/json")
    public List<HistoricPrice> getLastPriceItem(@PathVariable("name") String name){
        return historicPriceService.getHistoricPriceList(name);
    }

    @GetMapping(value="/priceHDVItem/name/{name}",produces = "application/json")
    public List<HistoricPrice> getLastPriceItemHDV(@PathVariable("name") String name){
        return historicPriceService.getHistoricPriceList(name);
    }

    @GetMapping("/priceItem")
    public ArrayList<PriceItem> getAllItemPrice(){
        return priceItemService.findLastPriceAllItem();
    }

    @GetMapping("/priceSellItem/{name}")
    public List<HistoricPrice> getItemHDVPrice(@PathVariable("name") String name){
        return itemService.getItem(name).lastxDaysPriceItem(14).stream().map(elem->new HistoricPrice(elem.getPrice(), elem.getDate(),elem.getItem())).collect(Collectors.toList());
    }




}
