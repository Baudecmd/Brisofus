package com.baudec.brisofus.service;

import com.baudec.brisofus.entity.Item;
import com.baudec.brisofus.entity.ItemResource;
import com.baudec.brisofus.entity.PriceItem;
import com.baudec.brisofus.entity.PriceItemRep;
import com.baudec.brisofus.repository.ItemRepository;
import com.baudec.brisofus.repository.PriceItemRepository;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import net.ricecode.similarity.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.text.Normalizer;
import java.util.ArrayList;
import java.util.Optional;

@Service
public class PriceItemService {

    @Autowired
    PriceItemRepository priceItemRepository;

    @Autowired
    PriceItemService priceItemService;
    @Autowired
    ItemRepository itemRepository;

    public PriceItem getLastPriceCraft(String name){
        Item item=itemRepository.findByName(name);

        long price=0;
        for (ItemResource itemResource
                :item.getListCraftResources()
        ) {
            PriceItem priceItem=findLastPrice(itemResource.resourceItem.getName());
            if(priceItem!=null){
                int itemPrice=priceItem.getPrice();
                price+=itemResource.quantite*(itemPrice);
            }
        }
        return new PriceItem((int) price,item,findLastPrice(item.getName()).getPrice());
    }

    public PriceItem getLastPriceCraftByName(String nom){
        ItemScore item= priceItemService.getMostSimilarItemFromString(nom);
        long price=0;
        for (ItemResource itemResource
             :item.getItem().getListCraftResources()
             ) {
            PriceItem priceItem=findLastPrice(itemResource.resourceItem.getName());
            if(priceItem!=null){
                int itemPrice=priceItem.getPrice();
                price+=itemResource.quantite*(itemPrice);
            }
        }
        return new PriceItem((int) price,item.item,findLastPrice(item.item.getName()).getPrice());
    }

    public static String stripAccents(String s)
    {
        s = Normalizer.normalize(s, Normalizer.Form.NFD);
        s = s.replaceAll("[\\p{InCombiningDiacriticalMarks}]", "");
        return s;
    }

    public ItemScore getMostSimilarItemFromString(String nom){
        double score=0;
        ItemScore itemScore=null;
        for (Item i : itemRepository.findAll()
        ) {
            String target = stripAccents(nom);
            String source = stripAccents(i.getName());


            SimilarityStrategy strategy = new LevenshteinDistanceStrategy();

            StringSimilarityService service = new StringSimilarityServiceImpl(strategy);

            if(service.score(source, target)>=score){
                score=service.score(   source
                        ,       target
                );
                itemScore=new ItemScore(i,score);
            }

        }

        return itemScore;

    }
    @Getter
    @Setter
    @NoArgsConstructor
    @AllArgsConstructor
    public class ItemScore{
        Item item;
        double score;
    }

    public PriceItem addPriceItem(PriceItemRep priceItemRep){
        Item testitem=itemRepository.findByName(priceItemRep.item());
        if(testitem !=null){
            PriceItem priceItem=new PriceItem(Integer.parseInt(priceItemRep.price()),testitem);
            System.out.println(priceItem.getItem().getName() + " == "+testitem.getName());
            return priceItemRepository.save(priceItem);
        }else{

        ItemScore bestItem=getMostSimilarItemFromString(priceItemRep.item());

        PriceItem priceItem=new PriceItem(Integer.parseInt(priceItemRep.price()),bestItem.item);

            System.out.println( " recu "+priceItemRep.item() +" vs "+ bestItem.item.getName() + " "+bestItem.score);

            if(bestItem.score>=0.94f){

            return priceItemRepository.save(priceItem);
        }
            System.out.println(priceItem.getItem().getName()+" trouvé "+ bestItem.score+" et  pas sauvegardé");

        return null;


    }}

    public PriceItem findLastPrice(String name){
            Item item=itemRepository.findByName(name);
        if(item != null){
            PriceItem priceItem=priceItemRepository.findFirstByItemOrderByDateDesc(item);
            if (priceItem != null){
                return priceItem;
            }
            else new PriceItem(0,item,0);
        }
        return new PriceItem(0,item,0);
    }

    public ArrayList<PriceItem> findLastPriceAllItem() {
       return  priceItemRepository.findAllByOrderByDateDesc();
    }
}
