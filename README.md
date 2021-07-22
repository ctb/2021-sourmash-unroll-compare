# Unroll sourmash compare matrices

## quickstart

```
sourmash compare <signatures> --max-containment --csv max_cont.csv
sourmash compare <signatures> --csv sim.csv
./unroll-compare.py max_cont.csv sim.csv -o pairs.csv
```
will produce a file that contains all pairs with non-zero max containment
(along with their similarities), taken from the compare matrices:
```
g1,g2,similarity,max_containment
CP000667.1,NZ_CP015081.1,0.00011970313622216902,0.0003074085459575776
AE015928.1,CP000139.1,0.0040110526784918445,0.009
CP000561.1,CP000561.1,1.0,1.0
AE006470.1,NZ_KQ961402.1,0.0002304147465437788,0.0004610419548178884
CP000660.1,CP000660.1,1.0,1.0
```
