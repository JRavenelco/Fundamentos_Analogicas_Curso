#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera graficas de resultados de LTspice para los decks de Fundamentos Analogicas."""
import math, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

NAVY = (23/255, 54/255, 93/255)
GOLD = (179/255, 142/255, 62/255)
INK  = (44/255, 51/255, 58/255)
GRID = "#D7DDE3"

OUT = "figs"
os.makedirs(OUT, exist_ok=True)

def parse_raw(path):
    with open(path, "r", encoding="latin-1") as f:
        txt = f.read()
    nvar = npts = None
    names = []
    in_vars = False
    vals_start = None
    lines = txt.splitlines()
    for i, ln in enumerate(lines):
        if ln.startswith("No. Variables:"):
            nvar = int(ln.split(":")[1].strip())
        elif ln.startswith("No. Points:"):
            npts = int(ln.split(":")[1].strip())
        elif ln.strip() == "Variables:":
            in_vars = True
        elif in_vars:
            s = ln.strip()
            if not s:
                continue
            if s.startswith("Values:"):
                in_vars = False
                vals_start = i
                break
            # formato: idx name type  -> name es col 1
            parts = s.split()
            names.append(parts[1])
    # recoger tokens tras "Values:"
    rest = "\n".join(lines[vals_start+1:])
    toks = rest.replace(",", " ").split()
    # cada punto: idx + nvar valores
    points = []
    k = 0
    while k + 1 + nvar <= len(toks):
        idx = int(toks[k])
        vals = toks[k+1:k+1+nvar]
        points.append([float(v) for v in vals])
        k += 1 + nvar
    return names, points

def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), dpi=130)
    plt.close(fig)
    print("generada", name)

def style(ax):
    ax.grid(True, color=GRID, lw=0.6)
    ax.set_axisbelow(True)
    for sp in ax.spines.values():
        sp.set_color(INK)

# ---------- S2.1: divisor cargado (Vout y error vs RL) ----------
def s21():
    names, pts = parse_raw("../../Simulaciones Ltspice/sim/semana2_01_divisor_cargado.raw")
    idx = {n:i for i,n in enumerate(names)}
    x = [p[idx['rl']]/1000 for p in pts]              # kOhm
    vout = [p[idx['V(vout)']] for p in pts]
    err = [100*(v-2.5)/2.5 for v in vout]
    fig, ax = plt.subplots()
    ax.loglog(x, vout, "o-", color=NAVY, lw=2, ms=6, label="V$_{out}$")
    ax.axhline(2.5, color=GOLD, ls="--", lw=1.4, label="ideal 2.5 V")
    ax.set_xlabel("R$_L$ (k$\\Omega$)")
    ax.set_ylabel("V$_{out}$ (V)")
    ax.set_title("S2.1 · Divisor cargado: efecto de la carga", color=NAVY)
    style(ax); ax.legend()
    save(fig, "s21_divisor_cargado.png")

# ---------- S2.2: tolerancia del divisor (4 casos) ----------
def s22():
    names, pts = parse_raw("../../Simulaciones Ltspice/sim/semana2_02_divisor_tolerancia.raw")
    idx = {n:i for i,n in enumerate(names)}
    vout = [p[idx['V(vout)']] for p in pts]
    err = [100*(v-2.5)/2.5 for v in vout]
    fig, ax = plt.subplots()
    ax.bar(range(4), err, color=NAVY, width=0.6)
    ax.axhline(0, color=INK, lw=1)
    ax.axhline(1, color=GOLD, ls="--", lw=1.2); ax.axhline(-1, color=GOLD, ls="--", lw=1.2)
    ax.set_xticks(range(4)); ax.set_xticklabels(["Caso 0\n$-$/$-$","Caso 1\n$-$/$+$","Caso 2\n$+$/$-$","Caso 3\n$+$/$+$"])
    ax.set_ylabel("Error (%)")
    ax.set_title("S2.2 · Tolerancia: error vs combinación", color=NAVY)
    style(ax)
    save(fig, "s22_tolerancia.png")

# ---------- S2.3: puente (Vdiff vs delta) ----------
def s23():
    names, pts = parse_raw("../../Simulaciones Ltspice/sim/semana2_03_wheatstone_desbalance.raw")
    idx = {n:i for i,n in enumerate(names)}
    d = [100*p[idx['delta']] for p in pts]             # en %
    vd = [(p[idx['V(left)']]-p[idx['V(right)']])*1000 for p in pts]  # mV
    fig, ax = plt.subplots()
    ax.plot(d, vd, "-", color=NAVY, lw=2, label="exacto")
    ax.plot(d, [-12.5*dd for dd in d], "--", color=GOLD, lw=1.6, label="aprox. $V_{exc}/4$")
    ax.axhline(0, color=INK, lw=1)
    ax.set_xlabel("$\\Delta$ (%)")
    ax.set_ylabel("V$_{diff}$ (mV)")
    ax.set_title("S2.3 · Puente de Wheatstone: linealidad", color=NAVY)
    style(ax); ax.legend()
    save(fig, "s23_puente.png")

