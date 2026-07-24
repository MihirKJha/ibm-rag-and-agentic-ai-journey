# 14. LlamaIndex Indexes

> **Category:** Advanced Retrieval Engineering  
> **Module:** Advanced RAG with Vector Databases and Retrievers  
> **Prerequisites:** Vector Databases, RAG, Embeddings, LangChain Retrievers  
> **Difficulty:** Intermediate

---

# Overview

An **Index** in LlamaIndex is a data structure that organizes documents to make retrieval efficient for Large Language Models (LLMs).

Unlike a vector database, which primarily stores embeddings, LlamaIndex provides multiple index types optimized for different retrieval strategies.

According to the IBM course, the three core LlamaIndex indexes are:

- **VectorStoreIndex**
- **DocumentSummaryIndex**
- **KeywordTableIndex**

Each index is designed for a different retrieval scenario. :contentReference[oaicite:0]{index=0}

---

# Why Multiple Index Types?

Not every application retrieves information the same way.

For example:

- A chatbot benefits from semantic similarity search.
- A research assistant may first search document summaries.
- A compliance system may rely on exact keyword matching.

Instead of one universal index, LlamaIndex provides specialized indexes.

---

# Index Architecture

```text
                    Documents
                         │
                         ▼
                 LlamaIndex
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
VectorStoreIndex  DocumentSummaryIndex  KeywordTableIndex
        │                │                │
        ▼                ▼                ▼
 Semantic Search     Summary Search    Keyword Search
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                    Retrieved Context
                         │
                         ▼
                         LLM
```

---

# 1. VectorStoreIndex

## Overview

The **VectorStoreIndex** is the default and most commonly used index in LlamaIndex.

It stores vector embeddings for each document chunk and retrieves documents using semantic similarity.

According to IBM, the VectorStoreIndex stores vector embeddings for each document chunk and is best suited for semantic retrieval in LLM-powered pipelines. :contentReference[oaicite:1]{index=1}

---

## Architecture

```text
Documents
     │
Chunking
     │
Embeddings
     │
Vector Database
     │
Semantic Search
     │
Relevant Chunks
```

---

## Implementation

```python
from llama_index.core import VectorStoreIndex

index = VectorStoreIndex.from_documents(
    documents
)
```

---

## Query

```python
query_engine = index.as_query_engine()

response = query_engine.query(
    "Explain vector databases."
)

print(response)
```

---

## Best Use Cases

- RAG chatbots
- Enterprise search
- Technical documentation
- Question-answering systems

---

# 2. DocumentSummaryIndex

## Overview

Instead of storing embeddings for every chunk, the **DocumentSummaryIndex** creates and stores summaries for entire documents.

These summaries are searched first to identify the most relevant documents before retrieving their full content.

IBM describes this index as generating and storing document summaries, which are used to filter documents before retrieving their complete content. It is especially useful for large and diverse document collections. :contentReference[oaicite:2]{index=2}

---

## Architecture

```text
Documents
     │
     ▼
Generate Summaries
     │
Store Summaries
     │
Summary Search
     │
Relevant Documents
     │
Retrieve Full Content
```

---

## Implementation

```python
from llama_index.core import DocumentSummaryIndex

index = DocumentSummaryIndex.from_documents(
    documents
)
```

---

## Best Use Cases

- Research assistants
- Long reports
- Books
- Large enterprise knowledge bases

---

# 3. KeywordTableIndex

## Overview

The **KeywordTableIndex** extracts important keywords from documents and maps them to document locations.

Instead of semantic similarity, retrieval is based on keyword matching.

According to IBM, the KeywordTableIndex extracts keywords from documents and maps them to specific content chunks, making it useful for hybrid and rule-based search scenarios. :contentReference[oaicite:3]{index=3}

---

## Architecture

```text
Documents
      │
Keyword Extraction
      │
Keyword Table
      │
Keyword Lookup
      │
Matching Documents
```

---

## Implementation

```python
from llama_index.core import KeywordTableIndex

index = KeywordTableIndex.from_documents(
    documents
)
```

---

## Best Use Cases

- Compliance systems
- Legal search
- Rule-based retrieval
- Exact terminology search

