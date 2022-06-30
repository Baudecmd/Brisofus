package com.baudec.brisofus.repository;

import com.baudec.brisofus.entity.Item;
import com.baudec.brisofus.entity.PriceItem;
import com.baudec.brisofus.entity.PriceItemKey;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;

@Repository
public interface PriceItemRepository extends CrudRepository<PriceItem, Long>{
    PriceItem findFirstByItemOrderByDateDesc(Item item);

    ArrayList<PriceItem> findAllByOrderByDateDesc();

}
