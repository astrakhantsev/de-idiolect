## `accretion slow-down` — flagged 20260721T013948Z (trigger: collider-demo)

- Source files: demo-collider/corpus/_work/sideA-prose.md
- Excerpts: 1 paragraphs, 129 words; prompt sha256 `a2709d7099c09ad59ffce5c223a245d92f56332716f8484b5b95d82f828ddf1d`
- **Every candidate below is UNVERIFIED**: a model-proposed name, not a checked mapping. The failure record this tool comes from includes *fabricated owners* — the next step is always to open one primary source per candidate you intend to rely on.

### Draw: sonnet (status: ok, 38s; manifest: /mnt/f/src/de-idiolect/demo-collider/term-check/.term-check/manifests/20260721T013948Z-accretion-slow-down-sonnet.txt)

## 1. Plain-language restatement
The term denotes momentum loss a body suffers by physically absorbing nearby matter into itself (thereby also gaining mass and possibly emitting radiation), as opposed to momentum loss from merely deflecting that matter at a distance without capturing it.

## 2. Closest existing terms of art

| Candidate | Field |
|---|---|
| Accretion drag (esp. Bondi–Hoyle–Lyttleton drag) | Astrophysics (compact-object dynamics) |
| Dynamical friction | Stellar dynamics / astrophysics |
| Variable-mass mechanics (mass-gain problem, Meshchersky-type equations) | Classical mechanics |
| Mass loading | Space/plasma physics |
| Accretion braking (of compact objects in gas/dark-matter media) | Astrophysics (PBH/compact-object literature) |

## 3. Oldest expected treatments

