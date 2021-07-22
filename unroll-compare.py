#! /usr/bin/env python
import argparse
import csv


def main():
    p = argparse.ArgumentParser()
    p.add_argument('max_cont_csv', help='output of sourmash compare --max-containment')
    p.add_argument('similarity_csv', help='output of sourmash compare --csv')
    p.add_argument('-o', '--output', required=True, help='output file')
    args = p.parse_args()

    mc_mat = {}
    with open(args.max_cont_csv, newline='') as infp:
        r = csv.reader(infp)
        headers = next(r)
        headers = [ h.split(' ')[0] for h in headers ]

        for h, row in zip(headers, r):
            for h2, col in zip(headers, row):
                col = float(col)
                if col > 0.0:
                    k = tuple(sorted([h, h2]))
                    mc_mat[k] = col


    sim_mat = {}
    with open(args.similarity_csv, newline='') as infp:
        r = csv.reader(infp)
        headers = next(r)
        headers = [ h.split(' ')[0] for h in headers ]

        for h, row in zip(headers, r):
            for h2, col in zip(headers, row):
                col = float(col)
                if col > 0.0:
                    k = tuple(sorted([h, h2]))
                    sim_mat[k] = col

    all_keys = set(mc_mat)
    all_keys.update(set(sim_mat))

    with open(args.output, 'w', newline="") as outfp:
        w = csv.writer(outfp)
        w.writerow(['g1', 'g2', 'similarity', 'max_containment'])
        for k in all_keys:
            sim = sim_mat.get(k, 0.0)
            max_cont = mc_mat.get(k, 0.0)

            w.writerow([k[0], k[1], sim, max_cont])

    print(f"wrote {len(all_keys)} entries to '{args.output}'")


if __name__ == '__main__':
    main()
