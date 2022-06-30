import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import Item from '../models/Item';
import ItemFilter from '../models/ItemFilter';
import ItemPrice from '../models/ItemPrice';
import { environment } from 'src/environments/environment';
import HistoricComparePrice from '../models/HistoricComparePrice';
@Injectable({
  providedIn: 'root'
})
export class ItemService {

  constructor(private http: HttpClient) { }

  getItemDetails(item:String){
    return this.http.get<Item>(environment.apiUrl+"/items/"+item);
  }

  searchItemPrice(itemFilter:ItemFilter){
    return this.http.post<HistoricComparePrice[]>(environment.apiUrl+"/search",itemFilter);
  }
}
