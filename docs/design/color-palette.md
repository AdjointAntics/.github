# Adjoint Ten — AdjointAntics Color Palette

An adjunction is not a symmetry. It's a directed relationship — one functor dominates, the other recedes. The palette reflects this. Cyan speaks. Everything else listens.

## Core

| Role | Name | Color | Hex | Contrast on Void | Rationale |
|:--|:--|:--|:--|:--|:--|
| Background | **Void** | Deep Indigo | `#0C0E16` | — | The category itself. Contains all objects and morphisms. Shows none. Almost everything is this. |
| Text | **Morphism** | Silver Arrow | `#D4D4D4` | 13.0:1 AAA | Arrows between objects. Not pure white — pure white is a statement, and the text isn't making one. |
| Primary | **Left Adjoint** | Alien Cyan | `#00FFCE` | 14.9:1 AAA | F. The free functor. Constructs, synthesizes, reaches forward. Used sparingly, which is why it works. |

## Accent

| Role | Name | Color | Hex | Contrast on Void | Rationale |
|:--|:--|:--|:--|:--|:--|
| Secondary | **Right Adjoint** | Forgetful Lilac | `#AA78C8` | 5.7:1 AA | G. The forgetful functor. Evolved from Julia purple. The lineage is visible in the color space. |
| Alert | **Unit** | Hot Rose | `#FF3366` | 5.4:1 AA | η: 1 → GF. The natural transformation that starts a round trip. Errors, breaking changes, deprecations. If you see this color, something is asking you to act. |
| Warning | **Comonad** | Electric Amber | `#FFBE0B` | 11.6:1 AAA | GF. The composition that observes before it transforms. Warnings, highlights, selections. The thing that asks you to notice before you decide. |
| Info | **Hom** | Frozen Neon | `#4CB8E8` | 8.6:1 AAA | Hom(A, B). The collection of all morphisms between two objects. Structural, quiet, always present. Info states, focus rings, hover backgrounds — the things that say "you're here" without saying "look at me." |
| Success | **Isomorphism** | Cathode Green | `#33DD66` | 10.7:1 AAA | f where f⁻¹ exists. The strongest positive statement. Passing tests, verified states, confirmed operations. Everything checks out. |

## Structure

| Role | Name | Color | Hex | Contrast on Void | Rationale |
|:--|:--|:--|:--|:--|:--|
| Surface | **Elevation** | Charcoal | `#181B24` | — | Code blocks, cards, anything that lifts off the void. The step is subtle. That's the point — structure should be felt, not seen. |
| Border | **Counit** | Ash | `#666666` | 3.4:1 AA-large | ε: FG → 1. The return. Borders, dividers, de-emphasized text. The things that organize without competing. |

## Adjoint Ten

<p>
  <img src="https://img.shields.io/badge/-Void-0C0E16?style=flat-square" alt="#0C0E16"/>
  <img src="https://img.shields.io/badge/-Elevation-181B24?style=flat-square" alt="#181B24"/>
  <img src="https://img.shields.io/badge/-Counit-666666?style=flat-square" alt="#666666"/>
  <img src="https://img.shields.io/badge/-Morphism-D4D4D4?style=flat-square" alt="#D4D4D4"/>
  <img src="https://img.shields.io/badge/-Left_Adjoint-00FFCE?style=flat-square" alt="#00FFCE"/>
  <img src="https://img.shields.io/badge/-Right_Adjoint-AA78C8?style=flat-square" alt="#AA78C8"/>
  <img src="https://img.shields.io/badge/-Unit-FF3366?style=flat-square" alt="#FF3366"/>
  <img src="https://img.shields.io/badge/-Comonad-FFBE0B?style=flat-square" alt="#FFBE0B"/>
  <img src="https://img.shields.io/badge/-Hom-4CB8E8?style=flat-square" alt="#4CB8E8"/>
  <img src="https://img.shields.io/badge/-Isomorphism-33DD66?style=flat-square" alt="#33DD66"/>
</p>

## Accessibility

All text-bearing colors meet WCAG 2.1 AA or higher on both Void (`#0C0E16`) and Elevation (`#181B24`) backgrounds:

