# Clothing detection ecommerce dataset

I have created a dataset with more than 80k images from ecommerce websites:

- "dataset.zip" (https://mega.nz/#!op4ADSRQ!af4skXn2jEEkOOWRrwAQi47OM_wIa0ZpKGJ5u8WjY9E), where you can find all the images.


## Getting Started

The images have been classified by category in folders, here I list all the categories:

```
['camisetas',      
 'planos',
 'petos',
 'bodies',
 'guantes',
 'botas',
 'carteras',
 'monos',
 'jerseys',
 'camisas',
 'zapatos',
 'calcetines',
 'corbatas',
 'sombreros',
 'gafas',
 'banadores',
 'trajes',
 'medias',
 'bufandas',
 'jeans',
 'tacones',
 'chanclas',
 'pantalones',
 'paraguas',
 'camiseta-interior',
 'sujetadores',
 'pijamas',
 'braguitas',
 'polos',
 'sudaderas',
 'vestidos',
 'gorros',
 'camisones',
 'bolsos-y-mochilas',
 'panuelos',
 'shorts',
 'reloj',
 'cardigans',
 'botines',
 'bisuteria',
 'abrigos',
 'bikinis',
 'faldas',
 'alpargatas',
 'cinturones',
 'camisas-y-blusas',
 'lenceria',
 'gorras',
 'zapatillas',
 'calzoncillos',
 'sandalias']
```

All images have been automatically annotate, you can find all the annotations in the file 'annotation.zip'.

### Example

In preview_annotation.py there is an example code to preview the annotations, you can go to next picture with key 'n', go back with key 'b', remove the image from the folder with key 'r' and quit with key 'q'.

```
python preview_annotation.py -d dataset/camisetas/ -a annotations
```

![alt text](https://github.com/seralexger/clothing-detection-ecommerce-dataset/blob/master/resources/clothe.gif)


### Annotation JSON scheme example

```
{
  "arr_boxes": [
    {
      "coor_center": [
        0.618742361664772,
        0.9013392329216003
      ],
      "coor1": [
        0.3926389515399933,
        0.8026784658432007
      ],
      "coor2": [
        0.8448457717895508,
        1
      ],
      "x": 661.9892722964287,
      "y": 2029.9738401174545,
      "width": 762.4206989407539,
      "height": 499.02615988254547,
      "gender": "male",
      "class": "trousers"
    },
    {
      "coor_center": [
        0.61893330514431,
        0.49360528588294983
      ],
      "coor1": [
        0.25417014956474304,
        0.14857351779937744
      ],
      "coor2": [
        0.983696460723877,
        0.8386370539665222
      ],
      "x": 428.53087216615677,
      "y": 375.74242651462555,
      "width": 1229.9813606142998,
      "height": 1745.1706829667091,
      "gender": "male",
      "class": "coats"
    }
  ],
  "file_name": "dataset/abrigos/1.jpg"
}
```

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7WYS86C54HFSE&source=url)
