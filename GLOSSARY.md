# AdjointAntics — Category Theory Glossary

## Core Concepts

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **Morphism** | Structure-preserving map between objects | Theory.jl | `AbstractMorphism{S,T}` |
| **Functor** | Structure-preserving map between categories | Theory.jl | `AbstractFunctor{C,D}` |
| **Natural Transformation** | Structure-preserving map between functors | Theory.jl | `AbstractNatTransform{F,G}` |
| **Composition** | Sequential application of morphisms | Theory.jl | `compose(f, g)` |
| **Identity** | Neutral element for composition | Theory.jl | `id(::Type{T})` |
| **fmap** | Functor action on morphisms | Theory.jl | `fmap(F, f)` |
| **pure** | Monadic unit (η) | Theory.jl | `pure(::Type{M}, a)` |
| **bind** | Monadic extension (Kleisli) | Theory.jl | `bind(m, f)` |
| **extract** | Comonadic counit (ε) | Theory.jl | `extract(w)` |
| **extend** | Comonadic extension (co-Kleisli) | Theory.jl | `extend(f, w)` |
| **duplicate** | Comultiplication (δ) | Theory.jl | `duplicate(w)` |

## Pattern Functor

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **ExprF** | One-layer functor for Julia AST | Theory.jl | `ExprF{A}` (17 variants) |
| **project** | Peel one recursive layer: X → F{X} | Theory.jl | `project(expr)` |
| **embed** | Wrap one recursive layer: F{X} → X | Theory.jl | `embed(ef)` |
| **fmap_exprf** | Functor map over ExprF children | Theory.jl | `fmap_exprf(f, ef)` |

## Recursion Schemes

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **Catamorphism** | Bottom-up fold (initial algebra → target algebra) | Initial.jl | `cata_exprf(alg, expr)` |
| **Paramorphism** | Fold with original subtree access | Initial.jl | `para_exprf(alg, expr)` |
| **Anamorphism** | Top-down unfold (seed → terminal coalgebra) | Terminal.jl | `ana_exprf(coalg, seed)` |
| **Apomorphism** | Unfold with early termination | Terminal.jl | `apo(coalg, seed)` |
| **Hylomorphism** | Fused unfold-fold (no intermediate tree) | Theory.jl | `hylo_exprf(alg, coalg, seed)` |

## Fixed Points

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **Initial Algebra** | Least fixed point of a functor | Initial.jl | `InitialAlgebra{F}` |
| **Terminal Coalgebra** | Greatest fixed point of a functor | Terminal.jl | `TerminalCoalgebra{F}` |

## Adjunctions

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **Free Monad** | Free construction over a functor | Free.jl | `Eff{R,A}` |
| **Cofree Comonad** | Cofree construction over a functor | Cofree.jl | `Cofree{F,A}` |
| **Polynomial Functor** | Arena of positions and directions | Poly.jl | `Arena{P,D}` |
| **Lens** | Morphism between polynomial functors | Poly.jl | `Lens` |
| **Moore Machine** | Coalgebra of a polynomial functor | Poly.jl | `Moore` |

## Representability

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **Representable** | Functor isomorphic to Hom(R, -) | Yoneda.jl | `Representable` trait |
| **tabulate** | Build representation from index function | Yoneda.jl | `tabulate(F, f)` |
| **index** | Extract value at index from representation | Yoneda.jl | `index(fa, i)` |
| **Presheaf** | Contravariant functor to Set | Yoneda.jl | `Presheaf` |

## Dualities

