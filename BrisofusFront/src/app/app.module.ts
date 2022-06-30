import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import {RouterModule} from "@angular/router";
import { AppRoutingModule } from './app-routing/app-routing.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LogoComponent } from './logo/logo.component';
import { ItemsComponent } from './items/items.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { ItemDetailsComponent } from './item-details/item-details.component';
import { AppbarComponent } from './appbar/appbar.component';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { ItemImageComponent } from './item-image/item-image.component';
import {MultiSelectModule} from 'primeng/multiselect';
import {InputTextModule} from 'primeng/inputtext';
import {ButtonModule} from 'primeng/button';
import {CardModule} from 'primeng/card';
import { TableModule } from 'primeng/table';
import {MenubarModule} from 'primeng/menubar';
import {SkeletonModule} from 'primeng/skeleton';
import { GraphHistoricPriceComponent } from './graph-historic-price/graph-historic-price.component';
import { BreakingsComponent } from './breakings/breakings.component';
@NgModule({
  declarations: [
    AppComponent,
    LogoComponent,
    ItemsComponent,
    ItemDetailsComponent,
    AppbarComponent,
    ItemImageComponent,
    GraphHistoricPriceComponent,
    BreakingsComponent
  ],
  imports: [
    BrowserModule,
    RouterModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    NgxChartsModule,
    MultiSelectModule,
    InputTextModule,
    ButtonModule,
    CardModule,
    TableModule,
    MenubarModule,
    SkeletonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
