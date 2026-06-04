---
name: Cross-AI red-team — verify temporal claims before accepting findings
description: When a cross-AI red-team challenges a name, title, role, or state-of-the-world claim, verify against vault primary sources before treating it as a finding. The reviewer's training cutoff may pre-date the vault state.
type: feedback
originSessionId: 254eda7f-7db4-4f93-b460-1e14e2726754
---
When running a cross-AI red-team and the reviewer pushes back on a name, title, role, or state-of-the-world claim, check the vault's primary sources before accepting the finding. The reviewer's training cutoff may pre-date the claim and produce a confident false negative.

**Why:** On 2026-05-26 during the BDR-FLEET-READINESS §3 red-team, Gemini Pro's Round 1 told us "Caudle is not the CNO, the CNO is Franchetti." The vault's primary source was the 14 May 2026 House Armed Services Committee testimony PDF titled "STATEMENT OF ADMIRAL DARYL L. CAUDLE CHIEF OF NAVAL OPERATIONS." Gemini's training data pre-dated the change. Treating the finding as ground truth would have forced an unnecessary correction. The right move was to push back with the primary source, which Gemini conceded in Round 2.

**How to apply:** When a cross-AI red-team challenges any claim about who holds what role or what the current state of the world is, before accepting:

1. Find the vault primary source the claim cites.
2. Read what the source actually says.
3. If the source supports the claim, push back on the red-team finding with the source text and resolve in dialogue.
4. If the source does not support the claim, the red-team is right — fix the claim.

Generalize: cross-AI red-team is a strong adversarial check on logic, scope, and analytical structure. It is weaker than the vault on temporal facts because the vault holds primary sources captured at known dates while the reviewer holds training data with an older cutoff. Use the cross-AI for structure, use the vault for facts.