| Left | Right | Relationship |
|------|-------|-------------|
| Free.jl | Cofree.jl | syntax ↔ observation |
| Initial.jl | Terminal.jl | fold ↔ unfold |
| Poly.jl | HomTime.jl | interface ↔ measurement |
| algebra | coalgebra | constructor ↔ observer |
| cata | ana | fold ↔ unfold |
| para | apo | fold+context ↔ unfold+termination |
| pure | extract | unit ↔ counit |
| bind | extend | Kleisli ↔ co-Kleisli |
| histo | futu | fold+history ↔ unfold+future |
| zygo | mutual ana | paired fold ↔ paired unfold |
| tensor | cotensor | monoidal product ↔ internal hom |
| limit | colimit | universal cone ↔ universal cocone |
| cartesian lift | cocartesian lift | fibration ↔ opfibration |

## Monoidal Structure

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **MonoidalCategory** | Category with a tensor product and unit object | Theory.jl | `MonoidalCategory` protocol |
| **tensor** | Monoidal product of two objects | Theory.jl | `tensor(a, b)` |
| **monoidal_unit** | Unit object for the tensor product | Theory.jl | `monoidal_unit(::Type{C})` |
| **associator** | Natural isomorphism (A⊗B)⊗C ≅ A⊗(B⊗C) | Theory.jl | `associator(a, b, c)` |
| **left_unitor** | Natural isomorphism I⊗A ≅ A | Theory.jl | `left_unitor(a)` |
| **right_unitor** | Natural isomorphism A⊗I ≅ A | Theory.jl | `right_unitor(a)` |
| **BraidedMonoidal** | Monoidal category with braiding A⊗B ≅ B⊗A | Theory.jl | `BraidedMonoidal` protocol |
| **TracedMonoidal** | Monoidal category with trace (feedback) | Theory.jl | `TracedMonoidal` protocol |

## Profunctors

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **Profunctor** | Functor C^op × D → Set | Theory.jl | `Profunctor` protocol |
| **dimap** | Profunctor action: contravariant in first, covariant in second | Theory.jl | `dimap(f, g, p)` |
| **TambaraModule** | Strength for profunctor optics | Theory.jl | `TambaraModule` |
| **PastroModule** | Free Tambara (left Kan extension along tensor) | Theory.jl | `PastroModule` |

## Limits & Colimits

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **Product** | Universal cone over a discrete diagram | Theory.jl + Yoneda.jl | `compute_product(objects)` |
| **Coproduct** | Universal cocone over a discrete diagram | Theory.jl + Yoneda.jl | `compute_coproduct(objects)` |
| **Equalizer** | Limit of a parallel pair | Theory.jl + Yoneda.jl | `compute_equalizer(f, g)` |
| **Pullback** | Limit of a cospan | Theory.jl + Yoneda.jl | `compute_pullback(f, g)` |
| **Pushout** | Colimit of a span | Theory.jl + Yoneda.jl | `compute_pushout(f, g)` |
| **Cone** | Compatible family of morphisms to a diagram | Theory.jl | `Cone` |
| **Cocone** | Compatible family of morphisms from a diagram | Theory.jl | `Cocone` |

## Fibrations

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **Fibration** | Functor with cartesian lifts | Theory.jl | `Fibration` protocol |
| **Opfibration** | Functor with cocartesian lifts | Theory.jl | `Opfibration` protocol |
| **CartesianLift** | Lift of a morphism along a fibration | Theory.jl | `CartesianLift` |
| **CocartesianLift** | Lift of a morphism along an opfibration | Theory.jl | `CocartesianLift` |
| **GrothendieckObj** | Object in the total category of a fibration | Theory.jl | `GrothendieckObj` |
| **GrothendieckMor** | Morphism in the Grothendieck construction | Theory.jl | `GrothendieckMor` |

## 2-Categories

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **TwoCategory** | Category enriched over categories | Theory.jl | `TwoCategory` protocol |
| **TwoMorphism** | 2-cell between morphisms | Theory.jl | `TwoMorphism` |
| **horizontal_compose** | Composition of 2-morphisms along objects | Theory.jl | `horizontal_compose(α, β)` |
| **vertical_compose** | Composition of 2-morphisms along morphisms | Theory.jl | `vertical_compose(α, β)` |

