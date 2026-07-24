# 16. Query Fusion Retriever

> **Category:** Advanced Retrieval Engineering  
> **Module:** Advanced RAG with Vector Databases and Retrievers  
> **Prerequisites:** Vector Index Retriever, BM25 Retriever, Document Summary Retriever, Auto Merging Retriever  
> **Difficulty:** Advanced

---

# Overview

A **Query Fusion Retriever** improves retrieval quality by combining the results from **multiple retrievers** into a single ranked list.

Instead of relying on only one retrieval strategy, it executes several retrieval methods in parallel and merges their results using a **fusion algorithm**.

According to the IBM course, the Query Fusion Retriever combines the outputs of different retrievers using one of three supported fusion strategies:

- **Reciprocal Rank Fusion (RRF)**
- **Relative Score Fusion**
- **Distribution-Based Fusion** :contentReference[oaicite:0]{index=0}

---

# Why Use Query Fusion?

Every retriever has strengths and weaknesses.

| Retriever | Strength | Weakness |
|-----------|-----------|-----------|
| Vector Retriever | Semantic understanding | Misses exact keywords |
| BM25 Retriever | Exact keyword matching | Misses semantic meaning |
| Summary Retriever | Excellent for long documents | May overlook detailed chunks |

Instead of choosing one retriever, Query Fusion combines all of them.

---

# Architecture

```text
                    User Query
                         │
                         ▼
              Query Fusion Retriever
                         │
      ┌──────────────────┼──────────────────┐
      ▼                  ▼                  ▼
 Vector Retriever    BM25 Retriever   Summary Retriever
      │                  │                  │
      ▼                  ▼                  ▼
 Ranked Results     Ranked Results    Ranked Results
      └──────────────────┼──────────────────┘
                         ▼
                 Fusion Strategy
                         │
                  Unified Ranking
                         │
                         ▼
                  Final Documents
                         │
                         ▼
                         LLM
```

---

# How It Works

### Step 1 — Receive the query

```
Explain Kubernetes networking.
```

---

### Step 2 — Execute multiple retrievers

The system may run:

- Vector Index Retriever
- BM25 Retriever
- Document Summary Retriever

simultaneously.

---

### Step 3 — Collect ranked results

Example

**Vector Retriever**

```
Doc A

Doc C

Doc D
```

**BM25**

```
Doc B

Doc A

Doc E
```

**Summary Retriever**

```
Doc A

Doc F

Doc D
```

---

### Step 4 — Apply fusion strategy

The Query Fusion Retriever combines these rankings into a single ranked list.

---

### Step 5 — Return the final documents

```
Doc A

Doc B

Doc D

Doc C

Doc F
```

These documents are passed to the LLM.

---

# Fusion Strategies

The IBM course introduces three supported fusion strategies.

---

# 1. Reciprocal Rank Fusion (RRF)

## Overview

Instead of using raw similarity scores, Reciprocal Rank Fusion combines the **rank positions** assigned by different retrievers.

Documents that consistently appear near the top across multiple retrievers receive the highest combined ranking.

IBM identifies Reciprocal Rank Fusion as one of the supported fusion strategies. :contentReference[oaicite:1]{index=1}

---

### Example

| Document | Vector Rank | BM25 Rank | Final Score |
|----------|------------:|----------:|------------:|
| Doc A | 1 | 2 | Highest |
| Doc B | 4 | 1 | High |
| Doc C | 2 | 5 | Medium |

---

### Best For

- Enterprise search
- Mixed retrieval methods
- Stable ranking across retrievers

---

# 2. Relative Score Fusion

## Overview

Relative Score Fusion combines the **normalized similarity scores** from different retrievers.

Instead of considering only document positions, it also evaluates how strongly each retriever matches the query.

IBM lists Relative Score Fusion as a supported strategy. :contentReference[oaicite:2]{index=2}

---

### Example

| Retriever | Raw Score | Normalized Score |
|-----------|----------:|-----------------:|
| Vector | 0.93 | 0.95 |
| BM25 | 12.1 | 0.88 |
| Summary | 0.84 | 0.86 |

Combined score

```
0.95 + 0.88 + 0.86
```

---

### Best For

- Hybrid retrieval
- Mixed similarity metrics
- Production ranking

---

# 3. Distribution-Based Fusion

## Overview

Distribution-Based Fusion considers the statistical distribution of scores produced by each retriever before combining them.

This reduces the impact of retrievers whose scoring ranges differ significantly.

IBM identifies Distribution-Based Fusion as the third supported fusion strategy. :contentReference[oaicite:3]{index=3}

---

### Best For

- Large enterprise search
- Multiple heterogeneous retrievers
- Different scoring distributions

---

# Query Fusion Workflow

