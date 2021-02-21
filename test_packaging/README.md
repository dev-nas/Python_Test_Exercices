# PACKAGE analyseur de text

## structure

    1. la classe Gen génère un texte random

    2. la classe Clean nettoie le texte

    3. la classe Order renvoie un dictionnaire des occurences du texte


## utilisation

    * exemple script

    ```python
    
    from txt_analyser import Gen, Clean, Order

    g = Gen()
    c = Clean(g.generate())
    o = Order(c.process())
    print(o.getOccurences(20))

    ```