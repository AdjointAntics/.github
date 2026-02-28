# AdjointAntics — Categorical Design Standards

We build Julia libraries that take adjunctions seriously as an engineering discipline — not a curiosity, not a flex, but the computational structure behind differentiation, learning, and optimization. Where [AlgebraicJulia](https://github.com/AlgebraicJulia) gives you categories as data structures, we build categories as computational strategies — particularly the adjoint machinery (F &#8866; G) that drives autodiff, encoder-decoder architectures, and compositional inference.

For naming, testing, and code conventions, see [engineering.md](engineering.md).

---

## Design Principles

### 1. Protocol-then-model

Theory.jl declares abstract types and function stubs. Every downstream package implements concrete methods. This is explicit typeclass-style design: the protocol says what operations exist; the model says how they behave.

Do not implement categorical abstractions ad hoc. If a new abstraction is needed, declare it in Theory.jl first (protocol), then implement it in the appropriate tier (model).

### 2. Duality discipline

Every construction has a dual. Implement one side, and the dual falls out structurally. This halves the design space and catches errors — if your fold doesn't have a corresponding unfold, something is missing.

```
Free.jl    <-> Cofree.jl      (syntax <-> observation)
Initial.jl <-> Terminal.jl    (fold <-> unfold)
Poly.jl    <-> HomTime.jl     (interface <-> measurement)
Theory.jl  <-> Theory.jl      (self-dual: protocols)
Product    <-> Coproduct       (limit <-> colimit)
Fibration  <-> Opfibration     (cartesian <-> cocartesian)
```

When adding a new construction, ask: what is its dual? If the dual doesn't exist yet, plan for it.

### 3. Tier system

Dependencies flow strictly downward. No circular dependencies. Each tier depends only on what is below it.

| Tier | Packages | Role |
|------|----------|------|
| 0 | Theory.jl | Algebraic theory protocols (zero deps) |
| 1 | Yoneda.jl, YonedaStyle.jl, HomTime.jl | Representable math, visual foundation, measurement |
| 2 | Initial.jl, Terminal.jl | Fixed-point tier (fold/unfold duality) |
| 3 | Free.jl, Cofree.jl, Poly.jl | Adjunction tier (syntax/observation/wiring) |
| 4 | PolyModes.jl | Application tier (TUI as Moore machines) |

A package at tier N may depend on packages at tiers 0 through N-1. Never on its own tier or above.

### 4. Codata justification

Immutable by default. The only valid reasons for `mutable struct` are codata patterns — types whose identity is their behavior over time, not a snapshot:

- **Moore machines** — state evolves via `step!`, readout observes current state
- **Screen buffers** — double-buffered display with `diff_flush`
- **Sinks** — `emit!`/`drain!` lifecycle (DiagnosticSink, MetricSink, LogSink)
- **Focus rings** — cycling through widgets via feedback/trace
- **App roots** — running flag, theme, focus state

Document the codata justification in a comment above any mutable struct. If you can't articulate why the type needs mutation, make it immutable.

### 5. Law verification

Algebraic laws are not aspirational — they are tested. Every categorical abstraction MUST have its laws verified:

- **30+ law checkers** in Theory.jl (category, functor, monad, comonad, nat trans, adjunction triangles, 2-category interchange, pentagon, hexagon, profunctor, limit universal properties, pullback commutativity, fibration laws)
- **15 pre-built law suites** in Cofree.jl (functor, monad, comonad, semigroup, monoid, category, lens, prism, applicative, traverse, arrow, natural transformation, distributive, monoidal, profunctor, product, coproduct, equalizer, fibration, Grothendieck)

When adding a new abstraction: write the law checker in Theory.jl, add a law suite in Cofree.jl, and test it against your concrete implementation. Laws that aren't tested don't exist.

### 6. Compositionality

Abstractions compose — this is not optional, it's the point. Verify composition at every level:

- **Recursion schemes** compose: `chrono = futu + histo`, `dyna = ana + histo`. The law checkers verify the fusion equations.
- **Optics** compose via profunctors: Iso, Lens, Prism, Affine, Traversal, Grate form a lattice with `optic_lub` computing the least upper bound.
- **Moore machines** compose via wiring: `parallel` (tensor product), `sequential` (composition), `feedback` (trace).
- **Effects** compose via handlers: stack `run_state`, `run_reader`, `run_error` in any order.
- **BiCoders** compose: `(c1 then c2)` with forward `c2.encode . c1.encode` and backward `c1.decode . c2.decode`.

If two things don't compose cleanly, the abstraction boundary is wrong.

### 7. Iterative safety

Naive recursion is not acceptable for production code operating on unbounded structures:

- **AST traversal** uses explicit stack frames (`_children_and_rebuild` + frame vector), not native recursion. `cata_exprf` is stack-safe on arbitrarily deep ASTs.
- **Free monad bind** uses a type-aligned queue (`Chain`), achieving O(1) bind instead of O(n^2) with naive left-nesting. `_apply_continuation` handles reassociation on `Impure` nodes.
- **Benchmarks** disable GC during measurement windows and auto-calibrate evaluations per sample.

When implementing a recursive pattern, consider: will this stack-overflow on real-world input? If yes, use an explicit stack or continuation-passing.

### 8. Zero-dep foundations

Theory.jl, YonedaStyle.jl, and HomTime.jl have zero external dependencies. This is non-negotiable. Mathematical foundations cannot be contaminated by implementation concerns. If a foundation package needs functionality from an external library, either implement it locally or reconsider the architecture.

---

## Architecture

### Dual Pairs

```
Free.jl    <-> Cofree.jl      (syntax <-> observation)
Initial.jl <-> Terminal.jl    (fold <-> unfold)
Poly.jl    <-> HomTime.jl     (interface <-> measurement)
Theory.jl  <-> Theory.jl      (self-dual: protocols)
```

### Self-Improving Loop

```
DECLARE -> REPRESENT -> BUILD -> WIRE -> MEASURE -> OBSERVE -> FOLD -> UNFOLD -> (improve) -> DECLARE
Theory     Yoneda      Free    Poly    HomTime    Cofree     Initial  Terminal
```

### Key Modules in Theory.jl

| Module | Protocols | Purpose |
|--------|-----------|---------|
| Monoidal.jl | MonoidalCategory, BraidedMonoidal, TracedMonoidal | Tensor products, associators, unitors, braiding, trace |
| Profunctor.jl | Profunctor, TambaraModule, PastroModule | dimap, Tambara strength, free Tambara (left Kan along tensor) |
| Limit.jl | Cone, Cocone, Product, Coproduct, Equalizer, Coequalizer, Pullback, Pushout | Universal properties with mediating morphism factories |
| Fibration.jl | Fibration, Opfibration, CartesianMorphism, GrothendieckObj/Mor | Cartesian/cocartesian lifts, Grothendieck construction |
| Laws.jl | 30+ checkers | Pentagon, hexagon, profunctor identity, pullback square, cartesian lift, etc. |

---

## Practical Applications

| Application | Packages | What It Delivers |
|---|---|---|
| **AST refactoring tools** | Theory (ExprF) + Initial (cata/para/zygo/histo) + Terminal (ana/apo/futu) | Stack-safe, composable Julia source transforms. Paramorphisms see subtree + fold result; histomorphisms see full derivation history. |
| **Polyglot schema management** | Free (Schema + 11 backends) | Define once, generate SQL, TypeScript, GraphQL, Protobuf, OpenAPI, Avro, Arrow, TOML, Julia, Lean from one source. |
| **Algebraic effect systems** | Free (Eff + 7 handlers) | Pure business logic separated from effects. Swap interpreters for testing vs production. NonDet gives search/backtracking. |
| **Bidirectional data pipelines** | Free (BiCoder) + Poly (optics) | Composable encode/decode pairs. Lenses for records, prisms for variants, traversals for collections. |
| **Property testing + law verification** | Cofree (Gen/shrink/suites) + Theory (Laws) | Drop-in property testing with shrinking + 15 pre-built law suites for functor, monad, lens, profunctor, fibration laws. |
| **Terminal UI applications** | PolyModes + Poly (Moore/wiring) + YonedaStyle | Widgets as Moore coalgebras. parallel = hsplit, sequential = vsplit, feedback = focus ring. Immutable state, testable in isolation. |
| **Categorical benchmarking** | HomTime | Auto-calibrated microbenchmarks. compose_temporal (sequential) and tensor_temporal (parallel) for correct pipeline arithmetic. |
| **Finite category computation** | Yoneda (Kan extensions, ends/coends, limits) | Compute left/right Kan extensions. Union-find coend quotients. Verify universal properties algorithmically. |
| **Wiring diagrams + visualization** | Poly (Diagrams + SVG renderer) | Build, validate, rewrite, and render string diagrams. Topological sort for evaluation order. SVG with bezier curves. |
| **Algebraic probability** | Free (Measure) | Pushforwards, marginalizations, conditioning as pure data. Compose with the effect system for probabilistic programming. |

### Highest-Leverage Bets

1. **Schema pipeline** — any project needing multi-target code generation can use Free.jl's Schema today. 11 backends is a serious head start.
2. **Property testing + law suites** — any Julia library defining algebraic abstractions can import Cofree.jl's law suites and get law verification out of the box.
3. **ExprF + recursion schemes** — stack-safe AST folds with histomorphic context are genuinely better than hand-written recursive Expr walkers, which are the norm in Julia macro libraries.

---

## Julia-Specific Pitfalls

### Phantom type parameters

Julia struct type params not used in any field cause `MethodError` on construction. Only include type params that appear in field types.

```julia
# BAD — A is phantom, construction fails
struct Wrapper{A}
    value::Int
end

# GOOD — A appears in field type
struct Wrapper{A}
    value::A
end
```

### Function equality

Composed functions (`g . h . f`) are never `==` to the original in Julia. For law tests, use pointwise comparison on test values or value-level data structures instead of function equality.

```julia
# BAD — always false
f = x -> x + 1
g = x -> x + 1
f == g  # false

# GOOD — compare outputs
all(f(x) == g(x) for x in test_values)
```

### Monoidal unitors

For tuple monoidal categories with unit `()`:
- Left unitor: `((), a) -> a` is `x -> x[2]` (not `identity`)
- Right unitor: `(a, ()) -> a` is `x -> x[1]` (not `identity`)

Getting this wrong breaks pentagon and triangle identities silently.