```text
User Query
      │
      ▼
Run Multiple Retrievers
      │
      ├─────────────► Vector
      │
      ├─────────────► BM25
      │
      └─────────────► Summary
                     │
                     ▼
           Collect Rankings
                     │
                     ▼
          Apply Fusion Strategy
                     │
                     ▼
          Unified Ranked Results
                     │
                     ▼
                     LLM
```

---

# Example Retrieval

Suppose a user asks:

```
Explain Kubernetes networking.
```

### Vector Retriever

```
Networking Guide

Cluster Networking

Pods
```

### BM25 Retriever

```
Networking Guide

Ingress

Services
```

### Summary Retriever

```
Kubernetes Handbook

Networking Guide
```

Fusion ranking

```
1. Networking Guide

2. Kubernetes Handbook

3. Cluster Networking

4. Ingress

5. Services
```

---

# LlamaIndex Example

```python
from llama_index.core.retrievers import QueryFusionRetriever

retriever = QueryFusionRetriever(
    retrievers=[
        vector_retriever,
        bm25_retriever,
    ]
)
```

---

## Retrieve Documents

```python
nodes = retriever.retrieve(
    "Explain Kubernetes networking."
)

for node in nodes:
    print(node.text)
```

> **Note:** The IBM course demonstrates the concept and supported fusion strategies but does not provide implementation code for configuring specific fusion algorithms. :contentReference[oaicite:4]{index=4}

---

# Comparison of Fusion Strategies

| Strategy | Uses Ranking | Uses Scores | Best For |
|-----------|--------------|-------------|----------|
| Reciprocal Rank Fusion | ✅ | ❌ | Stable rankings |
| Relative Score Fusion | ❌ | ✅ | Hybrid retrieval |
| Distribution-Based Fusion | ✅ | ✅ | Enterprise-scale search |

---

# Enterprise Use Cases

### Enterprise Search

Combine semantic search and keyword search.

---

### Legal Research

Fuse BM25 with semantic retrieval.

---

### Research Portals

Combine summary retrieval with semantic retrieval.

---

### Internal Knowledge Bases

Retrieve information from multiple retrieval pipelines simultaneously.

---

### Production RAG

Improve both recall and ranking quality.

---

# Production Best Practices

- Combine retrievers with complementary strengths.
- Evaluate retrieval quality using recall and precision metrics.
- Use Reciprocal Rank Fusion when retrievers produce reliable rankings.
- Use score-based fusion when similarity scores are meaningful.
- Benchmark different fusion strategies before deploying to production.

---

# Common Mistakes

❌ Combining identical retrievers

❌ Assuming more retrievers always improve results

❌ Ignoring latency introduced by multiple retrieval passes

❌ Mixing incompatible scoring systems without normalization

❌ Evaluating only the LLM instead of the retrieval pipeline

---

# Interview Questions

### What problem does the Query Fusion Retriever solve?

It combines multiple retrieval strategies into a single ranked result to improve retrieval quality. :contentReference[oaicite:5]{index=5}

---

### Which fusion strategies are supported?

According to IBM:

- Reciprocal Rank Fusion
- Relative Score Fusion
- Distribution-Based Fusion :contentReference[oaicite:6]{index=6}

---

### Why use multiple retrievers?

Different retrievers capture different types of relevance, such as semantic similarity, keyword matching, or document summaries.

---

### When is Query Fusion most useful?

For enterprise search systems, hybrid search, and large knowledge bases where multiple retrieval methods complement one another.

---

### Does the IBM course recommend one fusion strategy over another?

No. The course identifies the three supported fusion strategies but does not rank or recommend one over the others. :contentReference[oaicite:7]{index=7}

---

# Quick Revision

```text
User Query
      │
      ▼
Multiple Retrievers
│        │        │
▼        ▼        ▼
Vector   BM25   Summary
      │
      ▼
Fusion Strategy
│
├── Reciprocal Rank Fusion
├── Relative Score Fusion
└── Distribution-Based Fusion
      │
      ▼
Unified Ranking
      │
      ▼
LLM
```

---

# Key Takeaways

- Query Fusion Retriever combines multiple retrieval strategies into a single ranked result.
- It improves retrieval robustness by leveraging the strengths of different retrievers.
- The IBM course introduces three supported fusion strategies:
  - **Reciprocal Rank Fusion (RRF)**
  - **Relative Score Fusion**
  - **Distribution-Based Fusion**
- Query Fusion is particularly valuable in enterprise RAG systems where semantic, keyword, and summary-based retrieval need to work together. :contentReference[oaicite:8]{index=8}

---

# References

- IBM — *Advanced RAG with Vector Databases and Retrievers* :contentReference[oaicite:9]{index=9}
- LlamaIndex Documentation

---

## Next Note

**17-faiss-fundamentals.md** — Learn the fundamentals of **Facebook AI Similarity Search (FAISS)**, including its architecture, vector indexing concepts, and why it is widely used for scalable similarity search in production RAG systems.