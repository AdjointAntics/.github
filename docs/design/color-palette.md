# Adjoint Ten — AdjointAntics Color Palette

An adjunction is not a symmetry. It's a directed relationship — one functor constructs, the other forgets. The palette encodes this asymmetry. Cyan dominates. Everything else recedes.

## Core

| Role | Name | Color | | Hex | Contrast on Void | Rationale |
|:--|:--|:--|:--|:--|:--|:--|
| Background | **Void** | Deep Indigo | ![](https://img.shields.io/badge/-%20-0C0E16?style=flat-square) | `#0C0E16` | — | The category. Contains everything, shows nothing. Almost all surface area is this. |
| Text | **Morphism** | Silver Arrow | ![](https://img.shields.io/badge/-%20-D4D4D4?style=flat-square) | `#D4D4D4` | 13.0:1 AAA | Arrows between objects. Not white — pure white is a statement. Text isn't making one. |
| Primary | **Left Adjoint** | Alien Cyan | ![](https://img.shields.io/badge/-%20-00FFCE?style=flat-square) | `#00FFCE` | 14.9:1 AAA | F. The free functor. Constructs, synthesizes, reaches forward. Used sparingly, which is why it works. |

## Accent

| Role | Name | Color | | Hex | Contrast on Void | Rationale |
|:--|:--|:--|:--|:--|:--|:--|
| Secondary | **Right Adjoint** | Forgetful Lilac | ![](https://img.shields.io/badge/-%20-AA78C8?style=flat-square) | `#AA78C8` | 5.7:1 AA | G. The forgetful functor. Evolved from Julia purple — the lineage is visible in the color space. |
| Error | **Unit** | Hot Rose | ![](https://img.shields.io/badge/-%20-FF3366?style=flat-square) | `#FF3366` | 5.4:1 AA | η: 1 → GF. The natural transformation that starts a round trip. Errors, breaking changes. If you see this, act. |
| Warning | **Comonad** | Electric Amber | ![](https://img.shields.io/badge/-%20-FFBE0B?style=flat-square) | `#FFBE0B` | 11.6:1 AAA | GF. Observes before it transforms. Warnings, highlights, deprecations — the things that ask you to notice before you decide. |
| Info | **Hom** | Frozen Neon | ![](https://img.shields.io/badge/-%20-4CB8E8?style=flat-square) | `#4CB8E8` | 8.6:1 AAA | Hom(A, B). The set of all morphisms between two objects. Structural, always present. Info states, focus rings — "you're here" without "look at me." |
| Success | **Isomorphism** | Cathode Green | ![](https://img.shields.io/badge/-%20-33DD66?style=flat-square) | `#33DD66` | 10.7:1 AAA | f where f⁻¹ exists. The strongest positive statement. Passing tests, verified states. Everything checks out. |

## Structure

| Role | Name | Color | | Hex | Contrast on Void | Rationale |
|:--|:--|:--|:--|:--|:--|:--|
| Surface | **Elevation** | Charcoal | ![](https://img.shields.io/badge/-%20-181B24?style=flat-square) | `#181B24` | — | Code blocks, cards, anything lifted off the void. The step is subtle — structure should be felt, not seen. |
| Border | **Counit** | Ash | ![](https://img.shields.io/badge/-%20-666666?style=flat-square) | `#666666` | 3.4:1 AA-lg | ε: FG → 1. The return. Borders, dividers, de-emphasized text. Organizes without competing. |

## Adjoint Ten

<p>
  <img src="https://img.shields.io/badge/Void-%20-0C0E16?style=flat-square&labelColor=0C0E16" alt="Void #0C0E16"/>
  <img src="https://img.shields.io/badge/Elevation-%20-181B24?style=flat-square&labelColor=0C0E16" alt="Elevation #181B24"/>
  <img src="https://img.shields.io/badge/Counit-%20-666666?style=flat-square&labelColor=0C0E16" alt="Counit #666666"/>
  <img src="https://img.shields.io/badge/Morphism-%20-D4D4D4?style=flat-square&labelColor=0C0E16" alt="Morphism #D4D4D4"/>
  <img src="https://img.shields.io/badge/Left_Adjoint-%20-00FFCE?style=flat-square&labelColor=0C0E16" alt="Left Adjoint #00FFCE"/>
  <img src="https://img.shields.io/badge/Right_Adjoint-%20-AA78C8?style=flat-square&labelColor=0C0E16" alt="Right Adjoint #AA78C8"/>
  <img src="https://img.shields.io/badge/Unit-%20-FF3366?style=flat-square&labelColor=0C0E16" alt="Unit #FF3366"/>
  <img src="https://img.shields.io/badge/Comonad-%20-FFBE0B?style=flat-square&labelColor=0C0E16" alt="Comonad #FFBE0B"/>
  <img src="https://img.shields.io/badge/Hom-%20-4CB8E8?style=flat-square&labelColor=0C0E16" alt="Hom #4CB8E8"/>
  <img src="https://img.shields.io/badge/Isomorphism-%20-33DD66?style=flat-square&labelColor=0C0E16" alt="Isomorphism #33DD66"/>
</p>

## Accessibility

WCAG 2.1 contrast ratios on both surfaces. Seven of eight colors exceed AA (4.5:1) on both Void and Elevation. Counit meets AA-large (3.0:1) — reserved for borders and muted large text. The *Minimum required* column is our internal standard: the threshold below which we reject a color change.

| Color | | Void | Elevation | Minimum required |
|:--|:--|:--|:--|:--|
| Left Adjoint | ![](https://img.shields.io/badge/-%20-00FFCE?style=flat-square) | 14.9:1 AAA | 13.3:1 AAA | AA — headings, accent |
| Morphism | ![](https://img.shields.io/badge/-%20-D4D4D4?style=flat-square) | 13.0:1 AAA | 11.6:1 AAA | AAA — body text |
| Comonad | ![](https://img.shields.io/badge/-%20-FFBE0B?style=flat-square) | 11.6:1 AAA | 10.3:1 AAA | AA — warnings |
| Isomorphism | ![](https://img.shields.io/badge/-%20-33DD66?style=flat-square) | 10.7:1 AAA | 9.6:1 AAA | AA — success states |
| Hom | ![](https://img.shields.io/badge/-%20-4CB8E8?style=flat-square) | 8.6:1 AAA | 7.6:1 AAA | AA — info, focus |
| Right Adjoint | ![](https://img.shields.io/badge/-%20-AA78C8?style=flat-square) | 5.7:1 AA | 5.1:1 AA | AA — links, labels |
| Unit | ![](https://img.shields.io/badge/-%20-FF3366?style=flat-square) | 5.4:1 AA | 4.8:1 AA | AA — alerts |
| Counit | ![](https://img.shields.io/badge/-%20-666666?style=flat-square) | 3.4:1 AA-lg | 3.0:1 AA-lg | AA-lg — muted text, borders |

**Never convey meaning through color alone.** Every color-coded element gets a paired signal: icon, underline, text label, or shape.

### Pairwise contrast

No two accent colors achieve 3:1 contrast against each other. The highest pair (Left Adjoint ↔ Unit, 2.7:1) still fails AA-large. Accent colors are legible on Void and Elevation, not on each other. This is structural — it enforces Rule 11 and prevents visual noise.

<details>
<summary>Full pairwise matrix (15 pairs)</summary>

&nbsp;

| Pair | Ratio |
|:--|:--|
| Left Adjoint ↔ Unit | 2.7:1 |
| Left Adjoint ↔ Right Adjoint | 2.6:1 |
| Unit ↔ Comonad | 2.1:1 |
| Unit ↔ Isomorphism | 2.0:1 |
| Right Adjoint ↔ Comonad | 2.0:1 |
| Right Adjoint ↔ Isomorphism | 1.9:1 |
| Left Adjoint ↔ Hom | 1.7:1 |
| Unit ↔ Hom | 1.6:1 |
| Right Adjoint ↔ Hom | 1.5:1 |
| Left Adjoint ↔ Isomorphism | 1.4:1 |
| Comonad ↔ Hom | 1.4:1 |
| Left Adjoint ↔ Comonad | 1.3:1 |
| Hom ↔ Isomorphism | 1.3:1 |
| Right Adjoint ↔ Unit | 1.1:1 |
| Comonad ↔ Isomorphism | 1.1:1 |

</details>

### Color vision deficiency

Simulated against protanopia, deuteranopia, and tritanopia using Viénot/Brettel matrices. All colors maintain WCAG compliance under every simulation. The worst drop is Unit under protanopia (5.4:1 → 3.7:1, AA → AA-large) — the ✕ icon carries the signal.

<details>
<summary><strong>Protanopia</strong> — no red cones (~1% of males)</summary>

&nbsp;

| Name | Original | Simulated | Ratio | Level |
|:--|:--|:--|:--|:--|
| Left Adjoint | ![](https://img.shields.io/badge/-%20-00FFCE?style=flat-square) `#00FFCE` | ![](https://img.shields.io/badge/-%20-F7EDCC?style=flat-square) `#F7EDCC` | 16.5:1 | AAA |
| Isomorphism | ![](https://img.shields.io/badge/-%20-33DD66?style=flat-square) `#33DD66` | ![](https://img.shields.io/badge/-%20-DFC95B?style=flat-square) `#DFC95B` | 11.6:1 | AAA |
| Comonad | ![](https://img.shields.io/badge/-%20-FFBE0B?style=flat-square) `#FFBE0B` | ![](https://img.shields.io/badge/-%20-D9BF00?style=flat-square) `#D9BF00` | 10.5:1 | AAA |
| Hom | ![](https://img.shields.io/badge/-%20-4CB8E8?style=flat-square) `#4CB8E8` | ![](https://img.shields.io/badge/-%20-A0B6EA?style=flat-square) `#A0B6EA` | 9.5:1 | AAA |
| Right Adjoint | ![](https://img.shields.io/badge/-%20-AA78C8?style=flat-square) `#AA78C8` | ![](https://img.shields.io/badge/-%20-6989CB?style=flat-square) `#6989CB` | 5.5:1 | AA |
| Unit | ![](https://img.shields.io/badge/-%20-FF3366?style=flat-square) `#FF3366` | ![](https://img.shields.io/badge/-%20-6F6D67?style=flat-square) `#6F6D67` | 3.7:1 | AA-lg |
| Counit | ![](https://img.shields.io/badge/-%20-666666?style=flat-square) `#666666` | ![](https://img.shields.io/badge/-%20-666666?style=flat-square) `#666666` | 3.4:1 | AA-lg |
| Morphism | ![](https://img.shields.io/badge/-%20-D4D4D4?style=flat-square) `#D4D4D4` | ![](https://img.shields.io/badge/-%20-D4D4D4?style=flat-square) `#D4D4D4` | 13.0:1 | AAA |

No confusable pairs. Unit (rose → gray) loses chromatic punch but the ✕ icon carries the signal.

</details>

<details>
<summary><strong>Deuteranopia</strong> — no green cones (~1% of males)</summary>

&nbsp;

| Name | Original | Simulated | Ratio | Level |
|:--|:--|:--|:--|:--|
| Left Adjoint | ![](https://img.shields.io/badge/-%20-00FFCE?style=flat-square) `#00FFCE` | ![](https://img.shields.io/badge/-%20-DDDAD1?style=flat-square) `#DDDAD1` | 13.8:1 | AAA |
| Comonad | ![](https://img.shields.io/badge/-%20-FFBE0B?style=flat-square) `#FFBE0B` | ![](https://img.shields.io/badge/-%20-E8CF1F?style=flat-square) `#E8CF1F` | 12.3:1 | AAA |
| Isomorphism | ![](https://img.shields.io/badge/-%20-33DD66?style=flat-square) `#33DD66` | ![](https://img.shields.io/badge/-%20-CCBC6F?style=flat-square) `#CCBC6F` | 10.1:1 | AAA |
| Hom | ![](https://img.shields.io/badge/-%20-4CB8E8?style=flat-square) `#4CB8E8` | ![](https://img.shields.io/badge/-%20-8AA6E7?style=flat-square) `#8AA6E7` | 8.0:1 | AAA |
| Unit | ![](https://img.shields.io/badge/-%20-FF3366?style=flat-square) `#FF3366` | ![](https://img.shields.io/badge/-%20-A39761?style=flat-square) `#A39761` | 6.6:1 | AA |
| Right Adjoint | ![](https://img.shields.io/badge/-%20-AA78C8?style=flat-square) `#AA78C8` | ![](https://img.shields.io/badge/-%20-758DC6?style=flat-square) `#758DC6` | 5.9:1 | AA |
| Counit | ![](https://img.shields.io/badge/-%20-666666?style=flat-square) `#666666` | ![](https://img.shields.io/badge/-%20-666666?style=flat-square) `#666666` | 3.4:1 | AA-lg |
| Morphism | ![](https://img.shields.io/badge/-%20-D4D4D4?style=flat-square) `#D4D4D4` | ![](https://img.shields.io/badge/-%20-D4D4D4?style=flat-square) `#D4D4D4` | 13.0:1 | AAA |

**Near-pairs:**

- **Right Adjoint ↔ Hom** — both shift blue-ish (Δ46). Different spatial roles (links vs containers), rarely adjacent. Rule 10 prevents nesting.
- **Unit ↔ Isomorphism** — both shift ochre (Δ57). The classic red-green collapse. Icons ✕ and ✓ are the only discriminant.

</details>

<details>
<summary><strong>Tritanopia</strong> — no blue cones (~0.003%)</summary>

&nbsp;

| Name | Original | Simulated | Ratio | Level |
|:--|:--|:--|:--|:--|
| Left Adjoint | ![](https://img.shields.io/badge/-%20-00FFCE?style=flat-square) `#00FFCE` | ![](https://img.shields.io/badge/-%20-00FFF1?style=flat-square) `#00FFF1` | 15.2:1 | AAA |
| Isomorphism | ![](https://img.shields.io/badge/-%20-33DD66?style=flat-square) `#33DD66` | ![](https://img.shields.io/badge/-%20-00D8C2?style=flat-square) `#00D8C2` | 10.6:1 | AAA |
| Comonad | ![](https://img.shields.io/badge/-%20-FFBE0B?style=flat-square) `#FFBE0B` | ![](https://img.shields.io/badge/-%20-FFAAA2?style=flat-square) `#FFAAA2` | 10.6:1 | AAA |
| Hom | ![](https://img.shields.io/badge/-%20-4CB8E8?style=flat-square) `#4CB8E8` | ![](https://img.shields.io/badge/-%20-00C5C8?style=flat-square) `#00C5C8` | 9.0:1 | AAA |
| Right Adjoint | ![](https://img.shields.io/badge/-%20-AA78C8?style=flat-square) `#AA78C8` | ![](https://img.shields.io/badge/-%20-A78397?style=flat-square) `#A78397` | 5.8:1 | AA |
| Unit | ![](https://img.shields.io/badge/-%20-FF3366?style=flat-square) `#FF3366` | ![](https://img.shields.io/badge/-%20-FF004A?style=flat-square) `#FF004A` | 4.9:1 | AA |
| Counit | ![](https://img.shields.io/badge/-%20-666666?style=flat-square) `#666666` | ![](https://img.shields.io/badge/-%20-666666?style=flat-square) `#666666` | 3.4:1 | AA-lg |
| Morphism | ![](https://img.shields.io/badge/-%20-D4D4D4?style=flat-square) `#D4D4D4` | ![](https://img.shields.io/badge/-%20-D4D4D4?style=flat-square) `#D4D4D4` | 13.0:1 | AAA |

**Near-pair:**

- **Hom ↔ Isomorphism** — both collapse to near-identical cyan (Δ20). Affects ~0.003% of the population. Icons are the interface for this group.

</details>

### Why it works

Rule 7 ("never color alone") was written before the CVD simulation was run. The simulation validated it. Color is a channel, not the signal. The signal is shape: ✓ ℹ ⚠ ✕. For the ~2% of users with color vision deficiency, the icons do the work. Color reinforces. This is the correct architecture.

## Usage rules

1. **Cyan is earned.** Headers, links, the logo, key data. Never decoration.
2. **Amber warns.** Deprecation notices, caution states, things worth a second look. Not as urgent as rose.
3. **Rose is rare.** If more than 5% of a surface is `#FF3366`, something is wrong with the surface, not the palette.
4. **Purple connects.** Links to Julia ecosystem, references to dependencies, inherited concepts.
5. **When in doubt, use gray.** Most UI is structure, and structure is gray.
6. **No gradients.** Flat color. The algebra is discrete.
7. **Never color alone.** Errors get an icon. Links get an underline. Status gets a label. Color reinforces — it doesn't carry.
8. **Blue informs.** Info banners, focus states, hover highlights, selected rows. Orients without demanding.
9. **Green confirms.** Passing tests, successful operations, verified states. Always paired with ✓ or "passed."
10. **Hom and Right Adjoint don't nest.** Never place lilac links inside blue info containers. Under deuteranopia, both collapse to the same blue.
11. **Three chromatic max per surface.** If a card needs four accent colors, one of them is wrong.
12. **Cyan is not success. Blue is not links.** Isomorphism handles success. Right Adjoint handles links. Web conventions do not override the algebra.

## Alerts

Four levels. Icons are not optional — they are the signal. Color is the channel.

| Level | Color | Icon | When |
|:--|:--|:--|:--|
| Success | ![](https://img.shields.io/badge/Isomorphism-%20-33DD66?style=flat-square&labelColor=0C0E16) `#33DD66` | ✓ | Passing tests, verified, confirmed |
| Info | ![](https://img.shields.io/badge/Hom-%20-4CB8E8?style=flat-square&labelColor=0C0E16) `#4CB8E8` | ℹ | Neutral information, status updates |
| Warning | ![](https://img.shields.io/badge/Comonad-%20-FFBE0B?style=flat-square&labelColor=0C0E16) `#FFBE0B` | ⚠ | Deprecations, caution, second look |
| Error | ![](https://img.shields.io/badge/Unit-%20-FF3366?style=flat-square&labelColor=0C0E16) `#FF3366` | ✕ | Failures, breaking changes, act now |

## Inversions

For solid-fill elements (tags, badges, buttons), use Void text on colored backgrounds. Always Void — never Elevation. The contrast is higher and the tint is invisible at small sizes.

| Background | Text | Ratio | Level |
|:--|:--|:--|:--|
| ![](https://img.shields.io/badge/Left_Adjoint-%20-00FFCE?style=flat-square&labelColor=0C0E16) | ![](https://img.shields.io/badge/Void-%20-0C0E16?style=flat-square&labelColor=0C0E16) | 14.9:1 | AAA |
| ![](https://img.shields.io/badge/Morphism-%20-D4D4D4?style=flat-square&labelColor=0C0E16) | ![](https://img.shields.io/badge/Void-%20-0C0E16?style=flat-square&labelColor=0C0E16) | 13.0:1 | AAA |
| ![](https://img.shields.io/badge/Comonad-%20-FFBE0B?style=flat-square&labelColor=0C0E16) | ![](https://img.shields.io/badge/Void-%20-0C0E16?style=flat-square&labelColor=0C0E16) | 11.6:1 | AAA |
| ![](https://img.shields.io/badge/Isomorphism-%20-33DD66?style=flat-square&labelColor=0C0E16) | ![](https://img.shields.io/badge/Void-%20-0C0E16?style=flat-square&labelColor=0C0E16) | 10.7:1 | AAA |
| ![](https://img.shields.io/badge/Hom-%20-4CB8E8?style=flat-square&labelColor=0C0E16) | ![](https://img.shields.io/badge/Void-%20-0C0E16?style=flat-square&labelColor=0C0E16) | 8.6:1 | AAA |
| ![](https://img.shields.io/badge/Right_Adjoint-%20-AA78C8?style=flat-square&labelColor=0C0E16) | ![](https://img.shields.io/badge/Void-%20-0C0E16?style=flat-square&labelColor=0C0E16) | 5.7:1 | AA |
| ![](https://img.shields.io/badge/Unit-%20-FF3366?style=flat-square&labelColor=0C0E16) | ![](https://img.shields.io/badge/Void-%20-0C0E16?style=flat-square&labelColor=0C0E16) | 5.4:1 | AA |

## CSS variables

```css
:root {
  --void: #0C0E16;
  --elevation: #181B24;
  --counit: #666666;
  --morphism: #D4D4D4;
  --left-adjoint: #00FFCE;
  --right-adjoint: #AA78C8;
  --unit: #FF3366;
  --comonad: #FFBE0B;
  --hom: #4CB8E8;
  --isomorphism: #33DD66;

  /* Alpha stops */
  --alpha-subtle: 0.06;
  --alpha-medium: 0.12;
  --alpha-strong: 0.20;
}
```

## Julia constants

```julia
const PALETTE = (
    void          = "#0C0E16",
    elevation     = "#181B24",
    counit        = "#666666",
    morphism      = "#D4D4D4",
    left_adjoint  = "#00FFCE",
    right_adjoint = "#AA78C8",
    unit          = "#FF3366",
    comonad       = "#FFBE0B",
    hom           = "#4CB8E8",
    isomorphism   = "#33DD66",
)
```

## Terminal colors

Nearest ANSI 256 codes for CI logs, REPL output, and test runners.

| Name | | Hex | ANSI 256 | Escape |
|:--|:--|:--|:--|:--|
| Void | ![](https://img.shields.io/badge/-%20-0C0E16?style=flat-square) | `#0C0E16` | 233 | `\e[38;5;233m` |
| Elevation | ![](https://img.shields.io/badge/-%20-181B24?style=flat-square) | `#181B24` | 234 | `\e[38;5;234m` |
| Counit | ![](https://img.shields.io/badge/-%20-666666?style=flat-square) | `#666666` | 102 | `\e[38;5;102m` |
| Morphism | ![](https://img.shields.io/badge/-%20-D4D4D4?style=flat-square) | `#D4D4D4` | 252 | `\e[38;5;252m` |
| Left Adjoint | ![](https://img.shields.io/badge/-%20-00FFCE?style=flat-square) | `#00FFCE` | 50 | `\e[38;5;50m` |
| Right Adjoint | ![](https://img.shields.io/badge/-%20-AA78C8?style=flat-square) | `#AA78C8` | 140 | `\e[38;5;140m` |
| Unit | ![](https://img.shields.io/badge/-%20-FF3366?style=flat-square) | `#FF3366` | 204 | `\e[38;5;204m` |
| Comonad | ![](https://img.shields.io/badge/-%20-FFBE0B?style=flat-square) | `#FFBE0B` | 220 | `\e[38;5;220m` |
| Hom | ![](https://img.shields.io/badge/-%20-4CB8E8?style=flat-square) | `#4CB8E8` | 81 | `\e[38;5;81m` |
| Isomorphism | ![](https://img.shields.io/badge/-%20-33DD66?style=flat-square) | `#33DD66` | 78 | `\e[38;5;78m` |

Reset with `\e[0m` or `tput sgr0`.

## Files

| File | Purpose |
|:--|:--|
| [`tokens.json`](tokens.json) | Single source of truth. Every other format is derivable from this. |
| [`adjoint.css`](adjoint.css) | Standalone CSS — custom properties, alerts, tags. No build step. |
