package com.baudec.brisofus.controller;

import com.baudec.brisofus.entity.HistoricComparePrice;
import com.baudec.brisofus.entity.Item;
import com.baudec.brisofus.entity.ItemFilter;
import com.baudec.brisofus.entity.PriceItem;
import com.baudec.brisofus.service.ItemService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "*")
@RestController
public class SearchController {
    @Autowired
    ItemService itemService;

    Logger logger = LoggerFactory.getLogger(SearchController.class);
    @PostMapping(value="/search",produces = "application/json",consumes = "application/json")
    public List<HistoricComparePrice> searchItem(@RequestBody ItemFilter filter){
        logger.info(" Requête de recherche {}",filter);
        return itemService.getAllItemWithFilter(filter);
    }
}
