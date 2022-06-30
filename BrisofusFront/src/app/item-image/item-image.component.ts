import { Component, Input, OnInit } from '@angular/core';
import Item from '../models/Item';

@Component({
  selector: 'app-item-image',
  templateUrl: './item-image.component.html',
  styleUrls: ['./item-image.component.css']
})
export class ItemImageComponent implements OnInit {

  @Input()
  item:Item=new Item();
  @Input()
  width:number=0;

  constructor() { }

  ngOnInit(): void {
  }

}