---

# Index Comparison

| Feature | VectorStoreIndex | DocumentSummaryIndex | KeywordTableIndex |
|----------|------------------|----------------------|-------------------|
| Retrieval Method | Semantic Similarity | Document Summaries | Keyword Matching |
| Uses Embeddings | ✅ | Optional | ❌ |
| LLM Required | No (after indexing) | Yes (for summary generation) | No |
| Best for | RAG | Long documents | Exact keyword search |
| Speed | High | Medium | Very High |
| Context Quality | High | High | Medium |

---

# Choosing the Right Index

| Scenario | Recommended Index |
|----------|-------------------|
| Chatbot | VectorStoreIndex |
| Technical documentation | VectorStoreIndex |
| Research assistant | DocumentSummaryIndex |
| Books | DocumentSummaryIndex |
| Legal search | KeywordTableIndex |
| Compliance search | KeywordTableIndex |
| Hybrid enterprise search | Multiple indexes |

---

# Enterprise Use Cases

### Enterprise Knowledge Portal

**VectorStoreIndex**

Semantic search across documentation.

---

### Research Platform

**DocumentSummaryIndex**

Locate the most relevant reports before retrieving detailed sections.

---

### Compliance Management

**KeywordTableIndex**

Find regulations using exact legal terminology.

---

### Technical Support

**VectorStoreIndex**

Retrieve troubleshooting guides based on user intent.

---

# Production Best Practices

- Use **VectorStoreIndex** as the default for most RAG applications.
- Use **DocumentSummaryIndex** when working with long-form documents.
- Use **KeywordTableIndex** when exact terminology is critical.
- Evaluate retrieval quality before selecting an index.
- Consider combining multiple index types for complex enterprise search systems.

---

# Common Mistakes

❌ Using only semantic search when keyword matching is required

❌ Summarizing short documents unnecessarily

❌ Choosing KeywordTableIndex for conversational search

❌ Ignoring document size when selecting an index

❌ Assuming one index fits every application

---

# Interview Questions

### What is the default index in LlamaIndex?

The **VectorStoreIndex**, which stores embeddings for semantic retrieval. :contentReference[oaicite:4]{index=4}

---

### When should you use a DocumentSummaryIndex?

When working with large and diverse document collections where summaries can efficiently identify relevant documents before retrieving full content. :contentReference[oaicite:5]{index=5}

---

### What is the purpose of a KeywordTableIndex?

It extracts keywords from documents and maps them to content chunks for keyword-based retrieval. :contentReference[oaicite:6]{index=6}

---

### Which index is best for semantic search?

VectorStoreIndex.

---

### Can multiple indexes be used together?

The IBM course presents these as distinct index types with different purposes. While LlamaIndex supports more advanced compositions, that is beyond the scope of this lesson. :contentReference[oaicite:7]{index=7}

---

# Quick Revision

```text
VectorStoreIndex
│
├── Stores embeddings
├── Semantic retrieval
└── Best for RAG

DocumentSummaryIndex
│
├── Stores summaries
├── Filters documents first
└── Best for long documents

KeywordTableIndex
│
├── Extracts keywords
├── Exact matching
└── Best for compliance and legal search
```

---

# Key Takeaways

- LlamaIndex provides multiple index types optimized for different retrieval strategies.
- **VectorStoreIndex** is the primary choice for semantic retrieval and RAG applications.
- **DocumentSummaryIndex** improves retrieval for large document collections by searching summaries before full documents.
- **KeywordTableIndex** supports keyword-based retrieval for rule-driven and exact-match scenarios.
- Selecting the appropriate index depends on the retrieval requirements, document characteristics, and application goals. :contentReference[oaicite:8]{index=8}

---

# References

- IBM — *Advanced RAG with Vector Databases and Retrievers* :contentReference[oaicite:9]{index=9}
- LlamaIndex Documentation

---

## Next Note

**15-llamaindex-retrievers.md** — Learn about the major retrievers available in LlamaIndex, including **Vector Index Retriever**, **BM25 Retriever**, **Document Summary Retriever**, **Auto Merging Retriever**, **Recursive Retriever**, and **Query Fusion Retriever**.