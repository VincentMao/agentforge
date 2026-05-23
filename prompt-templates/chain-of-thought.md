# Chain of Thought Pattern

## When to Use

Use for **complex reasoning tasks** where the answer depends on intermediate steps. Forcing explicit reasoning prevents "shortcut" errors where the model jumps to a plausible-sounding answer that skips critical logic.

Best for: algorithm selection, data structure design, system design trade-offs, mathematical reasoning, multi-constraint optimization.

**Do not use for simple lookups or tasks with obvious answers** — chain-of-thought adds tokens without adding quality when the reasoning path is trivial.

## The Pattern

```
PROMPT:
Think through this step by step before giving your final answer.
Show your reasoning at each step.
Only give your final answer after completing your reasoning chain.

[problem statement]
```

## Worked Example: Data Structure Selection

```
Problem: We need a cache with O(1) get/set and LRU eviction. Choose the data structure.

Step 1: What operations do we need?
- get(key) → value: O(1)
- set(key, value): O(1), evicts LRU entry if at capacity
- Eviction: O(1) removal of the least-recently-used entry

Step 2: What gives O(1) get/set?
- HashMap: O(1) get/set, but no ordering → can't identify LRU in O(1)
- Array: O(1) by index, but O(n) search → wrong
- Balanced BST: O(log n) → wrong

Step 3: What gives O(1) LRU identification and removal?
- Doubly-linked list: O(1) removal from any position IF we have a pointer to that node
- But: iteration to find LRU is O(n) without a pointer

Step 4: Can we combine?
- HashMap stores key → node pointer (the node is in the doubly-linked list)
- Doubly-linked list maintains access order: head = MRU, tail = LRU
- get: O(1) hashmap lookup → O(1) move to head
- set: O(1) insert at head. If at capacity: O(1) remove tail (LRU), O(1) delete from hashmap
- All operations O(1) ✓

Final Answer: HashMap + doubly-linked list (the standard LRU cache).
```

## Worked Example: Algorithm Selection

```
Problem: We have 10M log entries. We need to find the top-100 most frequent IPs.
         Memory is limited to 1GB. What algorithm?

Step 1: Brute force?
- Sort all 10M entries: O(n log n) time, O(n) space
- Then scan for top-100: O(n)
- 10M entries × ~50 bytes = ~500MB — fits in 1GB
- But sort is slow and uses all memory

Step 2: Better approach — counting then selection?
- HashMap of IP → count: O(n) time, O(k) space where k = unique IPs
- Then find top-100 from the map: min-heap of size 100, O(n log 100) = O(n)
- Memory: up to ~100M unique IPs × ~50 bytes = 5GB → might not fit

Step 3: What if k is large?
- Use Count-Min Sketch for approximate counts: O(1) per update, O(ε·n) space
- Then exact-count only the candidates: back to HashMap but for fewer IPs
- Acceptable for log analysis (approximate top-100 is fine)

Final Answer: For exact results: HashMap + min-heap (2 passes). If memory is tight:
             Count-Min Sketch for candidate filtering, then exact count.
             Given 1GB limit, test k first — if unique IPs < 10M, HashMap works exactly.
```

## Variants

**Self-consistency CoT**: Generate 3 independent reasoning chains, take the majority answer. Useful for high-stakes decisions where a single chain might make a systematic error.

**Zero-shot CoT**: Simply append "Let's think step by step." Works for mathematical reasoning; less reliable for code or architecture decisions (use explicit structured prompts instead).

## When NOT to Use

- Simple factual lookups
- Code generation with a complete and unambiguous spec
- Tasks where you've already verified the answer is obvious

## Anti-Patterns

| ❌ | ✅ |
|---|---|
| Jump to answer without steps | Work through each step explicitly |
| Steps that don't build on each other | Each step uses conclusions from prior steps |
| "Step 1: Think about it" | Concrete intermediate conclusions at each step |
| Use for obvious tasks | Reserve for tasks where intermediate reasoning changes the outcome |
