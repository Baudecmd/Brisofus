package com.baudec.brisofus.repository;

import com.baudec.brisofus.entity.Item;
import com.baudec.brisofus.entity.ItemFilter;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;

@Repository
public interface ItemRepository extends CrudRepository<Item, String> {

    Item findById(Long id);
    Item findByName(String name);

    @Query("SELECT item FROM Item item WHERE item.level > :#{#itemFilter.levelMin} and item.level < :#{#itemFilter.levelMax}   ")
    ArrayList<Item> getAllItemByFilter(@Param("itemFilter")ItemFilter itemFilter);
}
