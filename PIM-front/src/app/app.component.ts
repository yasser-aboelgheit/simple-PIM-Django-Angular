import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'PIM-front';
  categories = [{name:"computer"},{name:"mobile"}];
  subcategories;
  cars = ["Saab", "Volvo", "BMW"];
  constructor(private api: ApiService) {
    this.getCategories();
  }
  getCategories = () => {
    this.api.getAllCategories().subscribe(
      data => {
        data[0].arg3=["ana","ana"]
          
        ;
        this.categories = data;
        // console.log(data);
        var i;
        for (i = 0; i < Object.keys(data).length; i++) {
          if(Object.keys(data[i]["subcategories"]).length!==0)
          {
          console.log(data[i]["subcategories"][i]["name"]);
          }    
        }
      },
      error => {
        console.log(error);
      }
    );
  }
  productClicked = (product) => {
    console.log(product.slug);
    console.log(product.subcategories);
    this.api.getOneCategory(product.slug).subscribe(
      data => {
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }

}
