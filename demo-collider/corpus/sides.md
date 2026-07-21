# Section → side map

The demonstration splits the safety case into three **argument-type sides** (not one paper per side — the point is that theory and bounds arguments coexist *within* the same documents, written in different vocabularies). Each side file under `_work/` (gitignored) is assembled by [`build_sides.sh`](build_sides.sh) from cleaned prose slices; every slice carries an inline `===== [source · section] =====` provenance tag. Sizes: side A ≈ 3.2k words, side B ≈ 4.1k, side C ≈ 6.2k — all under the scan detector's 18k-word cap (full input, no downsampling).

## Side A — theory (production, Hawking/decay, accretion *mechanism*)

| Source | Section | What it contributes |
|---|---|---|
| Giddings & Mangano 2008 | §2.1 Instability of microscopic black holes | Hawking evaporation, black-hole thermodynamics, transplanckian modes |
| Giddings & Mangano 2008 | §4.1 Accretion basics | capture radius, mass flux, the growth equation |
| Giddings & Mangano 2008 | §4.3 Macroscopic (Bondi) accretion in Earth | Bondi accretion, the growth-timescale model |
| Giddings & Mangano 2008 | §4.5 An Eddington limit? | whether radiation caps the accretion rate |
| Giddings & Mangano 2008 | §5.1–5.2 Production kinematics; stopping of neutral black holes | how a cosmic-ray-produced BH is created and slowed |

## Side B — astrophysical bounds (cosmic-ray survival, white dwarfs, neutron stars)

| Source | Section | What it contributes |
|---|---|---|
| LHC Safety Assessment Group 2008 | §2 LHC compared with cosmic-ray collisions | the reader-facing cosmic-ray-survival argument (residual OCR) |
| Giddings & Mangano 2008 | §2.2 Cosmic ray collisions on Earth | why Earth's survival alone is insufficient for stable BHs |
| Giddings & Mangano 2008 | §7.2 Bondi accretion (white dwarf) | the WD bound, computed from **Bondi accretion timescales** vs WD lifetimes |
| Giddings & Mangano 2008 | §7.4 Summary of white dwarf constraints | the WD survival bound stated as a reassurance |
| Giddings & Mangano 2008 | §8.2 Catalysis of neutron star decay | the NS survival bound |

## Side C — critique (physics objection + methodology)

| Source | Section | What it contributes |
|---|---|---|
| Plaga 2009 (v3) | §2–4 metastable mBH / Eddington-limit Hawking risk / white-dwarf gap | the physics objection: a microcanonical metastable BH the bounds miss |
| Ord, Hillerbrand & Sandberg 2010 | §2 Probability estimates; the chance an argument is flawed | P(argument flawed) dominates tiny risk estimates |
| Ord, Hillerbrand & Sandberg 2010 | §4 Applying the analysis to particle-physics risks | the cosmic-ray argument and the LHC safety case as worked examples |

## The dependence the split is designed to expose

Side A's **§4 accretion mechanism** and side B's **§7 white-dwarf bound** read as two different reassurances in two vocabularies — a theoretical growth-law versus an observational survival bound. But §7.2 *is* the §4 Bondi-accretion timescale evaluated at white-dwarf density and compared to observed white-dwarf lifetimes. They share the **Bondi-accretion premise**; they are not independent. Side C (Plaga §4) attacks exactly that premise. This is the cross-side matching cell (component 3).