| Color | On Void | On Elevation | Minimum required |
|:--|:--|:--|:--|
| Morphism `#D4D4D4` | 13.0:1 AAA | 11.6:1 AAA | AAA (body text) |
| Left Adjoint `#00FFCE` | 14.9:1 AAA | 13.3:1 AAA | AA (headings, links) |
| Comonad `#FFBE0B` | 11.6:1 AAA | 10.3:1 AAA | AA (warnings, highlights) |
| Right Adjoint `#AA78C8` | 5.7:1 AA | 5.1:1 AA | AA (links, labels) |
| Unit `#FF3366` | 5.4:1 AA | 4.8:1 AA | AA (alerts) |
| Hom `#4CB8E8` | 8.6:1 AAA | 7.6:1 AAA | AA (info, focus states) |
| Isomorphism `#33DD66` | 10.7:1 AAA | 9.6:1 AAA | AA (success states) |
| Counit `#666666` | 3.4:1 AA-large | 3.0:1 AA-large | AA-large (muted text, borders) |

Never convey meaning through color alone. Pair color with shape, icon, or text label.

### Color vision deficiency

Simulated against protanopia, deuteranopia, and tritanopia. All WCAG levels hold across every simulation. Rule 7 is the load-bearing structure — icons are the signal, color is the channel.

<details>
<summary><strong>Protanopia</strong> — no red cones (~1% of males)</summary>

&nbsp;

| Name | Original | Simulated | On Void | Level |
|:--|:--|:--|:--|:--|
| Morphism | `#D4D4D4` | `#D4D4D4` | 12.9:1 | AAA |
| Left Adjoint | `#00FFCE` | `#F7EDCC` | 16.4:1 | AAA |
| Right Adjoint | `#AA78C8` | `#6989CB` | 5.5:1 | AA |
| Unit | `#FF3366` | `#6F6D67` | 3.7:1 | AA-large |
| Comonad | `#FFBE0B` | `#D9BF00` | 10.4:1 | AAA |
| Hom | `#4CB8E8` | `#A0B6EA` | 9.5:1 | AAA |
| Isomorphism | `#33DD66` | `#DFC95B` | 11.5:1 | AAA |
| Counit | `#666666` | `#666666` | 3.3:1 | AA-large |

No confusable pairs. Unit (rose → gray) loses chromatic punch but the ✕ icon carries it.

</details>

<details>
<summary><strong>Deuteranopia</strong> — no green cones (~1% of males)</summary>

&nbsp;

| Name | Original | Simulated | On Void | Level |
|:--|:--|:--|:--|:--|
| Morphism | `#D4D4D4` | `#D4D4D4` | 13.0:1 | AAA |
| Left Adjoint | `#00FFCE` | `#DDDAD1` | 13.8:1 | AAA |
| Right Adjoint | `#AA78C8` | `#758DC6` | 5.9:1 | AA |
| Unit | `#FF3366` | `#A39761` | 6.6:1 | AA |
| Comonad | `#FFBE0B` | `#E8CF1F` | 12.3:1 | AAA |
| Hom | `#4CB8E8` | `#8AA6E7` | 8.0:1 | AAA |
| Isomorphism | `#33DD66` | `#CCBC6F` | 10.1:1 | AAA |
| Counit | `#666666` | `#666666` | 3.4:1 | AA-large |

**Near-pairs:**

- **Right Adjoint ↔ Hom** — both shift blue-ish (Δ46). Different spatial roles (links vs info containers), rarely adjacent. Rule 10 prevents nesting.
- **Unit ↔ Isomorphism** — both shift ochre (Δ57). The classic red-green collapse. The ✕ and ✓ icons are mandatory here — they are the only discriminant.

</details>

<details>
<summary><strong>Tritanopia</strong> — no blue cones (~0.003% of population)</summary>

&nbsp;

| Name | Original | Simulated | On Void | Level |
|:--|:--|:--|:--|:--|
| Morphism | `#D4D4D4` | `#D4D4D4` | 13.0:1 | AAA |
| Left Adjoint | `#00FFCE` | `#00FFF1` | 15.2:1 | AAA |
| Right Adjoint | `#AA78C8` | `#A78397` | 5.8:1 | AA |
| Unit | `#FF3366` | `#FF004A` | 4.9:1 | AA |
| Comonad | `#FFBE0B` | `#FFAAA2` | 10.5:1 | AAA |
| Hom | `#4CB8E8` | `#00C5C8` | 9.0:1 | AAA |
| Isomorphism | `#33DD66` | `#00D8C2` | 10.6:1 | AAA |
| Counit | `#666666` | `#666666` | 3.3:1 | AA-large |

