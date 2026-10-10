# Proof of Work / Acceptance Evidence

"Done" is not evidence.

Before acceptance, collect the smallest sufficient proof:
- relevant test/lint/typecheck/build results,
- final diff review,
- security review for critical security-sensitive changes,
- independent review for configured high-risk changes,
- explicit unresolved risks/limitations,
- evidence events recording retries and verification outcomes.

A passing gate proves only what that gate checks. The parent must still compare the implementation against the original acceptance criteria.
