# Progressive Hellenization — AdjointAntics Notation Convention

Mathematics telescopes. A textbook opens with "add two numbers" and closes with $\int_X \omega$. This is not an accident — it is the only honest way to teach a subject whose depth is real. Our documentation follows the same gradient.

## The Rule

Within every README, notation progresses from English at the surface to Greek at the foundations. The reader who stops at Quick Start gets working code. The reader who reaches Categorical Foundations gets the equations. Neither is shortchanged.

## The Gradient

| Section | Register | What the reader sees |
|:--|:--|:--|
| **Quick Start** | English | "Fold a Julia AST", "count every node" |
| **Installation** | English | `Pkg.develop(...)` |
| **Usage by Level** | English + Greek etymology | `### Catamorphism (κατά) — collapse bottom-up` |
| **Categorical Foundations** | Greek-dominant, English glosses | $\mathrm{cata}(\alpha) = \alpha \circ F(\mathrm{cata}(\alpha)) \circ \mathrm{out}$ |
| **Duality** | Formal notation | $\mu F \xrightarrow{\mathrm{cata}} A \quad \dashv \quad S \xrightarrow{\mathrm{ana}} \nu F$ |
| **API Reference** | Code | `cata_exprf`, `para_exprf` |

The gradient is **within each document**, not across documents. Every README is self-contained — a reader never needs to have read another package's README to understand the progression.

## Section-Level Rules

### Quick Start — pure English

No Greek. No LaTeX. No categorical jargon beyond what a Julia developer already knows. The goal is a working example in under 10 lines.

```markdown
# Good
"Count every node in a Julia AST — one catamorphism"

# Bad
"Apply the unique F-algebra morphism from (μF, in) to count nodes"
```

### Usage by Level — etymology in headers, English in prose

Section headers carry the Greek root in parentheses. The prose below remains English. Code examples are pure Julia.

```markdown
### Catamorphism (κατά) — collapse bottom-up

The foundational fold. Project one layer, fold all children, apply the algebra.
```

The Greek root serves two purposes: it teaches the etymology, and it signals that this is a named mathematical concept, not just a library function.

**Greek roots used in headers:**

| Name | Root | Origin | Meaning |
|:--|:--|:--|:--|
| cata | κατά | Greek | "down" — bottom-up |
| ana | ἀνά | Greek | "up" — top-down |
| para | παρά | Greek | "beside" — with context |
| apo | ἀπό | Greek | "from" — with termination |
| histo | ἱστο | Greek | "tissue" — with history |
| futu | futu | Latin | "future" — with foresight |
| zygo | ζυγο | Greek | "yoke" — paired/mutual |
| chrono | χρόνο | Greek | "time" — forward+backward |
| dyna | δυνα | Greek | "power" — unfold+history |
| hylo | ὕλη | Greek | "matter" — fused fold-unfold |

### Categorical Foundations — Greek-dominant

This is where the mathematics lives. LaTeX notation is primary. English serves as gloss.

**Pattern:** Greek symbol, parenthetical English name, em dash, formal type signature, period, one-sentence English explanation.

```markdown
- **cata** (κατά, "down") — $\mathrm{cata}(\alpha) = \alpha \circ F(\mathrm{cata}(\alpha)) \circ \mathrm{out}$. The unique fold.
```

**Display math** for the defining equation of the section:

```markdown
$$\mathrm{cata}(\alpha) : \mu F \to A \quad \text{where} \quad \alpha : F(A) \to A$$
```

### Duality — full formal notation

The deepest section. Adjunction notation, turnstile symbol, Greek-only names in the correspondence line.

```markdown
> $\mu F \xrightarrow{\mathrm{cata}} A \quad \dashv \quad S \xrightarrow{\mathrm{ana}} \nu F$
>
> κατά ↔ ἀνά · παρά ↔ ἀπό · ἱστο ↔ futu · ζυγο ↔ mutual ἀνά
```

### API Reference — back to code

Type names and function names. No Greek. The reference is a lookup table, not a lecture.

## The Greek Alphabet in AdjointAntics

Seven letters carry structural meaning across the ecosystem. These are not arbitrary — they are the standard notation from category theory.

