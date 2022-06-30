import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import Item from './models/Item';
import ItemQuantity from './models/ItemQuantity';

@Injectable({
  providedIn: 'root'
})
export class BreakingsService {

  listBreaking:ItemQuantity[]=[];

  constructor(private http: HttpClient) { }

  addItems(item:Item){
    var itemQ=new ItemQuantity();
    itemQ.quantite=1;
    itemQ.resourceItem=item;
    this.listBreaking.push(itemQ);
  }

  brisageItem(){
    console.log(this.listBreaking);
    return this.http.post("http://127.0.0.1:5000/item/comp_buy",this.listBreaking);
  }
}
