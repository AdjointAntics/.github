<p align="center">
  <a href="https://github.com/AdjointAntics"><img src="https://raw.githubusercontent.com/AdjointAntics/.github/main/profile/logo.svg" alt="AdjointAntics" width="200"/></a>
</p>

<h1 align="center">AdjointAntics</h1>

<p align="center"><em>Seeking the universal property of good software.</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/F_%E2%8A%A3_G-adjoint%20paired-00FFCE?style=flat-square" alt="Adjoint Paired"/>
  <img src="https://img.shields.io/badge/julia-1.10+-9558B2?style=flat-square&logo=julia&logoColor=white" alt="Julia 1.10+"/>
  <img src="https://img.shields.io/badge/diagrams-commuting-00FFCE?style=flat-square" alt="Diagrams Commuting"/>
  <img src="https://img.shields.io/badge/license-MIT-D4D4D4?style=flat-square" alt="MIT"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Void-%20-0C0E16?style=flat-square&labelColor=0C0E16" alt="Void"/>
  <img src="https://img.shields.io/badge/Elevation-%20-181B24?style=flat-square&labelColor=0C0E16" alt="Elevation"/>
  <img src="https://img.shields.io/badge/Counit-%20-666666?style=flat-square&labelColor=0C0E16" alt="Counit"/>
  <img src="https://img.shields.io/badge/Morphism-%20-D4D4D4?style=flat-square&labelColor=0C0E16" alt="Morphism"/>
  <img src="https://img.shields.io/badge/Left_Adjoint-%20-00FFCE?style=flat-square&labelColor=0C0E16" alt="Left Adjoint"/>
  <img src="https://img.shields.io/badge/Right_Adjoint-%20-AA78C8?style=flat-square&labelColor=0C0E16" alt="Right Adjoint"/>
  <img src="https://img.shields.io/badge/Unit-%20-FF3366?style=flat-square&labelColor=0C0E16" alt="Unit"/>
  <img src="https://img.shields.io/badge/Comonad-%20-FFBE0B?style=flat-square&labelColor=0C0E16" alt="Comonad"/>
  <img src="https://img.shields.io/badge/Hom-%20-4CB8E8?style=flat-square&labelColor=0C0E16" alt="Hom"/>
  <img src="https://img.shields.io/badge/Isomorphism-%20-33DD66?style=flat-square&labelColor=0C0E16" alt="Isomorphism"/>
</p>

---