## Polynomial Functors

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **Arena** | Polynomial functor p(y) = Σᵢ yᴰⁱ (positions + directions) | Poly.jl | `Arena{P,D}` |
| **poly_add** | Sum of polynomial functors | Poly.jl | `poly_add(p, q)` |
| **poly_mul** | Product of polynomial functors | Poly.jl | `poly_mul(p, q)` |
| **poly_compose** | Composition of polynomial functors | Poly.jl | `poly_compose(p, q)` |
| **Lens** | Morphism between polynomial functors (get/set) | Poly.jl | `Lens` |
| **Prism** | Coproduct optic (match/build) | Poly.jl | `Prism` |
| **Iso** | Isomorphism between polynomial functors | Poly.jl | `Iso` |
| **Moore** | Coalgebra of a polynomial functor (state machine) | Poly.jl | `Moore` |

## Effects & Schemas

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **Eff** | Free monad over an effect signature | Free.jl | `Eff` (`Pure`, `Impure`) |
| **Handler** | Effect algebra (interprets effects into values) | Free.jl | `Handler` |
| **Schema** | Declarative data schema definition | Free.jl | `Schema` |
| **BiCoder** | Bidirectional encode/decode transformation | Free.jl | `BiCoder` |
| **ConstraintIR** | Constraint intermediate representation | Free.jl | `ConstraintIR` |
| **Measure** | Algebraic probability distribution | Free.jl | `Measure` |

## Property Testing

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **Gen** | Property test generator | Cofree.jl | `Gen`, `FnGen` |
| **Outcome** | Test result (Pass/Fail/Error/Skip/Pending/Timeout/Flaky) | Cofree.jl | `Outcome` variants |
| **PropertyResult** | Result of running a property test | Cofree.jl | `PropertyResult` |
| **@check** | Macro: run a property test inline | Cofree.jl | `@check` |
| **@suite** | Macro: group related property tests | Cofree.jl | `@suite` |

## Measurement

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **Measurement** | Single function timing observation | HomTime.jl | `Measurement` |
| **HomSet** | Collection of measurement observations | HomTime.jl | `HomSet` |
| **Suite** | Named collection of benchmarks | HomTime.jl | `Suite` |
| **Evidence** | Structured judgment (significance + effect + trust) | HomTime.jl | `Evidence` |
| **TrustScore** | Composite measurement reliability score | HomTime.jl | `TrustScore` |
| **ComplexityAnalysis** | Algorithmic complexity detection (O(1)..O(2^n)) | HomTime.jl | `ComplexityAnalysis` |

## Streams & Sinks

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **Stream** | Lazy coinductive sequence (head + thunked tail) | Terminal.jl | `Stream` |
| **iterate_stream** | Build a stream from a step function | Terminal.jl | `iterate_stream(f, x)` |
| **take** | Finite prefix of a stream | Terminal.jl | `take(s, n)` |
| **Config** | Terminal object for configuration | Terminal.jl | `Config` |
| **AbstractSink** | Observer hierarchy (DiagnosticSink, MetricSink, LogSink) | Terminal.jl | `AbstractSink` |

## Generalized Recursion

| Term | Definition | Package | Julia Construct |
|------|-----------|---------|-----------------|
| **histo** | Histomorphism: fold with full derivation history | Initial.jl | `histo_exprf(alg, expr)` |
| **zygo** | Zygomorphism: mutual catamorphism | Initial.jl | `zygo_exprf(alg₁, alg₂, expr)` |
| **futu** | Futumorphism: multi-step unfolding | Terminal.jl | `futu_exprf(coalg, seed)` |
| **chrono** | Chronomorphism: futu then histo | Terminal.jl | `chrono_exprf(alg, coalg, seed)` |
| **dyna** | Dynamorphism: ana then histo | Terminal.jl | `dyna_exprf(alg, coalg, seed)` |
