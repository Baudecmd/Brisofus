import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {RouterModule, Routes} from "@angular/router";
import {ItemsComponent} from "../items/items.component";
import { ItemDetailsComponent } from '../item-details/item-details.component';
import { BreakingsComponent } from '../breakings/breakings.component';


const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'items', component: ItemsComponent },
  { path: 'item/:name', component: ItemDetailsComponent },
  { path: 'breakings', component: BreakingsComponent },


];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
