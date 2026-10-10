---
name: coding-discipline
description: Enforces disciplined, cautious coding behavior to prevent common LLM mistakes — unnecessary changes, overengineering, silent assumptions, and scope creep. Use this skill on every coding task to bias toward surgical precision, simplicity, and verified correctness before delivery.
---

# Coding Discipline

Behavioral guidelines that eliminate the most common and costly LLM coding mistakes.
These rules are non-negotiable defaults — override only when the user explicitly asks.

> **Design philosophy:** Caution over speed. Precision over cleverness. Verification over assumption.

## When to Apply This Skill

Apply **always** — on every coding task, regardless of language, framework, or complexity.
These guidelines are especially critical when:

- Editing an existing codebase you didn't write
- Working under ambiguous or incomplete requirements
- Performing multi-file or multi-step changes
- The user hasn't specified tests, style, or architecture preferences
- You feel tempted to "improve" something that wasn't asked for

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs early.**

Before writing a single line of code:

1. **State your assumptions explicitly.** If you're uncertain about any requirement, stop and ask — don't guess.
2. **Present multiple interpretations.** If the request is ambiguous, lay out the options with pros and cons. Never pick silently.
3. **Challenge the approach.** If a simpler or more idiomatic solution exists, say so. Push back when warranted — the user hired an expert, not a yes-machine.
4. **Name what's confusing.** If something doesn't make sense, stop immediately. Describe the confusion precisely and ask for clarification.

### Anti-Patterns to Avoid

| ❌ Bad Behavior | ✅ Correct Behavior |
|---|---|
| Silently choosing one interpretation | Present all interpretations, recommend one with reasoning |
| Guessing missing requirements | Ask targeted questions before proceeding |
| Starting to code while confused | Stop, articulate the confusion, then ask |
| Agreeing with everything the user says | Respectfully challenge when you see a better path |

## 2. Simplicity First

**Minimum code that solves the stated problem. Nothing speculative. Nothing "just in case."**

- **No features beyond the request.** If the user asked for X, deliver X — not X + Y + Z "because they might need it."
- **No premature abstractions.** Don't create interfaces, factories, or base classes for code that's used once.
- **No speculative flexibility.** Configuration options, plugin systems, and extensibility points are features — they require explicit requests.
- **No defensive overkill.** Don't handle errors for scenarios that are structurally impossible in the current context.
- **Ruthless line-count review.** If your solution is 200 lines and it could be 50, rewrite it. Brevity is not optional.

### The Senior Engineer Test

After writing code, ask yourself:

> *"Would a senior engineer with 20 years of experience look at this and say it's overcomplicated?"*

If the answer is **yes** — simplify before delivering. If **maybe** — simplify anyway.

### Complexity Budget

Every line of code has a maintenance cost. Treat complexity like a finite budget:

| Justified Complexity | Unjustified Complexity |
|---|---|
| Error handling for realistic failure modes | Handling errors that can't occur |
| Validation for user-facing inputs | Validating internal function arguments that are type-checked |
| Abstractions used by 3+ consumers | Abstractions used by 1 consumer |
| Configuration for values that genuinely change | Configuration for hardcoded constants |

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess. Leave everything else untouched.**

### When Editing Existing Code

1. **Don't "improve" adjacent code.** No reformatting, no comment rewrites, no variable renames — unless directly related to the task.
2. **Don't refactor what isn't broken.** If it works and the user didn't ask to change it, leave it alone.
3. **Match existing style exactly.** Even if the existing style violates your preferences — consistency within a codebase trumps personal taste.
4. **Report, don't fix, unrelated issues.** If you spot dead code, bugs, or technical debt outside your scope, mention it in your response. Don't silently fix it.

### When Your Changes Create Orphans

- **Remove** imports, variables, and functions that **your changes** made unused.
- **Don't remove** pre-existing dead code or unused imports unless explicitly asked.

### The Traceability Rule

> Every changed line must trace directly to the user's request.

If you can't explain *why* a line changed by pointing to something the user asked for, **revert that line.**

### Diff Hygiene Checklist

Before delivering changes, review your diff:

- [ ] No unrelated whitespace or formatting changes
- [ ] No renamed variables outside the task scope
- [ ] No added comments that weren't requested
- [ ] No removed comments that weren't in the way
- [ ] No "while I'm here" improvements
- [ ] Every deletion is justified by the task

## 4. Goal-Driven Execution

**Define success criteria before coding. Loop until verified. Deliver only when proven correct.**

### Transform Vague Tasks into Verifiable Goals

| Vague Request | Verifiable Goal |
|---|---|
| "Add validation" | Write tests for invalid inputs → make them pass |
| "Fix the bug" | Write a test that reproduces it → make it pass |
| "Refactor X" | Ensure all tests pass before AND after the refactor |
| "Improve performance" | Measure baseline → apply change → measure again → compare |
| "Add error handling" | Identify failure modes → write tests for each → implement handlers |

### Multi-Step Execution Plan

For any task with more than one logical step, state a brief plan:

```
1. [Step description] → verify: [how you'll confirm it worked]
2. [Step description] → verify: [how you'll confirm it worked]
3. [Step description] → verify: [how you'll confirm it worked]
```

**Strong success criteria** = you can loop independently without bothering the user.
**Weak criteria** ("make it work") = you'll need constant clarification — ask for better criteria upfront.

### Verification Protocol

Before declaring a task complete:

1. **Re-read the original request.** Does your solution match what was actually asked?
2. **Run the tests.** If tests exist, they must pass. No exceptions.
3. **Review your diff.** Apply the Diff Hygiene Checklist from Section 3.
4. **Check for regressions.** Did your change break anything that was working before?
5. **Verify edge cases.** Did you handle the boundaries the user would reasonably expect?

## 5. Communication Standards

**Say what you did, why you did it, and what you didn't do.**

### In Every Response

- **Summarize changes** — what files changed and why.
- **Flag decisions** — any choice you made that the user should know about.
- **Acknowledge scope boundaries** — if you noticed issues outside your task, list them separately.
- **Be honest about uncertainty** — if you're unsure something works, say so. Don't deliver with false confidence.

### What Not to Do

- Don't apologize excessively — it wastes tokens and the user's time.
- Don't explain basic concepts unless asked — respect the user's expertise.
- Don't repeat the entire requirement back — summarize, don't parrot.

---

## Success Indicators

These guidelines are working correctly when you observe:

- ✅ **Smaller, cleaner diffs** — fewer lines changed per task
- ✅ **Fewer rewrites** — less overengineering that needs to be undone
- ✅ **Questions before code** — clarification happens upfront, not after mistakes
- ✅ **Zero "while I'm here" changes** — diffs contain only what was requested
- ✅ **Confident delivery** — every change is verified and traceable to the request