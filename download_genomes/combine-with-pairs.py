#! /usr/bin/env python
import sys
import csv
import argparse
import os


def main():
    p = argparse.ArgumentParser()
    p.add_argument('pairs_csv')
    p.add_argument('fastani_out')
    p.add_argument('-o', '--output', required=True)
    args = p.parse_args()

    pairs_d = {}
    with open(args.pairs_csv, newline="") as fp:
        r = csv.DictReader(fp)
        for row in r:
            g1 = row['g1']
            g2 = row['g2']
            sim = float(row['similarity'])
            max_cont = float(row['max_containment'])

            assert g1 <= g2
            pairs_d[(g1,g2)] = (sim, max_cont)

    ani_d = {}
    with open(args.fastani_out, newline="") as fp:
        r = csv.reader(fp, delimiter='\t')
        for row in r:
            acc1 = os.path.basename(row[0])
            acc1 = '_'.join(acc1.split('_')[:2])
            
            acc2 = os.path.basename(row[1])
            acc2 = '_'.join(acc2.split('_')[:2])

            ani = float(row[2]) / 100

            acc1, acc2 = sorted([acc1, acc2])
            key = (acc1, acc2)

            assert key in pairs_d
            ani_d[key] = ani

    with open(args.output, 'w', newline="") as fp:
        n_written = 0
        w = csv.writer(fp)
        w.writerow(['g1', 'g2', 'similarity', 'max_containment', 'ani'])

        for (g1, g2), ani in ani_d.items():
            sim, max_cont = pairs_d[(g1, g2)]
            w.writerow([g1, g2, sim, max_cont, ani])
            n_written += 1

    print(f"wrote {n_written} rows", file=sys.stderr)
            

if __name__ == '__main__':
    main()
