import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import HistoricPrice from './models/HistoricPrice';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class HistoricPriceServiceService {

  constructor(private http: HttpClient) { }

  getHistoricPrice(itemName:String){
    console.log(environment.apiUrl+"/priceCraftItem/name/"+itemName)
    return this.http.get<HistoricPrice[]>(environment.apiUrl+"/priceCraftItem/name/"+itemName);
  }

  getHistoricPriceHDV(itemName:String){
    return this.http.get<HistoricPrice[]>(environment.apiUrl+"/priceSellItem/"+itemName);
  }
}