- **Accretion drag / Bondi–Hoyle–Lyttleton**: Hoyle & Lyttleton (1939); Bondi & Hoyle (1944), *MNRAS*; refined by Bondi (1952), *MNRAS*.
- **Dynamical friction**: Chandrasekhar (1943), *ApJ* — note this is normally the *gravitational-deflection* mechanism (what the excerpt itself calls "Coulomb slow-down"), not the accretion one.
- **Variable-mass mechanics**: Meshchersky (1897, doctoral thesis on bodies of variable mass); later treated by Levi-Civita and in classical-mechanics textbooks via the "growing raindrop" problem.
- **Mass loading**: Alfvén-era space plasma physics, ~1950s–60s, applied later to cometary/solar-wind ion pickup (e.g. papers from the 1980s on comet-solar-wind interaction).
- **Accretion braking of compact objects**: scattered through PBH/dark-matter halo dynamics literature, roughly 1970s–2000s (e.g. Ostriker 1999 generalizes Chandrasekhar's formula to include a gaseous accretion term).

## 4. Fit assessment

The closest match is **accretion drag** in the Bondi–Hoyle–Lyttleton sense: that literature already draws exactly this distinction — momentum loss from gravitational focusing/scattering of ambient matter (their "dynamical friction" term) versus momentum loss from matter actually captured onto the object (their "accretion" term) — which parallels the excerpt's Coulomb-slow-down/accretion-slow-down split closely.

What doesn't fit cleanly: the classic accretion-drag literature is built for a body moving through a continuous fluid/gas medium, computing a steady drag force from a flux of infalling matter. The excerpt's setting is a discrete two-body capture event (a black hole absorbing a single particle in a collision, with impact-parameter-dependent outcomes and possible radiation emission on capture) — closer to a quantized scattering/absorption cross-section problem than to fluid accretion. So the underlying physics (momentum removed via mass capture) is the same concept, but the excerpt is applying it in a particle-collision regime that the classical continuous-accretion formalism wasn't built for; it reads as a local coinage adapting "accretion drag" terminology to a discrete-particle/cosmic-ray-production context rather than a wholesale renaming of an existing single result.

### Draw: opus (status: ok, 44s; manifest: /mnt/f/src/de-idiolect/demo-collider/term-check/.term-check/manifests/20260721T013948Z-accretion-slow-down-opus.txt)

## 1. What the term denotes

The momentum loss (deceleration) a moving massive body suffers because it *captures and absorbs* the particles it runs into: each swallowed particle adds its mass to the body but carries away net forward momentum relative to the body's motion, so the enlarged body moves slower. It is the drag contribution from direct capture, as distinct from the drag from merely deflecting particles that are *not* captured (which the same document calls "Coulomb slow-down").

## 2. Established terms of art (closest first)

1. **Accretion drag / Bondi–Hoyle–Lyttleton (BHL) drag** — astrophysics / accretion theory. The drag on a compact object moving through a medium, arising from the momentum of the material it accretes within its capture radius. This is the direct match.
2. **Variable-mass ("sweep-up") dynamics; the growing-raindrop / Meshchersky problem** — classical mechanics. A body that accretes mass as it moves and decelerates to conserve momentum.
3. **Snowplow (momentum-conserving) phase** — astrophysics of supernova remnants / blast waves. A shell slows as it sweeps up and incorporates ambient mass.
4. **Ram-pressure / geometric-capture drag** — plasma & interstellar-medium physics. Deceleration set by the flux of mass intercepted by a physical (here, gravitational) capture cross-section.
5. **Dynamical friction** — stellar dynamics / plasma kinetics — listed only to *exclude* it: this is the scattering-without-capture channel, i.e. the document's "Coulomb slow-down," not "accretion slow-down."

## 3. Oldest / classic treatments

- **Accretion drag (BHL):** Hoyle & Lyttleton (1939, *Proc. Camb. Phil. Soc.*); Bondi & Hoyle (1944, *MNRAS*); Bondi (1952). Later standard: Edgar's review (2004).
- **Variable-mass / raindrop:** Meshchersky (1897); the falling-raindrop problem appears throughout early-20th-century mechanics texts (e.g. Lamb, Whittaker); Tsiolkovsky (1903) for the rocket-equation lineage.
- **Snowplow phase:** Oort (1951); Sedov (1959); Cox (1972); McKee & Ostriker (1977).
- **Ram-pressure:** Gunn & Gott (1972) for the interstellar/galactic ram-pressure formulation.
- **Dynamical friction (the excluded neighbor):** Chandrasekhar (1943, *ApJ*) — matches their "Coulomb slow-down," named by analogy to Coulomb scattering.

## 4. Fit of the best candidate, and what doesn't fit

**Accretion drag (BHL)** covers the concept well: a body moving through a particle background loses momentum to the material it captures, gaining mass in the process — exactly the mechanism described. The document's own pairing (scattering channel = dynamical friction/"Coulomb," capture channel = "accretion") reproduces the standard split between deflection drag and accretion drag, so "accretion slow-down" is essentially a rebranding of accretion drag.

What does not cleanly fit the classic candidate:
- **Collisionless, per-particle capture rather than hydrodynamic gas.** Canonical BHL is a fluid/gas treatment with a pressure and sound speed. Here the medium is discrete particles (cosmic-ray context) interacting *only gravitationally*, so the relevant object is a gravitational *capture cross-section* for individual quanta, closer to kinetic-theory / geometric-capture drag than to the Bondi gas formulae.
- **Relativistic mass–energy bookkeeping.** The clause "possibly emitting some radiation, and typically increasing its mass" implies a full energy–momentum balance (absorbed energy, radiated losses) that the Newtonian BHL and raindrop treatments don't carry.

Neither gap changes the identification — the concept is *accretion drag* — they just mark that the usage sits in a collisionless, relativistic regime where you'd compute the capture cross-section from geodesics rather than from Bondi's gas formulae.

Nothing in the excerpt is underdetermined for naming purposes; the one thing left unspecified is the *medium's* nature (are these the cosmic-ray particles themselves, or an ambient background?), which would decide whether the ram-pressure/capture-cross-section framing or the gas BHL framing is the more precise reference.

## `macroscopic absorption` — flagged 20260721T014110Z (trigger: collider-demo)

- Source files: demo-collider/corpus/_work/sideB-prose.md
- Excerpts: 1 paragraphs, 61 words; prompt sha256 `ac27410a58630c13fb3b89b07d6ada7803679eb1862da4be991b38aa388179bc`
- **Every candidate below is UNVERIFIED**: a model-proposed name, not a checked mapping. The failure record this tool comes from includes *fabricated owners* — the next step is always to open one primary source per candidate you intend to rely on.

### Draw: sonnet (status: ok, 47s; manifest: /mnt/f/src/de-idiolect/demo-collider/term-check/.term-check/manifests/20260721T014110Z-macroscopic-absorption-sonnet.txt)

## 1. Plain-language restatement

The term marks a **crossover in how a small, localized absorber (here, a black hole embedded in dense matter) "sees" the material around it**: when the absorber's zone of influence is smaller than the typical spacing between the individual particles making up the medium, it interacts with them one at a time as discrete objects; when its zone of influence is larger than that spacing, the surrounding matter behaves for its purposes like a smooth, continuous substance rather than a collection of separate particles.

## 2. Closest existing terms of art

| Candidate | Field |
|---|---|
| Continuum vs. free-molecular flow (Knudsen-number regime) | Kinetic theory of gases / fluid dynamics |
| Hydrodynamic vs. collisionless (ballistic) accretion | Astrophysics (compact-object accretion, esp. primordial-black-hole capture in stars) |
| Coherent vs. incoherent scattering | Nuclear/particle physics, scattering theory |
| Homogenization / effective-medium approximation | Condensed matter physics, electromagnetism of composites |
| Discrete-particle vs. continuum limit (kinetic–hydrodynamic crossover) | Statistical mechanics |

## 3. Oldest expected treatments

- **Knudsen regime**: Martin Knudsen, ~1909, on gas flow through tubes at low pressure; conceptually anticipated in Maxwell's kinetic theory papers of the 1860s–70s.
- **Hydrodynamic vs. collisionless accretion**: Bondi's 1952 accretion paper is the classic root for the hydrodynamic side; the specific application to black holes swallowing neutron-star matter traces to early-2010s primordial-black-hole capture papers (e.g., work by Capela, Pani, and Olinto, ~2013), which explicitly compare a capture radius to the nucleon mean free path/spacing.
- **Coherent vs. incoherent scattering**: van Hove's 1954 correlation-function treatment of scattering is the classic general reference; for the nuclear case specifically, Freedman's 1974 paper on coherent neutrino–nucleus scattering.
- **Effective-medium theory**: Maxwell Garnett, 1904; Bruggeman, 1935; with roots in 19th-century Clausius–Mossotti/Lorentz–Lorenz work.
- **Kinetic–hydrodynamic crossover**: Boltzmann's kinetic equation (1870s) and its continuum reduction via Chapman–Enskog theory (~1916–17).

## 4. Fit assessment

The **hydrodynamic vs. collisionless accretion** distinction from the primordial-black-hole-in-neutron-star literature is the best match — it's the same physical system (a compact absorber, a capture/interaction radius, nucleon spacing as the discreteness scale) and the same qualitative question (does the absorber sample the medium as discrete nucleons or as a continuous fluid). The generic **Knudsen-number** framing captures the same logical structure (compare an absorber/interaction length to inter-particle spacing) but is a flow concept, not natively about absorption/capture, so it fits the physics but not the vocabulary.

What doesn't fully fit any candidate: this one paragraph doesn't tell us what "absorption" quantitatively means here — a capture cross-section, an accretion rate, an energy-loss rate — so I can't confirm whether the paper needs the *rate-calculation* apparatus of Bondi-type accretion theory or just the qualitative regime language. Also, the black hole itself (not an external probe) is the thing whose "radius of influence" sets the microscopic scale, which is a slightly different geometry than the Knudsen or effective-medium pictures, where the small-scale structure belongs to the medium alone. With only one excerpt, I can't tell whether "macroscopic absorption" is meant as this project's own name for the hydrodynamic-accretion regime specifically, or a broader placeholder covering several of the above; more surrounding text (e.g., how $R_D$, $R_C$ are defined) would resolve that.

### Draw: opus (status: ok, 59s; manifest: /mnt/f/src/de-idiolect/demo-collider/term-check/.term-check/manifests/20260721T014110Z-macroscopic-absorption-opus.txt)

## 1. What the term appears to denote

In context, it names the regime in which a small gravitating body embedded in dense matter swallows the surrounding material as a **continuous bulk medium** — capturing many constituent particles collectively, treated as a fluid — rather than picking off individual particles one at a time. The switch happens when the body's gravitational reach (its capture/influence radius) grows larger than the mean spacing between the medium's constituent particles (here, ~1 fm between nucleons); below that spacing the body sees discrete particles ("microscopic"), above it a smooth continuum ("macroscopic").

So the term is really shorthand for **"the continuum/fluid regime of gravitational accretion, as opposed to discrete particle-by-particle capture."**

## 2. Closest established terms of art

- **Bondi accretion / Bondi–Hoyle–Lyttleton accretion** — astrophysics & fluid dynamics. The continuum, hydrodynamic capture of gas onto a compact body; this is the standard name for the "macroscopic" side.
- **Continuum vs. free‑molecular (kinetic) flow, indexed by the Knudsen number** — kinetic theory / rarefied gas dynamics. This is the canonical framework for exactly the micro→macro crossover being invoked: continuum when the characteristic length ≫ particle mean free path/spacing, free-molecular (particle-by-particle) when ≪.
- **Collisional vs. collisionless accretion** — plasma astrophysics. Distinguishes fluid (hydrodynamic) capture from ballistic single-particle capture.
- **Breakdown of the continuum hypothesis** — continuum mechanics. The generic statement that a medium can be modeled as a field only above a granularity scale.
- **Gravitational (geometric) capture cross-section** — general relativity / celestial mechanics. Names the *microscopic* side (per-particle capture probability), against which "macroscopic" is contrasted.

## 3. Oldest / classic treatments

- **Bondi–Hoyle–Lyttleton:** Hoyle & Lyttleton (Proc. Camb. Phil. Soc., 1939); Bondi & Hoyle (MNRAS, 1944); Bondi, "On spherically symmetrical accretion" (MNRAS, 1952).
- **Knudsen number / rarefied-gas regimes:** Martin Knudsen's effusion/molecular-flow work (~1909); the kinetic-theory foundation from Maxwell and Boltzmann (1860s–1870s); Chapman & Cowling, *The Mathematical Theory of Non-Uniform Gases* (1939).
- **Continuum hypothesis in fluid mechanics:** standard in Lamb's *Hydrodynamics* (early 1900s) and later Batchelor's *An Introduction to Fluid Dynamics* (1967).
- **Gravitational capture cross-section:** classical geometric-capture treatments; textbook form in Zel'dovich & Novikov, *Relativistic Astrophysics / Stars and Relativity* (~1971).
- **Compact/DM object inside a neutron star (the specific setting):** the tradition around Goldman & Nussinov (Phys. Rev. D, 1989) and subsequent trapped-object/accretion-onto-endoparasitic-black-hole work through the 2010s. (I'd expect references of this kind; I'm not certain of the exact paper this document draws on, so I won't attribute specifics.)

## 4. How well covered, and what doesn't fit

The **best single match is Bondi(–Hoyle–Lyttleton) accretion** for the "macroscopic" regime itself, and the **Knudsen-number continuum/free-molecular dichotomy** for the crossover being described. Together these cover the core idea almost completely: it is the standard "does the object see a fluid or individual particles?" question, and mature vocabulary already exists for both sides and the transition.

What does not cleanly fit any candidate:

- **The crossover length is the inter-particle *spacing* (~1 fm), not a mean free path.** Standard Knudsen-number reasoning sets continuum breakdown by the mean free path between *collisions*, which in dense degenerate matter differs from the bare spacing. Using nucleon separation as the dividing scale is a nonstandard choice.
- **The medium is a degenerate, quantum, strongly-interacting fluid,** not a classical rarefied gas. The "microscopic" side is quantum/degenerate nucleon matter, so the Knudsen picture (built for classical gases) is only an analogy.
- **The governing length on the "macroscopic" side is gravitational** (a capture/Bondi radius) rather than a geometric obstacle size, so it's a gravitational-capture problem wearing a rarefied-gas-dynamics label.
- The paragraph also couples this to **dimensional-crossover radii $R_D$, $R_C$ ("lower-dimensional behavior")**, which is outside all of the candidates above and isn't determined by this excerpt.

Underdetermined from one paragraph: whether "macroscopic absorption" is meant to be literally Bondi accretion (with a defined accretion rate) or just the qualitative continuum limit, and what physically sets the body's "range of influence" (Bondi radius, tidal radius, or Schwarzschild radius). If the document defines that influence radius and an accretion rate, the identification with Bondi accretion would be firm; without it, only the continuum-vs-kinetic reading is certain.

## `crust penetration time` — flagged 20260721T014256Z (trigger: collider-demo)

- Source files: demo-collider/corpus/_work/sideB-prose.md
- Excerpts: 1 paragraphs, 44 words; prompt sha256 `be8fc23a5d188ac2b0e71a90d07f24b74b4d3abb747ca410840b3c080325aa90`
- **Every candidate below is UNVERIFIED**: a model-proposed name, not a checked mapping. The failure record this tool comes from includes *fabricated owners* — the next step is always to open one primary source per candidate you intend to rely on.

### Draw: sonnet (status: ok, 45s; manifest: /mnt/f/src/de-idiolect/demo-collider/term-check/.term-check/manifests/20260721T014256Z-crust-penetration-time-sonnet.txt)

**1. What the term denotes (plain language):**
The elapsed time for something undergoing repeated random scattering (a random walk, characterized by a shortest mean free path and a correspondingly reduced average speed) to work its way down through a bounding outer layer, where a steady downward pull adds a net directional drift on top of the random motion. The paragraph is deriving a lower bound on this time from the slowest point in the layer.

**2. Closest established terms of art:**
- **Diffusion time / radiative diffusion timescale** — stellar astrophysics (radiative transfer)
- **Gravitational settling time / diffusive settling** — stellar astrophysics (element stratification in stars, white dwarfs)
- **Thermalization time / capture-and-sink time** — astroparticle physics (dark matter capture in stars/compact objects)
- **First-passage time of a biased random walk (Kramers problem)** — statistical mechanics / stochastic processes
- **Drift-diffusion transit time** — semiconductor device physics

**3. Oldest expected treatments:**
- Diffusion time: Eddington, *The Internal Constitution of the Stars* (1926); Rosseland's opacity/diffusion-approximation work (1920s)
- Gravitational settling: Schatzman (1958) on diffusion in stellar envelopes; Burgers, *Flow Equations for Composite Gases* (1969) for the multi-species diffusion formalism later applied to settling
- Thermalization/capture time: Press & Spergel (1985) and Goldman & Nussinov (1989) on particle capture and thermalization in stars/neutron stars; this lineage is what later astroparticle papers on WIMP capture in compact objects build on
- First-passage/biased random walk: Kramers, "Brownian Motion in a Field of Force" (1940); underlying Brownian-motion math traces to Einstein (1905) and Smoluchowski
- Drift-diffusion transit time: Shockley-era semiconductor transport theory (1950s), itself built on the same Einstein/Smoluchowski drift-diffusion relation

**4. Coverage assessment:**
The mechanics described — mean free path setting a random-walk step, a velocity floor at the point of slowest transport, and a gravitational term added as a drift — is fully standard territory for the "gravitational settling time" / "thermalization time" family in stellar and astroparticle physics; the math (diffusion coefficient plus drift velocity, bounding the transit time by the worst-case point in the profile) is the same machinery used there. Given the femtometer-cubed density scale ($\rho = m_p/\mathrm{fm}^3$, i.e., nuclear density) and the word "crust," this reads specifically like a particle (possibly a WIMP or other exotic particle) working through a neutron-star crust toward the core — which would place it in the dark-matter-capture-in-neutron-stars literature rather than ordinary stellar settling.

What doesn't fully pin down to one term from the excerpt alone: I can't tell what is doing the penetrating (photon, neutron, dark-matter particle) or what "crust" physically is (neutron-star crust, planetary crust, or something else), and those choices are exactly what decides whether the field's own vocabulary would call this a "settling time," a "thermalization time," or a "diffusion time." The excerpt gives the physics but not the referent, so "crust penetration time" is very likely just this project's ad hoc label for a diffusion-with-drift transit time whose established name depends on that missing context.

### Draw: opus (status: ok, 57s; manifest: /mnt/f/src/de-idiolect/demo-collider/term-check/.term-check/manifests/20260721T014256Z-crust-penetration-time-opus.txt)

## 1. What the term appears to denote

The time for a body to travel all the way through a bounded material layer (here, the dense outer shell of a compact star) when its speed is not free but is capped by collisions with the medium: scattering sets a short mean free path, which limits the object to a slow terminal fall speed under gravity, and the traversal time is dominated by (and bounded from the slow-velocity extreme of) the region where scattering is densest.

In short: **a gravity-driven, drag-limited traversal (settling) time through a resisting slab.**

## 2. Established terms of art (closest first)

| Term of art | Field that owns it |
|---|---|
| **Gravitational settling / sedimentation time** (terminal-velocity–limited) | fluid dynamics, colloid science; stellar astrophysics (element diffusion/settling in stellar interiors and WD/NS envelopes) |
| **Terminal (drift) velocity; mobility-limited drift time** | transport physics; plasma & semiconductor transport (drift velocity = mobility × force) |
| **First-passage / mean transit time** under drift–diffusion | stochastic processes, statistical physics |
| **Diffusion (crossing) time** through a slab | neutron/radiative transport theory |
| **Stopping time / stopping range** of a body slowing in matter | nuclear & radiation physics |

## 3. Oldest / classic treatments you'd expect

- **Settling / terminal velocity:** Stokes (1851) on the drag on a sphere; the whole "Stokes settling velocity" lineage. For astrophysical settling/diffusion: Chapman & Cowling, *The Mathematical Theory of Non-Uniform Gases* (1939/1952); later Michaud (1970s) on stellar element diffusion.
- **Terminal drift / mobility:** kinetic-theory drift-velocity results running back through Chapman–Cowling and Langevin-era mobility theory (early 1900s).
- **First-passage / drift–diffusion:** Einstein (1905) and Smoluchowski (1906) on Brownian motion; Chandrasekhar, "Stochastic Problems in Physics and Astronomy" (1943); Kramers (1940) escape times; modern synthesis in Redner, *A Guide to First-Passage Processes* (2001).
- **Diffusion/crossing time:** classical neutron-diffusion and radiative-transport texts of the mid-20th century (e.g. random-walk photon/neutron escape-time arguments).
- **Stopping time/range:** Bohr (1913) and Bethe (1930s) stopping-power theory.

(Author/decade only, as requested; I have not manufactured exact citations.)

## 4. Fit of the best candidate, and residue

The best match is **gravitational settling / sedimentation time at terminal velocity** (equivalently, mobility-limited gravitational drift). The excerpt's exact logic — mean free path minimizes → drift velocity is set by gravity balanced against scattering drag → integrate/bound to get a traversal time — *is* the standard terminal-velocity settling calculation. Established fields cover this fully; the physics is not novel, only the name is.

Two things about the usage sit slightly outside the plain "sedimentation" label:

- **"Penetration" framing.** Sedimentation normally describes a native constituent settling within its own medium; "penetration" connotes a *foreign* intruder entering and crossing the slab from outside. That reframes the same drag-limited-drift math as an intrusion/traversal problem — but it adds no new mechanism, so it's still the same concept under a border-crossing name.
- **The bounding move.** The excerpt does not compute the settling time; it *bounds* it by evaluating at the slowest-velocity (minimum-mean-free-path) point. That's a worst-case estimate layered on top of the standard concept, not a distinct one.

**What the single paragraph underdetermines** (so I won't guess):
- **What is penetrating** — a microscopic particle, a macroscopic intruder (strangelet, dark-matter clump, primordial black hole), or a diffusing chemical species. This decides whether the right owner is stochastic first-passage (small particle, random walk) vs. deterministic terminal-velocity settling (macroscopic body).
- **Whether motion is deterministic drift or diffusive.** The chain "mean free path → velocity → time" reads as deterministic terminal drift, which would make the stochastic first-passage / diffusion-time candidates overkill — but the excerpt doesn't state the transport regime or the drag law, so I can't fix this from the text alone.

If you can supply the identity of the penetrating object and whether its transport is treated as drift or diffusion, the choice between "sedimentation/settling time" and "first-passage time" becomes determinate.

## `multiple bounds argument` — flagged 20260721T014438Z (trigger: collider-demo)

- Source files: demo-collider/corpus/_work/sideC-prose.md
- Excerpts: 1 paragraphs, 155 words; prompt sha256 `8db0eba514f15dcb6041b8f1155151b73d06fe4a4e8c8abea2f18b05ae81c8c9`
- **Every candidate below is UNVERIFIED**: a model-proposed name, not a checked mapping. The failure record this tool comes from includes *fabricated owners* — the next step is always to open one primary source per candidate you intend to rely on.

### Draw: sonnet (status: ok, 57s; manifest: /mnt/f/src/de-idiolect/demo-collider/term-check/.term-check/manifests/20260721T014438Z-multiple-bounds-argument-sonnet.txt)

**1. What the term denotes**

An argument structure for showing that some catastrophic outcome is acceptably improbable, built not from a single calculation but from several logically independent sub-arguments, each of which — if sound — would on its own suffice to rule out (or sharply limit) the danger. The sub-arguments are not just piled up for redundancy; here they're arranged so that a later one only needs to be invoked if an earlier one fails, i.e., a primary argument backed by a contingent fallback.

**2. Closest existing terms of art**

- **Robustness analysis / triangulation** — philosophy of science (esp. philosophy of biology/modeling)
- **Consilience of inductions / convergent evidence** — philosophy of science and epistemology
- **Defense in depth** — safety/systems engineering (esp. nuclear and process safety)
- **Weight-of-evidence / multiple lines of evidence** — environmental and ecological risk assessment
- **Independent argument legs in an assurance case** — safety-critical systems/software engineering (assurance case methodology)

**3. Oldest expected treatments**

- Robustness analysis: Richard Levins, *The Strategy of Model Building in Population Biology* (1966); William Wimsatt, "Robustness, Reliability, and Overdetermination" (1981)
- Consilience: William Whewell, *Philosophy of the Inductive Sciences* (1840); later formalized as "convergent validity" by Campbell & Fiske (1959, psychometrics)
- Defense in depth: mid-20th-century US nuclear reactor safety doctrine, canonically associated with the Rasmussen Report / WASH-1400 (1975), though the principle predates that report
- Weight of evidence: traceable informally to Austin Bradford Hill's causal criteria in epidemiology (1965); formalized in US EPA ecological/environmental risk assessment guidance from the 1990s–2000s
- Assurance-case argument legs: safety-critical engineering literature from the 1990s, e.g. Tim Kelly's work on Goal Structuring Notation, and Bloomfield & Rushby's later taxonomy of assurance-case argument types

**4. Fit of the best candidate, and the gap**

*Defense in depth* is the closest match in spirit: it's explicitly about bounding risk (not just building positive confidence) through layers, and — unlike consilience — its classic formulations already allow for layers that activate only when a prior layer fails, matching the "only if this understanding is flawed will the next section come into play" structure in the excerpt. *Robustness analysis* and *consilience* capture the "independent lines converging on the same conclusion" idea well but are normally used for positive claims (this result is real/robust), not adversarial risk-bounding, and they don't naturally encode a sequential primary/fallback ordering.

What doesn't fit cleanly anywhere: the excerpt shows only two sub-arguments (A1, A2) and a stated dependency between them (A2 is conditional on A1's failure), so it's ambiguous from this fragment alone whether the intended structure is (a) a genuinely parallel redundant set like defense-in-depth's independent barriers, or (b) a strictly hierarchical fallback chain, which is a narrower and less commonly named pattern in any of these fields — closer to a "primary argument plus contingency argument" than to the simultaneous, mutually reinforcing layers that defense-in-depth or consilience usually describe. A single paragraph isn't enough to tell whether later sub-arguments in the fuller document (A3, A4, etc.) are independent of each other or chained the same way, which would decide which established term ultimately fits best.

### Draw: opus (status: ok, 55s; manifest: /mnt/f/src/de-idiolect/demo-collider/term-check/.term-check/manifests/20260721T014438Z-multiple-bounds-argument-opus.txt)

## 1. What the term denotes

A conclusion (here, "the process is safe") is established not by one chain of reasoning but by several logically independent sub-arguments, *each of which would on its own be enough* to rule the bad outcome out — so the conclusion fails only if all of them fail together. The excerpt also adds an ordering: later sub-arguments are held in reserve and only become relevant if the earlier, more robust ones turn out to be wrong.

## 2. Established terms of art (closest first)

1. **Defense in depth** — safety / reliability engineering (esp. nuclear-reactor safety). Multiple independent barriers, any one of which suffices.
2. **Robustness / robustness analysis** — philosophy of science and mathematical modeling. A result trusted because it is derivable by several independent routes.
3. **Convergent argument** (as opposed to a *linked* argument) — informal logic / argumentation theory. Several independent premise-sets each supporting the same conclusion.
4. **Consilience of inductions** — philosophy of science / epistemology. Independent lines converging on one conclusion.
5. **Triangulation** — social-science methodology. Corroboration of a finding by methodologically independent measures.

(Adjacent but *not* the right fit: the **union bound / Boole's inequality** in probability bounds a *disjunction* of failures — the opposite combinator. The structure here is a conjunction of failures, i.e. reliability of a *parallel/redundant* system, whose failure probability is the product under independence.)

## 3. Oldest / classic treatments I'd expect

- **Defense in depth**: origin in military strategy; formalized for engineered systems via fault-tree analysis — H. Watson / Bell Labs on the Minuteman program (early 1960s) — and codified in U.S. reactor-safety practice (AEC/NRC, 1960s–70s). Foundational reliability-of-redundant-components result: **von Neumann**, "Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components" (1956).
- **Robustness**: **Richard Levins**, "The Strategy of Model Building in Population Biology" (1966); **William Wimsatt**, "Robustness, Reliability, and Overdetermination" (1981).
- **Convergent vs. linked arguments**: **Monroe Beardsley**, *Practical Logic* (1950); **Stephen Thomas**, *Practical Reasoning in Natural Language* (1970s).
- **Consilience of inductions**: **William Whewell**, *The Philosophy of the Inductive Sciences* (1840).
- **Triangulation**: **Campbell & Fiske**, multitrait–multimethod / convergent validation (1959); **Webb et al.**, *Unobtrusive Measures* (1966).

## 4. How well the best candidate covers it, and what doesn't fit

The safety-engineering flavor is captured best by **defense in depth**: independent barriers, each individually sufficient, so the system fails only on joint failure. The *epistemic* flavor — trusting a claim because it survives several independent derivations (A1 robust across "several different physical theories") — is exactly **robustness analysis**. The bare logical shape is a **convergent argument**.

What no single term of art cleanly bundles is the conjunction of three features present here:
- each sub-argument is independently **sufficient to bound the outcome**, not merely a piece of accumulating evidence (this rules out consilience/triangulation, which are about *confirming a positive fact* by convergence, not about upper-bounding a catastrophe);
- the sub-arguments are arranged as a **conditional cascade / ordered fallback** ("only if this understanding is flawed will the next section come into play") — a hierarchy of defeaters, which defense-in-depth's *parallel* barriers don't quite express;
- the target is an **upper bound on a disaster probability reached without ever stating a probability** — a qualitative bounding, unlike the quantitative redundancy calculus of reliability engineering.

Net: "multiple bounds argument" is a local coinage for what is essentially **defense in depth realized at the level of arguments rather than physical barriers**, shading into **robustness** on the epistemic side. That is a real and adequately-named concept; the only genuinely distinctive twist in this usage is the explicit *ranked-fallback* structure, for which the nearest vocabulary is **defeaters / defeasible reasoning** in argumentation theory rather than any of the convergence terms.

One caveat on determinacy: a single paragraph is thin. It's clear the sub-arguments are meant to be independent and individually sufficient, but the excerpt doesn't say whether the author treats their *combination* quantitatively (multiplying failure probabilities) or purely qualitatively — that distinction is what would decide between the reliability-engineering reading and the informal-logic reading.