A monorepo of twelve Julia packages that take adjunctions seriously as an engineering discipline — not a curiosity, not a flex, but the computational structure behind differentiation, learning, and optimization. Where [AlgebraicJulia](https://github.com/AlgebraicJulia) gives you categories as data structures, we build categories as computational strategies — particularly the adjoint machinery $(F \dashv G)$ that drives autodiff, encoder-decoder architectures, and compositional inference.

The algebra should compile. The abstractions should vanish at runtime. The diagrams should commute.

## Quick Start

```julia
using Theory, Initial

# Fold a Julia AST bottom-up — count every node
expr = :(f(x + 1, g(y)))
count = cata_exprf(expr) do layer
    layer isa CallF ? 1 + sum(layer.args; init=0) :
    layer isa RefF  ? 1 : 1
end
# count = 6
```

## The Ecosystem

| | Package | What It Does | Dual |
|:--|:--|:--|:--|
| ![](https://img.shields.io/badge/T0-kernel-00FFCE?style=flat-square&labelColor=0C0E16) | [**Theory.jl**](Theory.jl) | Algebraic theory protocols, ExprF pattern functor, 78 law checkers | self-dual |
| ![](https://img.shields.io/badge/T1-foundation-4CB8E8?style=flat-square&labelColor=0C0E16) | [**Yoneda.jl**](Yoneda.jl) | Representable functors, presheaves, Kan extensions, limits | — |
| ![](https://img.shields.io/badge/T1-foundation-4CB8E8?style=flat-square&labelColor=0C0E16) | [**YonedaStyle.jl**](YonedaStyle.jl) | ANSI styling, tables, trees — display as representability | — |
| ![](https://img.shields.io/badge/T1-foundation-4CB8E8?style=flat-square&labelColor=0C0E16) | [**HomTime.jl**](HomTime.jl) | Hom-functor benchmarking with convergence and trust scores | [Poly.jl](Poly.jl) |
| ![](https://img.shields.io/badge/T2-fixed_point-FFBE0B?style=flat-square&labelColor=0C0E16) | [**Initial.jl**](Initial.jl) | Catamorphisms, paramorphisms, zygo, histo — the folds | [Terminal.jl](Terminal.jl) |
| ![](https://img.shields.io/badge/T2-fixed_point-FFBE0B?style=flat-square&labelColor=0C0E16) | [**Terminal.jl**](Terminal.jl) | Anamorphisms, futu, chrono, streams, sinks — the unfolds | [Initial.jl](Initial.jl) |
| ![](https://img.shields.io/badge/T3-adjunction-AA78C8?style=flat-square&labelColor=0C0E16) | [**Free.jl**](Free.jl) | Algebraic effects, schema DSL, 11 code-gen backends, monad transformers | [Cofree.jl](Cofree.jl) |
| ![](https://img.shields.io/badge/T3-adjunction-AA78C8?style=flat-square&labelColor=0C0E16) | [**Cofree.jl**](Cofree.jl) | Cofree comonad, property testing, 22 algebraic law suites | [Free.jl](Free.jl) |
| ![](https://img.shields.io/badge/T3-adjunction-AA78C8?style=flat-square&labelColor=0C0E16) | [**Poly.jl**](Poly.jl) | Polynomial functors, profunctor optics, wiring diagrams, SVG rendering | [HomTime.jl](HomTime.jl) |
| ![](https://img.shields.io/badge/T4-application-33DD66?style=flat-square&labelColor=0C0E16) | [**PolyModes.jl**](PolyModes.jl) | TUI framework — widgets as Moore machines | — |
| ![](https://img.shields.io/badge/App-tool-D4D4D4?style=flat-square&labelColor=0C0E16) | [**Strict.jl**](Strict.jl) | Julia linter — 118 rules, functor architecture, autofixes | — |
| ![](https://img.shields.io/badge/Util-scaffold-D4D4D4?style=flat-square&labelColor=0C0E16) | [**StrictTemplate.jl**](StrictTemplate.jl) | Package scaffold — every other package factors through it | — |

## Dependency Flow

```
                          ┌─────────┐
                          │ Theory  │  T0 — the equivariant kernel
                          └────┬────┘
               ┌───────────────┼───────────────┐
          ┌────▼────┐    ┌─────▼─────┐    ┌────▼────┐
          │ Yoneda  │    │YonedaStyle│    │ HomTime │  T1 — foundations
          └────┬────┘    └─────┬─────┘    └────┬────┘
               │         ┌─────┤               │
          ┌────▼────┐    │┌────▼────┐          │
          │ Initial │    ││Terminal │           │      T2 — fixed points
          └────┬────┘    │└────┬────┘          │
               │    ┌────┘    │               │
          ┌────▼────▼┐  ┌─────▼─────┐   ┌────▼────┐
          │   Free   │  │  Cofree   │   │  Poly   │  T3 — adjunctions
          └──────────┘  └───────────┘   └────┬────┘
                                        ┌────▼─────┐
                                        │PolyModes │  T4 — applications
                                        └──────────┘
```

The self-improving loop traces through the tiers:

**DECLARE** (Theory) → **REPRESENT** (Yoneda) → **BUILD** (Free) → **WIRE** (Poly) → **MEASURE** (HomTime) → **OBSERVE** (Cofree) → **FOLD** (Initial) → **UNFOLD** (Terminal) → *improve* → **DECLARE**

## Dualities

Every construction has a dual. Implement one side, and the other falls out structurally. This halves the design space and catches errors — if your fold doesn't have a corresponding unfold, something is missing.

| Left | | Right | Relationship |
|:--|:--|:--|:--|
| **Free.jl** | ↔ | **Cofree.jl** | syntax ↔ observation |
| **Initial.jl** | ↔ | **Terminal.jl** | fold ↔ unfold |
| **Poly.jl** | ↔ | **HomTime.jl** | interface ↔ measurement |
| **Theory.jl** | ↔ | **Theory.jl** | self-dual: protocols |
| Product | ↔ | Coproduct | limit ↔ colimit |
| Fibration | ↔ | Opfibration | cartesian ↔ cocartesian |

## Design System

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

Ten colors. Categorically named. WCAG AA minimum on every surface. See the [full palette](https://github.com/AdjointAntics/.github/blob/main/docs/design/color-palette.md).

## Standards

- [**Engineering Standards**](https://github.com/AdjointAntics/.github/blob/main/docs/standards/engineering.md) — naming, structs, docstrings, dependencies, testing, quality gates, commit conventions
- [**Categorical Design Standards**](https://github.com/AdjointAntics/.github/blob/main/docs/standards/categorical.md) — protocol-then-model, duality discipline, tier system, law verification, compositionality

## Commands

```sh
make test              # all package tests (dependency order)
make integration       # cross-package integration + law tests
make check-all         # test + integration (full CI gate)
make bench             # benchmarks for Theory, Initial, Terminal, Free, Cofree, Poly
make test-<Pkg>.jl     # single package (e.g., make test-Theory.jl)
```

## Contributing

Every construction has a dual. Every contribution has a home.

| If you care about... | Start with... |
|:--|:--|
| Category theory foundations | [Theory.jl](Theory.jl) |
| Representable functors / limits | [Yoneda.jl](Yoneda.jl) |
| Terminal styling / rendering | [YonedaStyle.jl](YonedaStyle.jl) |
| Benchmarking / measurement | [HomTime.jl](HomTime.jl) |
| Recursion schemes / AST folds | [Initial.jl](Initial.jl) + [Terminal.jl](Terminal.jl) |
| Effects / code generation | [Free.jl](Free.jl) |
| Property testing / algebraic laws | [Cofree.jl](Cofree.jl) |
| Polynomial functors / optics | [Poly.jl](Poly.jl) |
| TUI / interactive apps | [PolyModes.jl](PolyModes.jl) |
| Linting / static analysis | [Strict.jl](Strict.jl) |

See the org-wide [Contributing Guide](https://github.com/AdjointAntics/.github/blob/main/CONTRIBUTING.md).

## License

MIT. See each package's LICENSE file.

---

<p align="center"><em>Seeking the universal property of good software.</em></p>