**Near-pair:**

- **Hom ↔ Isomorphism** — both collapse to near-identical cyan (Δ20). Affects ~0.003% of the population. Icons are the interface for this group. Acceptable tradeoff — desaturating the entire palette to fix this would be a category error.

</details>

### Why it works

Rule 7 ("never color alone") was written before the CVD simulation was run. The simulation validated it. Color is a channel, not the signal. The signal is shape: ✓ for success, ℹ for info, ⚠ for warning, ✕ for error. For the ~2% of users with color vision deficiency, the icons do the actual work and the color is reinforcement. This is the correct architecture.

## Usage rules

1. **Cyan is earned.** Headers, links, the logo, key data. Never decoration.
2. **Amber warns.** Deprecation notices, caution states, things worth a second look. Not as urgent as rose.
3. **Rose is rare.** If more than 5% of a page is `#FF3366`, something is wrong with the page, not the palette.
4. **Purple connects.** Links to Julia ecosystem, references to dependencies, inherited concepts.
5. **When in doubt, use gray.** Most UI is structure, and structure is gray.
6. **No gradients.** Flat color. The algebra is discrete.
7. **Never color alone.** Errors get an icon. Links get an underline. Status gets a label. Color reinforces — it doesn't carry.
8. **Blue informs.** Info banners, focus states, hover highlights, selected rows. The things that orient without demanding.
9. **Green confirms.** Passing tests, successful operations, verified states. Always paired with a ✓ icon or "passed" label.
10. **Hom and Right Adjoint don't nest.** Never place lilac links inside blue info containers. Under deuteranopia, both collapse to the same blue.
11. **Three chromatic max per surface.** If a card needs four accent colors, one of them is wrong.
12. **Cyan is not success. Blue is not links.** Isomorphism handles success. Right Adjoint handles links. Web conventions do not override the algebra.

## Alerts

Four levels. The icons are not optional — they are the signal. The color is the channel.

| Level | Color | Icon | When |
|:--|:--|:--|:--|
| Success | Isomorphism `#33DD66` | ✓ | Passing tests, verified, confirmed |
| Info | Hom `#4CB8E8` | ℹ | Neutral information, status updates |
| Warning | Comonad `#FFBE0B` | ⚠ | Deprecations, caution, second look |
| Error | Unit `#FF3366` | ✕ | Failures, breaking changes, act now |

## Inversions

For solid-fill elements (tags, badges, buttons), use Void text on colored backgrounds. Always Void. Never Elevation — the contrast is higher and the tint is invisible at small sizes.

| Background | Text | Contrast |
|:--|:--|:--|
| Left Adjoint `#00FFCE` | Void `#0C0E16` | 14.9:1 |
| Isomorphism `#33DD66` | Void `#0C0E16` | 10.7:1 |
| Comonad `#FFBE0B` | Void `#0C0E16` | 11.6:1 |
| Hom `#4CB8E8` | Void `#0C0E16` | 8.6:1 |
| Unit `#FF3366` | Void `#0C0E16` | 5.4:1 |
| Right Adjoint `#AA78C8` | Void `#0C0E16` | 5.7:1 |

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

Nearest ANSI 256 codes for CI logs, REPL output, and test runners. Half the places these colors appear are terminals, not browsers.

| Name | Hex | ANSI 256 | Escape |
|:--|:--|:--|:--|
| Void | `#0C0E16` | 233 | `\e[38;5;233m` |
| Elevation | `#181B24` | 234 | `\e[38;5;234m` |
| Counit | `#666666` | 102 | `\e[38;5;102m` |
| Morphism | `#D4D4D4` | 252 | `\e[38;5;252m` |
| Left Adjoint | `#00FFCE` | 50 | `\e[38;5;50m` |
| Right Adjoint | `#AA78C8` | 140 | `\e[38;5;140m` |
| Unit | `#FF3366` | 204 | `\e[38;5;204m` |
| Comonad | `#FFBE0B` | 220 | `\e[38;5;220m` |
| Hom | `#4CB8E8` | 81 | `\e[38;5;81m` |
| Isomorphism | `#33DD66` | 78 | `\e[38;5;78m` |

Reset with `\e[0m` or `tput sgr0`.
