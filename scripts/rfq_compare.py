#!/usr/bin/env python3
"""供应商报价加权对比。CSV 列：supplier, price, lead_days, quality(0-10), payment_days"""
import argparse, csv

def norm(vals, higher_better):
    lo, hi = min(vals), max(vals)
    if hi == lo: return [1.0] * len(vals)
    return [((v - lo) / (hi - lo)) if higher_better else ((hi - v) / (hi - lo)) for v in vals]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("csv")
    for k, d in (("price", 40), ("lead", 20), ("quality", 25), ("payment", 15)): ap.add_argument(f"--w-{k}", type=float, default=d)
    a = ap.parse_args()
    rows = list(csv.DictReader(open(a.csv, encoding="utf-8-sig")))
    col = lambda k: [float(r[k]) for r in rows]
    s = [norm(col("price"), False), norm(col("lead_days"), False), norm(col("quality"), True), norm(col("payment_days"), True)]
    w = [a.w_price, a.w_lead, a.w_quality, a.w_payment]; tw = sum(w)
    scored = sorted(((sum(w[i] * s[i][j] for i in range(4)) / tw * 100, r["supplier"]) for j, r in enumerate(rows)), reverse=True)
    print(f"权重 价格/交期/质量/账期 = {w}")
    for rank, (sc, sup) in enumerate(scored, 1): print(f"{rank}. {sup:<20} {sc:6.1f}")

if __name__ == "__main__":
    main()
