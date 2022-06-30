import { Injectable } from '@angular/core';
import HistoricComparePrice from './models/HistoricComparePrice';
import ItemFilter from './models/ItemFilter';
import ItemPrice from './models/ItemPrice';

@Injectable({
  providedIn: 'root'
})
export class SearchItemService {

  itemFilter:ItemFilter=new ItemFilter();

  itemPriceList:HistoricComparePrice[]=[];

  constructor() { }
}
