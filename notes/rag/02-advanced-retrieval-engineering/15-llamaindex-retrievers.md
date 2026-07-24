# 15. LlamaIndex Retrievers

> **Category:** Advanced Retrieval Engineering  
> **Module:** Advanced RAG with Vector Databases and Retrievers  
> **Prerequisites:** LlamaIndex Indexes, Vector Databases, RAG Fundamentals  
> **Difficulty:** Intermediate

---

# Overview

While an **Index** organizes data, a **Retriever** determines **how relevant information is retrieved** from that index.

LlamaIndex provides multiple retrievers optimized for different retrieval strategies, allowing developers to balance semantic understanding, keyword matching, document summaries, hierarchical retrieval, and multi-retriever fusion.

According to the IBM course, the major retrievers covered are:

- Vector Index Retriever
- BM25 Retriever
- Document Summary Index Retriever
- Auto Merging Retriever
- Recursive Retriever
- Query Fusion Retriever :contentReference[oaicite:0]{index=0}

---

# Why Multiple Retrievers?

Different applications require different retrieval strategies.

Examples:

- Chatbot → Semantic Search
- Search Engine → Keyword Search
- Research Assistant → Summary Search
- Technical Documentation → Hierarchical Retrieval
- Enterprise Search → Fusion Retrieval

LlamaIndex allows selecting the retrieval strategy independently from the underlying index.

---

# Retriever Architecture

```text
                    User Query
                         │
                         ▼
                 LlamaIndex Retriever
                         │
      ┌──────────────────┼──────────────────┐
      ▼                  ▼                  ▼
 Semantic Search   Keyword Search   Summary Search
      │                  │                  │
      └──────────────────┼──────────────────┘
                         ▼
                 Retrieved Documents
                         │
                         ▼
                         LLM
```

---

# 1. Vector Index Retriever

## Overview

The **Vector Index Retriever** performs semantic retrieval using vector embeddings stored in a **VectorStoreIndex**.

According to IBM, it retrieves semantically related content using vector embeddings and is ideal for general-purpose search and RAG pipelines. :contentReference[oaicite:1]{index=1}

---

## Architecture

```text
User Query
      │
Embedding
      │
Vector Search
      │
Relevant Chunks
```

---

## Implementation

```python
query_engine = index.as_query_engine()

response = query_engine.query(
    "Explain vector databases."
)
```

---

## Best Use Cases

- Enterprise RAG
- Chatbots
- Semantic search
- Technical documentation

---

# 2. BM25 Retriever

## Overview

The **BM25 Retriever** performs keyword-based retrieval instead of semantic similarity.

IBM describes BM25 as a ranking method based on exact keyword matches rather than vector embeddings. :contentReference[oaicite:2]{index=2}

---

## Architecture

```text
User Query
      │
Keyword Matching
      │
BM25 Ranking
      │
Top Documents
```

---

## Implementation

```python
from llama_index.retrievers.bm25 import BM25Retriever

retriever = BM25Retriever.from_defaults(
    index=index
)
```

---

## Best Use Cases

- Legal search
- Compliance
- Source code search
- Product documentation

---

# 3. Document Summary Index Retriever

## Overview

Instead of searching document chunks directly, this retriever searches document summaries first.

IBM explains that the Document Summary Index Retriever uses summaries instead of the original documents and supports two retrieval approaches:

- LLM-based retrieval
- Semantic similarity retrieval :contentReference[oaicite:3]{index=3}

---

## Architecture

```text
User Query
      │
Summary Search
      │
Relevant Documents
      │
Retrieve Full Content
```

---

## Best Use Cases

- Research assistants
- Books
- Long reports
- Large document repositories

---

# 4. Auto Merging Retriever

## Overview

The **Auto Merging Retriever** preserves context by using hierarchical document structures.

According to IBM, it uses hierarchical chunking to split documents into parent and child nodes and automatically merges related child nodes during retrieval. :contentReference[oaicite:4]{index=4}

---

## Architecture

```text
Large Document
      │
Parent Nodes
      │
Child Nodes
      │
Semantic Search
      │
Merge Parent Context
      │
Final Context
```

---

## Best Use Cases

- Technical manuals
- Books
- Research papers
- Long enterprise documentation

---

# 5. Recursive Retriever

## Overview

The **Recursive Retriever** retrieves information by following relationships between nodes.

IBM explains that it traverses references such as citations, hyperlinks, or metadata links to discover additional related content. :contentReference[oaicite:5]{index=5}

---

## Architecture

```text
User Query
      │
Primary Node
      │
Follow References
      │
Related Nodes
      │
Expanded Context
```

---

## Best Use Cases

- Knowledge graphs
- Academic papers
- Documentation with hyperlinks
- Cross-referenced enterprise knowledge

---

# 6. Query Fusion Retriever

## Overview

The **Query Fusion Retriever** combines results from multiple retrievers into a single ranked result.

IBM states that it supports three fusion strategies:

- Reciprocal Rank Fusion (RRF)
- Relative Score Fusion
- Distribution-Based Fusion :contentReference[oaicite:6]{index=6}

---

## Architecture

