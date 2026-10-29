<!-- Generated from references/writing-style.md; edit the source and run scripts/sync-references.py. -->

# Writing Style

**Technical precision in plain language.**

Apply this guidance when writing or updating issues, projects, local work artifacts, and PR titles or descriptions. Write for a technically capable reader who knows neither the current conversation nor every detail of this system. Aim for the voice of a knowledgeable colleague: direct, natural, and specific.

## Make understanding easy

- **Lead with behavior or meaning.** State the gap, resulting behavior, or changed responsibility before explaining the mechanism. Choose detail that helps someone continue the work or review the change.
- **Make cause and effect explicit.** Connect a choice to its reason and a mechanism to its consequence. “The worker checks again before sending because preferences can change after a batch is created” explains more than “Improves preference handling.”
- **Name who or what acts.** Prefer concrete subjects and strong verbs: “The worker checks the saved preference” over “Preference validation is performed.” Keep actors and terminology consistent so readers can follow the relationships.
- **Preserve useful technical terms.** Use the precise term when it helps, with enough context to understand it. Replace abstract wording with observable behavior; explain an unfamiliar boundary or abbreviation without turning the artifact into a tutorial.
- **Write connected sentences.** Give each sentence a clear main point and let the next build on it. Use natural prose and existing section shapes; avoid fragments, stacked clauses, repeated labels, and compressed noun phrases that make readers reconstruct the meaning.
- **Match claims to evidence.** Use wording that distinguishes a proposed approach, implemented behavior, verified result, and remaining uncertainty. Name the relevant check or observation instead of making broad claims such as “Fully validated.”

## Stay readable within the limits

The [work-artifact](work-artifact.md#information-budget) and [PR](pull-request.md) word and section limits still apply. Remove repeated facts, filler, and low-value detail before shortening sentences. Keep the reason, system meaning, and material evidence or limitation; link deeper detail where the artifact guidance allows it. Do not fit more information by packing unrelated claims into a long sentence or replacing clear language with jargon.

Before writing back, re-read from the recipient's perspective: can they follow what happens, why it matters, and what the evidence supports without decoding the prose? Revise unclear passages within the existing budget. This is an editing lens, not an additional output section or checklist.

## Remove generated filler

These constraints apply to issue and PR prose as well as their templates:

- Do not use promotional adjectives such as “seamless,” “robust,” or “comprehensive” in place of evidence; describe the behavior or scope they would need to establish.
- Remove canned framing such as “It's worth noting,” “Importantly,” “This isn't about X; it's about Y,” and concluding recaps that repeat the body.
- Use ordinary verbs instead of inflated wording such as “leverage” or “facilitate” when “use” or “help” expresses the meaning; keep necessary domain terms.
- Avoid invented labels, noun stacks, and activity summaries such as “Implemented enhancements”; name the actor, changed behavior, and relevant reason.
- Do not claim a change is simpler, better, complete, or validated without the concrete comparison or evidence that supports the claim.

Apply these constraints to newly written prose; preserve Original Request, exact quotations, identifiers, and external contracts as required by the artifact guidance.

## Examples

These fictional examples illustrate the voice, not required phrasing.

| Dense or vague | Clear and precise |
| --- | --- |
| Send eligibility is dynamically evaluated against persisted preference state at the dispatch boundary. | Before sending each digest, the worker checks the saved preference and skips recipients who disabled digests. |
| Final authorization responsibility transitions from batch generation to dispatch execution. | The batch selects possible recipients; the worker decides who still receives a digest. |
| Digest suppression has been fully validated. | A regression test confirmed that opting out after batch creation prevents the send; live behavior remains unverified. |

## Sources

Adapted for Equilio Coding from [Google's voice and tone guidance](https://developers.google.com/style/tone), [Microsoft's style and voice tips](https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice), and [Google's technical writing guidance on audience](https://developers.google.com/tech-writing/one/audience). These inform the local guidance; their full conventions are not additional requirements.