# ---------- S2.4: equivalencia red vs Thevenin ----------
def s24():
    names, pts = parse_raw("../../Simulaciones Ltspice/sim/semana2_04_thevenin_sensor.raw")
    idx = {n:i for i,n in enumerate(names)}
    x = [p[idx['rl']]/1000 for p in pts]
    vo = [p[idx['V(original)']] for p in pts]
    ve = [p[idx['V(equivalent)']] for p in pts]
    fig, ax = plt.subplots()
    ax.semilogx(x, vo, "o-", color=NAVY, lw=2, ms=6, label="red original")
    ax.semilogx(x, ve, "s--", color=GOLD, lw=2, ms=6, label="equivalente Thévenin")
    ax.axhline(2.5, color=INK, ls=":", lw=1)
    ax.set_xlabel("R$_L$ (k$\\Omega$)")
    ax.set_ylabel("V$_{out}$ (V)")
    ax.set_title("S2.4 · Red original y equivalente coinciden", color=NAVY)
    style(ax); ax.legend()
    save(fig, "s24_thevenin.png")

# ---------- S1.4: potencia vs V con limite de derating ----------
def s14():
    names, pts = parse_raw("../../Simulaciones Ltspice/sim/semana1_04_potencia_derating.raw")
    idx = {n:i for i,n in enumerate(names)}
    v = [p[idx['V(vin)']] for p in pts]
    # potencia en el resistor: P = V^2/R con R=1k ; o usar I(V1)*V(vin)
    p = [p[idx['V(vin)']]*(p[idx['I(V1)']]) for p in pts]  # W (neg? use abs)
    p = [abs(pp) for pp in p]
    fig, ax = plt.subplots()
    ax.plot(v, [pp*1000 for pp in p], "-", color=NAVY, lw=2)
    ax.axhline(125, color=GOLD, ls="--", lw=1.5, label="límite derating 125 mW")
    ax.axvline(11.18, color=GOLD, ls=":", lw=1.5, label="$V_{lim}$ = 11.18 V")
    ax.set_xlabel("V$_{in}$ (V)")
    ax.set_ylabel("P (mW)")
    ax.set_title("S1.4 · Potencia y límite de derating", color=NAVY)
    style(ax); ax.legend()
    save(fig, "s14_derating.png")

# ---------- S1.5: fuente real (Vbus vs RL) ----------
def s15():
    names, pts = parse_raw("../../Simulaciones Ltspice/sim/semana1_05_fuente_y_falla.raw")
    idx = {n:i for i,n in enumerate(names)}
    # Vcontrol 0..3 (log): RL = 10^Vcontrol ; V(bus)
    vc = [p[idx['V(control)']] for p in pts]
    rl = [10**x for x in vc]
    vbus = [p[idx['V(bus)']] for p in pts]
    fig, ax = plt.subplots()
    ax.semilogx(rl, vbus, "o-", color=NAVY, lw=2, ms=5)
    ax.axhline(12, color=GOLD, ls="--", lw=1.4, label="$V_{ideal}$ = 12 V")
    ax.set_xlabel("R$_L$ ($\\Omega$)")
    ax.set_ylabel("V$_{bus}$ (V)")
    ax.set_title("S1.5 · Fuente real: el bus se hunde con la carga", color=NAVY)
    style(ax); ax.legend()
    save(fig, "s15_fuente_real.png")

# ---------- S1.6: potenciometro (cargado vs sin carga vs alpha) ----------
def s16():
    names, pts = parse_raw("../../Simulaciones Ltspice/sim/semana1_06_divisor_cargado.raw")
    idx = {n:i for i,n in enumerate(names)}
    a = [100*p[idx['valpha']] for p in pts]
    vu = [p[idx['V(vout_u)']] for p in pts]
    vl = [p[idx['V(vout_l)']] for p in pts]
    fig, ax = plt.subplots()
    ax.plot(a, vu, "-", color=GOLD, lw=2, label="sin carga (ideal)")
    ax.plot(a, vl, "-", color=NAVY, lw=2, label="con carga 10 k$\\Omega$")
    ax.set_xlabel("posición del cursor $\\alpha$ (%)")
    ax.set_ylabel("V$_{out}$ (V)")
    ax.set_title("S1.6 · Potenciómetro: efecto de carga", color=NAVY)
    style(ax); ax.legend()
    save(fig, "s16_pot.png")

for fn in (s21, s22, s23, s24, s14, s15, s16):
    try:
        fn()
    except Exception as e:
        print("ERROR en", fn.__name__, "->", e)