```text
                User Query
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 Vector Search   BM25 Search   Summary Search
      │              │              │
      └──────────────┼──────────────┘
                     ▼
              Fusion Strategy
                     │
             Ranked Results
                     │
                     ▼
                     LLM
```

---

## Best Use Cases

- Enterprise search
- Hybrid search
- Large knowledge bases
- Production RAG systems

---

# Retriever Comparison

| Retriever | Retrieval Method | Best For |
|------------|------------------|----------|
| Vector Index Retriever | Semantic similarity | General RAG |
| BM25 Retriever | Keyword matching | Legal, compliance |
| Document Summary Retriever | Summary search | Long documents |
| Auto Merging Retriever | Hierarchical retrieval | Context preservation |
| Recursive Retriever | Graph traversal | Linked knowledge |
| Query Fusion Retriever | Multi-retriever fusion | Enterprise search |

---

# Choosing the Right Retriever

| Scenario | Recommended Retriever |
|----------|-----------------------|
| Chatbot | Vector Index Retriever |
| Legal Search | BM25 Retriever |
| Research Assistant | Document Summary Retriever |
| Books | Auto Merging Retriever |
| Knowledge Graph | Recursive Retriever |
| Enterprise Search | Query Fusion Retriever |

---

# Enterprise Use Cases

### Customer Support

**Vector Index Retriever**

Retrieve semantically relevant troubleshooting guides.

---

### Compliance Platform

**BM25 Retriever**

Locate documents using exact regulatory terminology.

---

### Research Portal

**Document Summary Retriever**

Search summaries before retrieving full papers.

---

### Technical Documentation

**Auto Merging Retriever**

Maintain surrounding context when retrieving document sections.

---

### Knowledge Management

**Recursive Retriever**

Traverse linked documents, citations, and references.

---

### Enterprise AI Search

**Query Fusion Retriever**

Combine semantic, keyword, and summary retrieval into a unified ranking.

---

# Production Best Practices

- Match the retriever to the document structure and user queries.
- Use **Vector Index Retriever** as the default for semantic RAG.
- Use **BM25 Retriever** when exact terminology is critical.
- Use **Auto Merging Retriever** for long documents with hierarchical structure.
- Use **Query Fusion Retriever** when combining multiple retrieval strategies improves search quality.

---

# Common Mistakes

❌ Using semantic retrieval for exact keyword searches

❌ Ignoring document hierarchy

❌ Using only one retrieval strategy for every workload

❌ Applying fusion retrieval to very small datasets

❌ Assuming every retriever requires the same index type

---

# Interview Questions

### What is the default retriever in LlamaIndex?

The **Vector Index Retriever**, which retrieves semantically related content using vector embeddings. :contentReference[oaicite:7]{index=7}

---

### How does BM25 differ from the Vector Index Retriever?

BM25 ranks documents using exact keyword matches, whereas the Vector Index Retriever uses semantic similarity. :contentReference[oaicite:8]{index=8}

---

### What is the purpose of the Document Summary Retriever?

It searches document summaries before retrieving the full content and supports both LLM-based and semantic retrieval approaches. :contentReference[oaicite:9]{index=9}

---

### How does the Auto Merging Retriever preserve context?

It retrieves child nodes and automatically merges them into their larger parent context using a hierarchical document structure. :contentReference[oaicite:10]{index=10}

---

### Which fusion strategies are supported by the Query Fusion Retriever?

According to IBM, the supported strategies are:

- Reciprocal Rank Fusion
- Relative Score Fusion
- Distribution-Based Fusion :contentReference[oaicite:11]{index=11}

---

# Quick Revision

```text
Vector Index Retriever
│
├── Semantic Search
└── General RAG

BM25 Retriever
│
├── Keyword Search
└── Exact Matches

Document Summary Retriever
│
├── Summary Search
└── Long Documents

Auto Merging Retriever
│
├── Parent/Child Nodes
└── Context Preservation

Recursive Retriever
│
├── Follow References
└── Knowledge Graphs

Query Fusion Retriever
│
├── Multiple Retrievers
└── Fusion Strategies
```

---

# Key Takeaways

- LlamaIndex offers multiple retrievers, each optimized for a different retrieval strategy.
- **Vector Index Retriever** is the standard choice for semantic RAG.
- **BM25 Retriever** excels at exact keyword matching.
- **Document Summary Retriever** improves retrieval across long documents.
- **Auto Merging Retriever** preserves context using hierarchical chunk relationships.
- **Recursive Retriever** traverses linked nodes to expand retrieved context.
- **Query Fusion Retriever** combines multiple retrieval methods using supported fusion strategies such as Reciprocal Rank Fusion, Relative Score Fusion, and Distribution-Based Fusion. :contentReference[oaicite:12]{index=12}

---

# References

- IBM — *Advanced RAG with Vector Databases and Retrievers* :contentReference[oaicite:13]{index=13}
- LlamaIndex Documentation

---

## Next Note

**16-query-fusion-retriever.md** — Dive deeper into the **Query Fusion Retriever**, its fusion algorithms (Reciprocal Rank Fusion, Relative Score Fusion, and Distribution-Based Fusion), and how it combines multiple retrieval strategies to improve enterprise RAG performance.