| Symbol | Name | What it means here | Where it appears |
|:--|:--|:--|:--|
| $\eta$ | eta | Unit — monadic `pure`, the start of a round trip | Theory.jl, Free.jl |
| $\epsilon$ | epsilon | Counit — comonadic `extract`, the return | Theory.jl, Cofree.jl |
| $\mu$ | mu | Multiplication — monadic `join` / `bind`, flattening | Theory.jl, Free.jl |
| $\delta$ | delta | Comultiplication — comonadic `duplicate`, branching | Theory.jl, Cofree.jl |
| $\alpha$ | alpha | Algebra — the target of a fold ($F(A) \to A$) | Initial.jl |
| $\gamma$ | gamma | Coalgebra — the source of an unfold ($S \to F(S)$) | Terminal.jl |
| $\phi$ | phi | Yoneda isomorphism — `tabulate` / `index` | Yoneda.jl |

Additional notation used in specific packages:

| Symbol | Package | Usage |
|:--|:--|:--|
| $\Sigma$ | Poly.jl | Polynomial sum: $p(y) = \Sigma_i y^{D_i}$ |
| $\int_A$, $\int^A$ | Yoneda.jl | End and coend |
| $\Omega$ | Yoneda.jl | Subobject classifier |
| $\chi$ | Yoneda.jl | Characteristic morphism |
| $\otimes$ | Poly.jl | Tensor product (parallel composition) |
| $\dashv$ | All | Adjunction: $F \dashv G$ |
| $\nu F$ | Terminal.jl | Terminal coalgebra (greatest fixed point) |
| $\mu F$ | Initial.jl | Initial algebra (least fixed point) |
| $F^*$ | Free.jl | Free monad |
| $F_\infty$ | Cofree.jl | Cofree comonad |

## Tier Calibration

The amount of Greek scales with the tier's categorical depth. This is structural, not decorative.

| Tier | Greek density | Why |
|:--|:--|:--|
| T0 (Theory) | Notation table only | Declares protocols — the Greek lives in the implementations |
| T1 (Yoneda, YonedaStyle, HomTime) | LaTeX in Foundations | First contact with representability, Hom-sets |
| T2 (Initial, Terminal) | Etymology in headers + formal types | Recursion schemes ARE Greek — the names encode structure |
| T3 (Free, Cofree, Poly) | Heaviest notation | Adjunction tier — η, ε, μ, δ are the API's shadow |
| T4 (PolyModes) | English only | Application layer — the categories are below the surface |
| App/Util (Strict, StrictTemplate) | English only | Tools — the user doesn't need to know it's a catamorphism |

## LaTeX Conventions

GitHub renders `$...$` for inline math and `$$...$$` for display math via MathJax.

**Operator names** use `\mathrm{}`: $\mathrm{cata}$, $\mathrm{ana}$, $\mathrm{Hom}$, $\mathrm{Lan}$, $\mathrm{Nat}$.

**Category names** use `\mathbf{}`: $\mathbf{Set}$, $\mathbf{C}$, $\mathbf{Poly}$.

**Op** uses `\mathrm{op}` as superscript: $\mathbf{C}^{\mathrm{op}}$.

**Functor categories** use brackets: $[\mathbf{C}^{\mathrm{op}}, \mathbf{Set}]$.

**Code names** stay in backticks, even inside math-heavy sections: `cata_exprf`, `project`, `embed`. The distinction between the mathematical concept ($\mathrm{cata}$) and the Julia function (`cata_exprf`) is load-bearing.

## What NOT to Do

- Do not add Greek to Quick Start sections. Ever.
- Do not use Greek in code comments or docstrings — those follow Julia conventions.
- Do not explain what $\eta$ means every time it appears. Define it once in Theory.jl's table; reference it everywhere else.
- Do not transliterate Julia function names into Greek ($\mathrm{cata\_exprf}$). The function is `cata_exprf`. The concept is $\mathrm{cata}(\alpha)$.
- Do not use Greek in CLAUDE.md files. Those are implementation references, not mathematical documents.
- Do not use display math (`$$...$$`) for inline expressions. Reserve display math for defining equations.
- Do not introduce Greek symbols that aren't standard in category theory. If Borceux or Mac Lane doesn't use it, neither do we.

---

<p align="center"><em>The notation is the territory.</em></p>
