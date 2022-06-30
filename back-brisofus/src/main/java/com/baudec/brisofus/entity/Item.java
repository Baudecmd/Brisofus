package com.baudec.brisofus.entity;

import com.baudec.brisofus.BrisofusApplication;
import lombok.*;

import javax.persistence.*;
import java.util.*;


@ToString
@Entity
public class Item {
    long id;
    int imgId;
    @Id
    String name;
    @OneToMany( cascade = CascadeType.ALL)
    List<Statistique> listAttribute=new ArrayList<Statistique>();
    @OneToMany (cascade = CascadeType.ALL)
    List<ItemResource> listCraftResources=new ArrayList<ItemResource>();
    int level;

    @Getter
    String type;
    @OneToMany(mappedBy = "item")
    List<PriceItem> priceItemList;

    public int getCraftPriceAtADate(Date date){
        int price=0;
        for (ItemResource itemres:this.listCraftResources
             ) {

            List<PriceItem> priceItemList=itemres.getResourceItem().getPriceItemList().stream().filter(elem->elem.getDate().before(date)).toList();
            if(priceItemList.size()==0){
                price+=0;
            }else price+=priceItemList.get(priceItemList.size()-1).price*itemres.quantite;
        }
        return price;

    }

    public List<PriceItem> lastxDaysPriceItem(int days){
        List<PriceItem> priceItemList=new ArrayList<>();
        for(int i=days;i>=0;i--){
            Date d=new Date();
            d.setTime( d.getTime() - (long)i*1000*60*60*24 );
            Optional<PriceItem> priceItem=getPriceItemList().stream().filter(elem->elem.getDate().before(d)).findFirst();

            if(priceItem.isPresent()==true)
            {
                priceItemList.add(priceItem.get());
            }
            else{
                priceItemList.add(new PriceItem(0,this,d));
            }
        }
        return priceItemList;
    }

    public Long average14days(){
        Long total=0L;
        Long count=0L;
        for(int i=14;i>=0;i--){
            Date d=new Date();
            d.setTime( d.getTime() - (long)i*1000*60*60*24 );
            int price=this.getCraftPriceAtADate(d);
            if(price!=0){
                total+=price;
                count++;
            }

        }
        if(count!=0)
            return total/count;
        else return 0L;
    }

    public boolean containsAllAttribute(List<String> listAttribute){
        for (String string:listAttribute
             ) {
            boolean trouve=false;
            for (Statistique statistique: this.listAttribute
                 ) {
                if(statistique.nom.toLowerCase(Locale.ROOT).equals(string.toLowerCase(Locale.ROOT)))trouve=true;
            }
            if(!trouve)return false;
        }
        return true;
    }

    public int getLastPrice(){
        if(priceItemList==null || priceItemList.size()==0 ){
            return 0;
        }
        return priceItemList.get(priceItemList.size()-1).price;
    }

    public boolean containsType(List<String> listType){
        return listType.contains(type);
    }
    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }



    public Item(long id, String nom) {
        this.id = id;
        this.name = nom;
    }

    public Item(BrisofusApplication.EquipmentParsing.ItemRep itemRep) {
        this.id = itemRep.getItem_id();
        this.name = itemRep.getItem_name();
        this.imgId=itemRep.getImg_id();
        this.level=itemRep.getLevel();
        this.type=itemRep.getItem_type();
        this.imgId=itemRep.getImg_id();
        this.listAttribute=itemRep.getList_stat().stream().map(elem->new Statistique(elem.getMin(),elem.getMax(),elem.getType())).toList();
        this.listCraftResources=itemRep.getList_craft().stream().map(elem->new ItemResource(new Item(elem.getItem()),elem.getQuantite(),0)).toList();
    }

    public List<ItemResource> getListCraftResources() {
        return listCraftResources;
    }

    public void setListCraftResources(List<ItemResource> listCraftResources) {
        this.listCraftResources = listCraftResources;
    }

    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Item(String nom) {
        this.name = nom;
    }

    public Item() {
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Statistique> getListAttribute() {
        return listAttribute;
    }

    public void setListAttribute(List<Statistique> listAttribute) {
        this.listAttribute = listAttribute;
    }

    public int getImgId() {
        return imgId;
    }

    public void setImgId(int imgId) {
        this.imgId = imgId;
    }

    private List<PriceItem> getPriceItemList() {
        return priceItemList;
    }

    public void setPriceItemList(List<PriceItem> priceItemList) {
        this.priceItemList = priceItemList;
    }
}


@Entity
@Setter
@Getter
@ToString
@AllArgsConstructor
@NoArgsConstructor
class Statistique{
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    int id;
    int min;
    int max;
    @Column( length = 1000 )
    String nom;

    Statistique(int min,int max, String nom){
        this.min=min;
        this.max=max;
        this.nom=nom;
    }


}