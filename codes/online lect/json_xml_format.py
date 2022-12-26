"""
JSON files are pure text files.
the basic format f jason file is shown under
{
  "fruit":"Apple",
  "size":"large",
  "color":"red"
}
"""
"""
fruit is name, and apple is value. JASON is a name-value pair file.

JSON format is used for serializing and transmitting structured data over network connection.
It is primarily used to transmit data between a server and web applications.
Web services and APIs use JSON format to provide public data. It can be used with modern programming languages.

if we want to mark a place, google maps API use marker for it in the format of JASON

{
    "markers": {
        {
            "name": "Rixos The Palm Dubai"
            "position": [25.1212, 55.1535]
        }
        {
            "name": "Shangri-La Hotel"
            "position": [534.1212, 55.1235]
        }
        {
            "name": "Grand Hyatt"
            "position": [25.1343, 21.1535]
        }
    }
}


xml are pure txt files and are used to describe data

p01,20,3,60
p02,30,5,150

p01,20,3,60 = <ProductCode>p01</ProductCode>,<UnitPrice>20</UnitPrice>,<Qty>3</Qty>,<Amount>60</Amount>


<InTheShelf>
<product>
<ProductCode>p01</ProductCode>,<UnitPrice>20</UnitPrice>,<Qty>3</Qty>,<Amount>60</Amount>
</product>

<product>
<ProductCode>p02</ProductCode>,<UnitPrice>30</UnitPrice>,<Qty>5</Qty>,<Amount>150</Amount>
</product>
</InTheShelf>


"""