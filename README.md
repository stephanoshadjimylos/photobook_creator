## Photobook Creator

Welcome to the Photobook Creator! This program allows you to create a photobook (book where each page
is a collage of photos) given an input of photos. Each page of the photobook can be one of six modes.

### Modes

| Mode | Description |
| ------- | ----------- |
| 0 | A single square photo positioned in the center of the page |
| 1 | Two portrait photos. One positioned on the left & one on the right |
| 2 | Two landscape photos. One positioned on the top & one on the bottom |
| 3 | Four square photos positioned in the four quadrants of the page |
| 4 | One portrait photo on the left & one square photo on the right |
| 5 | One landscape photo positioned in the center of the page |


### Input Payload

| Parameter | Description |
| ------- | ----------- |
| `uri` | The path of the input image. Should be located in photos directory |
| `position` | The position of the photo on the page |
| `page` | The page of the photobook which the photo is to be placed |
| `mode` | Which mode the format of the page is |
| `colorTheme` | The background colour of the page |

#### Format

The entire payload should have format:

```
"page_data" = [
    {}
]
```
Where each dictionary object is one of the examples below.

#### Example - Mode 0
```
{
    
    "image": {
        "uri": "photos/horizontal_1.jpg",
    },
    "position": "center",
    "page": 0,
    "mode": 0,
    "colorTheme": "#FFFFFF"
}
```
#### Example - Mode 1
```
{
"image": {
    "uri": "photos/vertical_3.jpg",
},
"position": "left",
"page": 1,
"mode": 1,
"colorTheme": "#FFFFFF",
},
{
"image": {
    "uri": "photos/vertical_2.jpg",
},
"position": "right",
"page": 1,
"mode": 1,
"colorTheme": "#FFFFFF",
}
```
#### Example - Mode 2
```
{
"image": {
    "uri": "photos/horizontal_2.jpg",
},
"position": "top",
"page": 2,
"mode": 2,
"colorTheme": "#FFFFFF",
},
{
"image": {
    "uri": "photos/horizontal_3.jpg",
},
"position": "bottom",
"page": 2,
"mode": 2,
"colorTheme": "#FFFFFF",
}
```
#### Example - Mode 3
```
{
    "image": {
        "uri": "photos/square_1.jpg",
    },
    "position": "topLeft",
    "page": 3,
    "mode": 3,
    "colorTheme": "#FFFFFF",
},
{
    "image": {
        "uri": "photos/square_2.jpg",
    },
    "position": "topRight",
    "page": 3,
    "mode": 3,
    "colorTheme": "#FFFFFF",
},
{
    "image": {
        "uri": "photos/square_3.jpg",
    },
    "position": "bottomLeft",
    "page": 3,
    "mode": 3,
    "colorTheme": "#FFFFFF",
},
{
    "image": {
        "uri": "photos/square_4.jpg",
    },
    "position": "bottomRight",
    "page": 3,
    "mode": 3,
    "colorTheme": "#FFFFFF",
}
```
#### Example - Mode 4
```
{
"image": {
    "uri": "photos/vertical_3.jpg",
},
"position": "left",
"page": 4,
"mode": 4,
"colorTheme": "#FFFFFF",
},
{
"image": {
    "uri": "photos/square_2.jpg",
},
"position": "right",
"page": 4,
"mode": 4,
"colorTheme": "#FFFFFF",
}
```
#### Example - Mode 5
```
{
"image": {
    "uri": "photos/horizontal_1.jpg",
},
"position": "center",
"page": 5,
"mode": 5,
"colorTheme": "#FFFFFF",
}
```

### Steps to run

1. In the file payload.py place your payload
2. Create a virtual environment

In the root directory of the project run:
```
$ pip install -r requirements.txt
$ python photobook_creator.py
```

### Output

The output of the program should be a PDF file located in the path:
```
photos/final_photobook.pdf
```

### Running the Tests

In the root directory of the project run:
```
$ pytest -s
```