# CSV Combiner
pip install -r  requirements.txt 
for csv-combiner.py

csv-combiner.py should be able to handle larger files than csv-combinerSmaller.py
based off of my tests. csv-combinerSmaller can be used for smaller files and I 
believe can be more easily changed and itterated upon to meet diferent needs.

Input method to generate combined.csv from cmd can remove "> combined.csv" for output to cmd.
Use this from the cmd in csv-combiner directory for csv-combiner. Of course you can change the name of the csv file it will save to as well as the files being combined.
`python csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv`

Input method to generate combined.csv from cmd can remove "> combined.csv" for output to cmd.
Use this from the cmd in csv-combiner directory for csv-combinerSmaller. Of course you can change the name of the csv file it will save to as well as the files being combined.
`python csv-combinerSmaller.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv`


##  Considerations
* You should use coding best practices. Your code should be re-usable and extensible.
* Your code should be testable by a CI/CD process. 
* Unit tests should be included.

## Example
This example is provided as one of the ways your code should run. It should also be
able to handle more than two inputs, inputs with different columns, and very large (> 2GB) 
files gracefully.

```
$ ./csv-combiner.php ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv
```


