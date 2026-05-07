# Drift Analysis — Nuxt app vs `.claude/` guidelines

Generated 2026-05-07. Compares the current `src/` against the Vue/architecture parts of `.claude/skills/vue-project-guidelines/`, `.claude/rules/ARCHITECTURE.md`, `.claude/rules/ANTI-PATTERNS.md`, and the per-rule overrides in `CLAUDE.md`.

C# / xUnit / DDD-only items in the imported rules (Result types, `[Fact]`, `record struct`, EF Core, etc.) are excluded — they don't apply here.

## Summary

The project is a small Notion-backed static Nuxt site. Most of the skill's lighter rules (thin `app.vue`, file-based folder layout, immutability-leaning models) are already respected. The drift is concentrated in three places:
1. A composable + store wired into nothing (dead code that won't run).
2. Pages doing their own network/data assembly instead of going through composables.
3. Notion's wire format leaking into the domain models and a chunk of homepage data hardcoded in the component.

None of this blocks the site from building, but each item is exactly the kind of thing the imported rules were written to prevent.

---

## 1. Aligned with the guidelines

| Rule | Where it's respected |
|---|---|
| Thin `app.vue` | `src/app.vue:1-9` — only Header / NuxtPage / Footer. |
| File-based routing in `pages/` | `src/pages/{index,Agenda,cours,danses,photos}` — matches Nuxt convention. |
| Models in their own folder | `src/models/{Album,Cours,Danse}.ts`. |
| Build-time data caching over runtime fetching | `scripts/` prebuild pipeline → `/cache/*.json` consumed by `useFetch`. Aligned with CLAUDE.md guidance "most data is build-time cached". |
| No premature Vue Query / no Redux-style global state | Confirmed — neither is installed/used. Matches "do not add Pinia just to imitate Redux". |
| `Footer.vue` is presentation-only | `src/components/Footer.vue:1-5` — pure markup. |

---

## 2. Drift, by severity

### 🔴 Broken / dead code

- **`composables/useDanses.ts` references symbols that don't exist.**
  - `useDanses.ts:5` calls `useNotionDanseStore()` — no Pinia store is defined anywhere in `src/`. `@pinia/nuxt` is installed and registered in `nuxt.config.ts:11`, but there is no `stores/` directory.
  - `useDanses.ts:9` calls `Danse.fromPinia(obj)` — `Danse` (in `src/models/Danse.ts`) only defines `fromNotion`, not `fromPinia`.
  - This composable is also **not imported by any page** — pages call `useFetch('/cache/danses.json')` directly. So it's both broken and unused.
  - **Action**: either delete `useDanses.ts` or finish the work (define the Pinia store, add `Danse.fromPinia`, route pages through the composable). Per `vue-project-guidelines` ("a component should not own network-call logic") the second option is preferred.

- **Stale debug log.** `pages/cours/index.vue:188` — `console.log(type)` inside a `watch`. Remove.

### 🟠 Architecture / boundary leaks

- **Pages own network I/O.** The skill says: "What should not live in a Vue component: `fetch`, `EventSource`, `Date.now()`, `window.location`, non-trivial business logic. Components should consume a composable or props."
  - `pages/danses/index.vue:94`, `pages/danses/[id].vue:69`, `pages/cours/index.vue:159-162`, `pages/photos/index.vue:48`, `pages/photos/[id].vue:66` all call `useFetch('/cache/...')` directly inside `<script setup>`.
  - **Action**: collapse these into composables (`useDanses`, `useCours`, `useAlbums`) so pages consume `{ danses }` instead of doing the fetch themselves. The existing `useDanses` is the natural starting point — fix it (per item above) and reuse the pattern.

- **Notion wire format leaks into the domain.** `models/Cours.ts:13-34` and `models/Danse.ts:10-24` know about Notion's nested response shape (`page.properties?.['Danses apprises']?.relation`, `page.properties?.Nom?.title?.[0]?.plain_text`, etc.).
  - This violates `rules/ARCHITECTURE.md` "Infrastructure adapts to domain — never the reverse" and the anti-pattern "External model leaking into domain".
  - The mapper logic should live next to the prebuild scripts (or in a `SecondaryAdapters/Notion/` folder) and produce plain `Album` / `Cours` / `Danse` instances. The cached JSON consumed at runtime should already be in domain shape, so runtime code shouldn't need a `fromNotion` at all.
  - **Action**: move `fromNotion` static factories out of `models/` and into the script that writes the cache. `models/` should only hold the domain shape.

- **Hardcoded content inside a presentation component.** `pages/index.vue:224-279` defines `detailsDesCoursCountry` — ~60 lines of course data inline. This is real content that belongs in Notion (or at minimum a `public/`/`models/` data file), not in the page's `<script setup>`.
  - **Action**: move to the same Notion/cache pipeline as the rest of the data; the homepage should read from `/cache/cours-summary.json` (or similar).

### 🟡 Smaller code-quality items (transferable from `rules/ANTI-PATTERNS.md`)

- **Anemic models.** `Album.ts`, `Cours.ts`, `Danse.ts` are constructors with all-public fields and zero behavior. Per `ANTI-PATTERNS.md` "Anemic Domain Model" + the skill's "no anemic models" rule:
  - For a content site this is a soft violation — there isn't much real behavior. But fields that are obviously derived (e.g. sorting albums by date in `pages/photos/index.vue:50-56`) should live as methods on the model, not in pages.
  - Public mutable fields (`public id: string` without `readonly`) also drift from the skill's "immutable by default". Add `readonly`.

- **Schema validation is not used despite `zod` being a dependency.** `models/Cours.ts:13` and `models/Danse.ts:10` accept `page: any` and reach into nested optional chains with fallback strings. If Notion changes a field name, code silently produces empty strings instead of failing.
  - **Action**: define a zod schema for the Notion page shape in the prebuild script and validate before serializing to cache.

- **God component**: `pages/photos/[id].vue` (107 lines) mixes fetch, lightbox state, keyboard handling, fullscreen mode, and rendering. Skill: "If a file mixes rendering, network calls, timers, snapshot mapping, and business rules, split it." Extract a `useLightbox` composable.

- **Type safety in routes**: `pages/danses/[id].vue:76` reads `danse.value.nom` outside the `v-if="danse"` guard, in `useHead`. If the URL has an unknown id, this throws at render time. Either redirect on miss or guard the `useHead` call.

### 🟢 Notes (informational, no action required unless you opt in)

- **No test framework is set up.** `package.json` shows no Vitest/Playwright. The skill's testing strategy (priority 1: pure command handlers; helpers `given*`/`when*`/`then*`) is inert until a stack is chosen. CLAUDE.md already documents this.
- **No `Pinia` store exists** even though `@pinia/nuxt` is in deps. Either remove the dep or add the store referenced by `useDanses`.
- **`@nuxt/content` is in deps but no `content/` directory exists.** Either remove the dep or migrate the static text content (homepage paragraphs in `pages/index.vue:155-208`) into Markdown under `content/`.

---

## 3. Suggested order of work

If you want to act on this, the cheapest-first sequence:

1. Delete the `console.log` and either delete or repair `useDanses.ts` + define the missing store and `fromPinia`. Smallest changes, removes a concrete bug.
2. Lift the inline `detailsDesCoursCountry` array out of `pages/index.vue` and into the cache pipeline (or at least into a typed module under `models/`).
3. Move `fromNotion` factories out of `models/` into the prebuild scripts. Add zod validation at that boundary. After this, `models/` is pure types and runtime code never touches Notion shape.
4. Introduce `useDanses` / `useCours` / `useAlbums` composables that wrap the `useFetch('/cache/*.json')` calls so pages stop owning IO.
5. Decide on `@pinia/nuxt` and `@nuxt/content` — either use them or drop them.
6. Only then consider testing: pick Vitest, write the first test against a now-pure helper (e.g. the album sort), and translate the skill's Given/When/Then convention to TS.

Items 1–3 are local refactors with no external surface change. Items 4–6 are larger and worth aligning on before starting.
