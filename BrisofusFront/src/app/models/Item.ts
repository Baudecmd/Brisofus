import CraftItem from "./CraftItem";
import DofusAttribute from "./DofusAttribute";

export default class Item{
    id:number;
    name:String;
    listAttribute:DofusAttribute[];
    listCraftResources:CraftItem[];
    level:number;
    url:String;
    imgId:number;
    type:String;
    lastPrice:number;

    constructor(){
        this.id=0;
        this.name="";
        this.listAttribute=[];
        this.listCraftResources=[];
        this.level=0;
        this.url="";
        this.imgId=0;
        this.type="";
        this.lastPrice=0;
    }
}