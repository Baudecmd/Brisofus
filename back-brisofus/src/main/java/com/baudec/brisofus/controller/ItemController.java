package com.baudec.brisofus.controller;

import com.baudec.brisofus.entity.Item;
import com.baudec.brisofus.service.ItemService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;

@CrossOrigin(origins = "*")
@Controller
public class ItemController {

    @Autowired
    ItemService itemService;

    @GetMapping("/items/{name}")
    public @ResponseBody Item getItem(@PathVariable String name){
        return itemService.getItem(name);
    }


    @GetMapping("/items")
    public @ResponseBody ArrayList<Item> getAllItem(){
        return itemService.getAllItem();
    }

    @PostMapping("/items")
    public @ResponseBody Item getAllItem(@RequestBody Item item){
        return itemService.addItem(item);
    }
}
