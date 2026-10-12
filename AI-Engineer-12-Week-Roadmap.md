# AI Engineer — 12-Week Roadmap

> Goal: Go from beginner to job-ready AI engineer in 12 weeks.
> Rule: Don't move to the next topic until you've solved at least the Easy and Medium problems.

---

## PHASE 1 — Weeks 1–3: Build the Foundation
**Goal: Strong Programming Foundation**

---

### Topic 1 — Python Basics → OOP

#### What to Learn

**Variables & Data Types**
A variable stores a value. Python figures out the type automatically.
```python
name = "Alice"        # str — text
age = 30              # int — whole number
score = 98.5          # float — decimal
is_active = True      # bool — True or False
```

**f-strings**
The cleanest way to embed variables inside a string.
```python
name = "Alice"
age = 30
print(f"Hello {name}, you are {age} years old.")
# → Hello Alice, you are 30 years old.
```

**Lists**
An ordered collection of items. Index starts at 0.
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])       # apple
fruits.append("mango") # add to end
fruits.remove("banana")# remove by value
print(len(fruits))     # 3
```

**Dictionaries**
Key-value pairs — like a real dictionary. Keys must be unique.
```python
person = {"name": "Alice", "age": 30, "city": "NYC"}
print(person["name"])        # Alice
person["email"] = "a@b.com" # add new key
del person["city"]           # remove a key
print(person.keys())         # dict_keys(['name', 'age', 'email'])
```

**Loops**
```python
# for loop — iterate over a list
for fruit in ["apple", "banana"]:
    print(fruit)

# while loop — keep going until condition is False
count = 0
while count < 3:
    print(count)
    count += 1

# range() — generate numbers
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)
```

**Conditions**
```python
score = 75
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")
```

**Functions**
Reusable blocks of code. Use `return` to send a value back.
```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # 7
```

**Classes & OOP**
A class is a blueprint for creating objects. `self` refers to the specific object being created.
```python
class Dog:
    def __init__(self, name, breed):  # runs when you create a Dog
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

rex = Dog("Rex", "Labrador")
print(rex.bark())  # Rex says woof!
```

**Inheritance**
A child class inherits everything from the parent and can add or override methods.
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Cat(Animal):          # Cat inherits from Animal
    def speak(self):        # overrides parent method
        return f"{self.name} says meow!"

cat = Cat("Whiskers")
print(cat.speak())  # Whiskers says meow!
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Write a `Student` class with `name` and `grade` attributes and a method `is_passing()` that returns `True` if grade >= 50. Create 3 students and print which ones are passing. |
| 🟡 Medium | Build a `BankAccount` class with `deposit()`, `withdraw()`, and `balance` — `withdraw()` should raise an error if funds are insufficient. Write a `SavingsAccount` subclass that adds 2% interest monthly via an `apply_interest()` method. |
| 🔴 Hard | Build a `Library` system with `Book`, `Member`, and `Library` classes. Members can borrow/return books. Library tracks who has which book, prevents borrowing unavailable books, and can print a full inventory report showing borrowed vs available books. |

---

### Topic 2 — Git & GitHub

#### What to Learn

**What Git is**
Git is a version control system — it tracks every change you make to your code so you can go back in time, work on features separately, and collaborate with others.

**Core Concepts**
- **Repository (repo):** A folder Git is tracking
- **Commit:** A saved snapshot of your code at a point in time
- **Branch:** A parallel version of your code (so you can build features without breaking main)
- **Remote:** The copy of your repo hosted online (e.g. GitHub)

**Essential Commands**
```bash
# Start tracking a folder
git init

# See what's changed
git status

# Stage a file (mark it for the next commit)
git add filename.py
git add .              # stage everything

# Save a snapshot with a message
git commit -m "add tip calculator"

# See history
git log --oneline

# Connect to GitHub and push
git remote add origin https://github.com/yourname/repo.git
git push -u origin main

# Download latest changes from GitHub
git pull
```

**Branches**
```bash
# Create and switch to a new branch
git checkout -b feature/weather

# Switch back to main
git checkout main

# Merge your feature branch into main
git merge feature/weather

# Delete the branch after merging
git branch -d feature/weather
```

**What a good commit message looks like**
```
add weather lookup feature       ✅ clear and specific
fixed stuff                      ❌ useless
```

**README.md**
Every repo should have one. It's the first thing people see on GitHub.
```markdown
# Project Name
One-sentence description.

## How to run
pip install requests
python3 weather.py

## Example
$ python3 weather.py
Enter city: London
Temperature: 18°C, Cloudy
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Create a local repo, make 3 commits (each changing one file), push to GitHub, and verify `git log --oneline` shows all 3. |
| 🟡 Medium | Create a `feature/calculator` branch, add a calculator script, commit it, switch back to `main`, merge the branch, and push. Write a `README.md` explaining how to run the script. |
| 🔴 Hard | Simulate a real workflow: create a branch, make changes, intentionally create a merge conflict with `main`, resolve the conflict manually, commit the resolution, and push. Document the process in a `CONTRIBUTING.md` file. |

---

### Topic 3 — REST APIs & JSON

#### What to Learn

**What an API is**
An API (Application Programming Interface) is a way for your code to talk to someone else's server. You send a request, they send back data.

**HTTP Methods**
| Method | When to use |
|---|---|
| GET | Fetch data (read-only) |
| POST | Send data to create something |
| PUT | Replace an existing resource |
| DELETE | Remove something |

**Status Codes**
| Code | Meaning |
|---|---|
| 200 | OK — success |
| 201 | Created — resource made successfully |
| 400 | Bad Request — you sent something wrong |
| 401 | Unauthorized — missing/wrong credentials |
| 404 | Not Found — that URL doesn't exist |
| 500 | Server Error — their problem, not yours |

**Making a GET request with `requests`**
```python
import requests

response = requests.get("https://api.agify.io?name=alice")
print(response.status_code)  # 200
print(response.json())       # {'name': 'alice', 'age': 28, 'count': 12345}

data = response.json()
print(f"Predicted age: {data['age']}")
```

**Handling errors**
```python
response = requests.get("https://api.agify.io?name=alice")

if response.status_code == 200:
    data = response.json()
    print(data["age"])
else:
    print(f"Error: {response.status_code}")
```

**JSON**
JSON (JavaScript Object Notation) is the data format APIs use. It looks like Python dicts and lists.
```python
import json

# Python dict → JSON string
data = {"name": "Alice", "scores": [95, 87, 92]}
json_string = json.dumps(data, indent=2)
print(json_string)

# JSON string → Python dict
raw = '{"name": "Alice", "age": 30}'
parsed = json.loads(raw)
print(parsed["name"])  # Alice
```

**Passing query parameters**
```python
# Both of these are the same:
requests.get("https://api.agify.io?name=alice")
requests.get("https://api.agify.io", params={"name": "alice"})
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Call `https://api.agify.io?name=yourname` — parse the JSON and print: `"The predicted age for [name] is [age]."` |
| 🟡 Medium | Build a weather CLI — user types a city name, your script calls `wttr.in/{city}?format=j1`, parses the JSON, and prints temperature, condition, humidity, and wind speed in a clean format. Handle city-not-found errors. |
| 🔴 Hard | Build a multi-API profile generator — takes a first name, calls Agify (age), Genderize (gender), and Nationalize (nationality) APIs concurrently using `concurrent.futures`, then prints a formatted profile. Cache results to a JSON file so repeat lookups don't hit the API. |

---

### Topic 4 — SQL Basics

#### What to Learn

**What SQL is**
SQL (Structured Query Language) is how you talk to a database. SQLite is a file-based database — no server needed, perfect for learning.

```python
import sqlite3
conn = sqlite3.connect("mydb.db")  # creates the file if it doesn't exist
cursor = conn.cursor()
```

**CREATE TABLE**
Define the structure of your data.
```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    grade INTEGER
);
```

**INSERT**
Add a row.
```sql
INSERT INTO students (name, grade) VALUES ('Alice', 85);
INSERT INTO students (name, grade) VALUES ('Bob', 42);
```

**SELECT**
Fetch rows.
```sql
SELECT * FROM students;                          -- all rows, all columns
SELECT name, grade FROM students;                -- specific columns
SELECT * FROM students WHERE grade >= 70;        -- filter
SELECT * FROM students ORDER BY grade DESC;      -- sort
SELECT * FROM students LIMIT 3;                  -- first 3 rows
```

**UPDATE & DELETE**
```sql
UPDATE students SET grade = 90 WHERE name = 'Bob';
DELETE FROM students WHERE grade < 50;
```

**GROUP BY & aggregate functions**
```sql
SELECT AVG(grade) FROM students;               -- average
SELECT MAX(grade), MIN(grade) FROM students;   -- max and min
SELECT grade, COUNT(*) FROM students GROUP BY grade;  -- count per grade
```

**JOIN — combining two tables**
```sql
-- orders table has a customer_id column that links to customers.id
SELECT customers.name, orders.amount
FROM orders
JOIN customers ON orders.customer_id = customers.id;
```

**Using SQLite in Python**
```python
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)")
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Alice", 85))
conn.commit()

cursor.execute("SELECT * FROM students WHERE grade >= 70")
rows = cursor.fetchall()
for row in rows:
    print(row)  # (1, 'Alice', 85)

conn.close()
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Create a SQLite database with a `students` table (id, name, grade). Insert 5 rows, then query all students with grade >= 70 and print their names sorted alphabetically. |
| 🟡 Medium | Build a contacts app backed by SQLite — functions to `add_contact`, `search_by_name`, `update_phone`, `delete_contact`. All data persists between script runs. |
| 🔴 Hard | Create two tables — `orders` and `customers` — with a foreign key relationship. Write queries to: (1) find the top 3 customers by total spend, (2) find all customers who haven't ordered in the last 30 days, (3) calculate average order value per customer. |

---

### Topic 5 — Prompt Engineering

#### What to Learn

**What prompt engineering is**
The skill of writing instructions to an LLM to get the output you want. The quality of your prompt directly determines the quality of the response.

**System Prompts**
Set the AI's persona, rules, and behavior before the conversation starts. The user never sees this.
```python
import anthropic
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    system="You are a concise technical assistant. Always answer in bullet points. Never use more than 5 bullets.",
    messages=[{"role": "user", "content": "How does the internet work?"}]
)
print(response.content[0].text)
```

**Few-shot Prompting**
Show the model examples of what you want before asking your question. This dramatically improves output quality.
```python
prompt = """
Classify the sentiment of these reviews:

Review: "The product broke after 2 days." → Negative
Review: "Absolutely love it, best purchase ever!" → Positive
Review: "It's fine, does what it says." → Neutral

Review: "Terrible customer service, never buying again." →
"""
```

**Chain-of-Thought (CoT)**
Force the model to reason step by step before answering. Improves accuracy on complex tasks.
```python
prompt = """
Solve this step by step, showing your reasoning before giving the final answer.

Problem: A store has 120 apples. They sell 40% on Monday and receive 30 new ones on Tuesday. How many are left?

Reasoning:
"""
```

**Structured Output (JSON)**
Ask the model to return data in a specific format you can parse.
```python
prompt = """
Analyze this text and return ONLY valid JSON. No explanation, no markdown.

Format:
{
  "sentiment": "positive" | "negative" | "neutral",
  "confidence": 0-100,
  "keywords": ["word1", "word2", "word3"]
}

Text: "The new iPhone is incredible but the price is way too high."
"""
```

**Temperature**
Controls randomness. Low = predictable and consistent. High = creative and varied.
```python
# For factual tasks (data extraction, code, JSON output)
response = client.messages.create(model="claude-sonnet-5", max_tokens=500,
    messages=[{"role": "user", "content": "What is 2+2?"}])
# temperature defaults to 1.0 — for JSON output, keep prompts very explicit

# Claude doesn't expose a temperature param in the same way,
# but other providers (OpenAI) do:
# openai_client.chat.completions.create(temperature=0.2)  # focused
# openai_client.chat.completions.create(temperature=1.5)  # creative
```

**Prompt patterns that work**
```
"Return ONLY JSON. No explanation."          → forces structured output
"Think step by step."                        → improves reasoning
"You are an expert [X]. Answer as [X]."      → sets context/persona
"Here are 3 examples: ... Now do the same:"  → few-shot
"If you don't know, say 'I don't know'."     → reduces hallucination
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Write 3 different system prompts that make Claude respond as: (1) a pirate, (2) a formal lawyer, (3) a 5-year-old. Ask each the same question and compare the outputs. |
| 🟡 Medium | Build a prompt that makes Claude reliably return JSON with fields `sentiment`, `confidence` (0–100), and `reason` for any text you send. Test it on 5 different inputs and confirm the JSON is always valid and parseable. |
| 🔴 Hard | Design a chain-of-thought prompt that solves multi-step math word problems. The prompt must force Claude to show its reasoning step by step before giving the final answer. Test on 5 problems and compare accuracy with and without chain-of-thought. |

---

### Topic 6 — Python Projects (Foundation)

#### What to Learn

**Files — reading and writing**
```python
# Write to a file
with open("notes.txt", "w") as f:
    f.write("Hello world\n")
    f.write("Second line\n")

# Read entire file
with open("notes.txt", "r") as f:
    content = f.read()

# Read line by line
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# Append without overwriting
with open("notes.txt", "a") as f:
    f.write("New line added\n")
```

**JSON files — saving and loading structured data**
```python
import json

data = {"contacts": [{"name": "Alice", "phone": "555-1234"}]}

# Save to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Load from file
with open("data.json", "r") as f:
    loaded = json.load(f)

print(loaded["contacts"][0]["name"])  # Alice
```

**Error handling**
```python
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {"contacts": []}   # start fresh if file doesn't exist
except json.JSONDecodeError:
    print("File is corrupted")
    data = {"contacts": []}
```

**Input validation**
```python
while True:
    age = input("Enter your age: ")
    if age.isdigit() and int(age) > 0:
        age = int(age)
        break
    print("Please enter a valid positive number.")
```

**Building a CLI loop**
```python
while True:
    command = input("\nCommand (add/list/quit): ").strip().lower()
    if command == "quit":
        break
    elif command == "add":
        name = input("Name: ")
        # do something
    elif command == "list":
        # show data
        pass
    else:
        print("Unknown command.")
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Build a CLI contact book — stores contacts in a JSON file, supports add/search/delete, persists between runs. |
| 🟡 Medium | Build a personal expense tracker — stores entries in SQLite (date, category, amount, note), supports adding entries and querying by category or date range, prints a monthly summary. |
| 🔴 Hard | Build a news aggregator CLI — fetches headlines from a free news API, lets the user filter by category, saves favorites to a local JSON file, and uses Claude to generate a one-sentence summary for each article. |

---

## PHASE 2 — Weeks 4–6: Master AI & LLMs
**Goal: Understand Modern AI Systems**

---

### Topic 7 — AI & Machine Learning Fundamentals

#### What to Learn

**Supervised vs Unsupervised Learning**
- **Supervised:** You give the model labeled examples (input → correct output). It learns to predict the output for new inputs. Example: spam classifier trained on emails labeled "spam" or "not spam."
- **Unsupervised:** No labels. The model finds patterns itself. Example: customer segmentation — grouping customers by behavior without telling it what groups to find.

**Train / Test Split**
You never test a model on data it trained on — that's cheating. Split your data: 80% to train, 20% to test.
```python
from sklearn.model_selection import train_test_split

X = [[100], [150], [200], [250], [300]]  # square footage
y = [200000, 280000, 350000, 420000, 500000]  # price

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

**Linear Regression** — predicting a number
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
prediction = model.predict([[175]])  # predict price for 175 sq ft
print(f"Predicted price: ${prediction[0]:,.0f}")
```

**Classification** — predicting a category
```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2%}")
```

**Overfitting**
When a model memorizes training data instead of learning patterns — it performs great on training data but poorly on new data. Signs: training accuracy 99%, test accuracy 60%.

**Tokenization**
LLMs don't read words — they read tokens. A token is roughly 4 characters or ¾ of a word. "Hello world" = 2 tokens. "supercalifragilistic" = 6 tokens.

**Embeddings**
A way to represent text (or anything) as a list of numbers so a computer can measure similarity. Similar meanings → similar numbers → close in space.
```
"dog"  → [0.2, 0.8, 0.1, ...]
"cat"  → [0.3, 0.7, 0.2, ...]  ← close to dog
"car"  → [0.9, 0.1, 0.6, ...]  ← far from dog
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Using `scikit-learn`, train a simple linear regression model to predict house prices from square footage. Print the model's prediction for a 1500 sq ft house. |
| 🟡 Medium | Load the Iris dataset, train a classification model, evaluate it with accuracy score and a confusion matrix, and explain in comments what each metric means. |
| 🔴 Hard | Build a spam classifier — use a real email dataset, TF-IDF vectorization, train/test split, and compare accuracy of at least 2 models (e.g. Naive Bayes vs Logistic Regression). Document which performs better and why. |

---

### Topic 8 — LLM Concepts

#### What to Learn

**Tokens**
The unit LLMs process. Text is broken into tokens before being fed to the model. Pricing is per token.
- 1 token ≈ 4 characters of English text
- "ChatGPT is great!" ≈ 5 tokens
- 1000 words ≈ 750 tokens

**Context Window**
The maximum number of tokens the model can "see" at once — both input and output combined. Claude Sonnet 5 has a 200k token context window (~150,000 words).

**Temperature**
Controls randomness of output.
- `0.0` → always picks the most likely next token → deterministic, consistent
- `1.0` → more random → creative but less predictable
- For data extraction, JSON, code: use low temperature
- For creative writing, brainstorming: use high temperature

**Top-p (nucleus sampling)**
Another way to control randomness. Limits the model to only consider tokens that together make up the top `p` probability mass. `top_p=0.9` means the model only picks from the 90% most likely tokens.

**Embeddings**
Converting text into a vector of numbers that captures its meaning. Used for search, similarity comparison, and RAG.
```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = ["I love dogs", "Cats are great pets", "Python is a programming language"]
embeddings = model.encode(sentences)

# Cosine similarity — 1.0 = identical meaning, 0.0 = unrelated
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

sim = cosine_similarity(embeddings[0], embeddings[1])
print(f"Similarity between dogs and cats: {sim:.3f}")  # high — both about pets
```

**How Transformers work (simplified)**
1. Input text is split into tokens
2. Each token becomes a vector (embedding)
3. The "attention" mechanism lets each token look at all other tokens to understand context
4. After many layers of this, the model predicts the next token
5. This repeats until the response is complete

**Tracking token usage with Claude**
```python
response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Explain gravity in one sentence."}]
)
print(response.content[0].text)
print(f"Input tokens: {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Write a script that sends the same prompt to Claude at `temperature=0.0` and `temperature=1.0` five times each — print all responses and note how they differ. |
| 🟡 Medium | Write a script that generates embeddings for 5 sentences using the `sentence-transformers` library, then computes cosine similarity between all pairs — identify which two sentences are most semantically similar. |
| 🔴 Hard | Build a token budget tracker — wrap the Claude API call so that after every response it prints: tokens used in this message, total tokens used in the session, and estimated cost based on Claude's pricing. Warn the user when they approach a set limit. |

---

### Topic 9 — RAG (Retrieval-Augmented Generation)

#### What to Learn

**What RAG is**
RAG = give the LLM only the relevant parts of your documents as context, instead of sending the entire document.

**Why it matters:** LLMs have a knowledge cutoff and don't know your private documents. RAG lets Claude answer questions about *your* data accurately.

**The RAG pipeline**
```
1. Load document
2. Split into chunks
3. Embed each chunk → vector
4. Store vectors in a vector DB
--- at query time ---
5. Embed the user's question → vector
6. Find the most similar chunks (vector search)
7. Insert those chunks into Claude's prompt
8. Claude answers using only that context
```

**Step 1–2: Chunking**
```python
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap  # overlap keeps context at boundaries
    return chunks

with open("document.txt") as f:
    text = f.read()

chunks = chunk_text(text)
print(f"Created {len(chunks)} chunks")
```

**Step 3–4: Embed and store**
```python
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.create_collection("my_docs")

embeddings = model.encode(chunks).tolist()
collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)
```

**Step 5–8: Query and answer**
```python
query = "What does the document say about pricing?"
query_embedding = model.encode([query]).tolist()

results = collection.query(query_embeddings=query_embedding, n_results=3)
context = "\n\n".join(results["documents"][0])

response = claude_client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": f"Answer this question using only the context below.\n\nContext:\n{context}\n\nQuestion: {query}"
    }]
)
print(response.content[0].text)
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Split a long text document into chunks of 500 characters, print the number of chunks, and display the first and last chunk. |
| 🟡 Medium | Build a basic RAG pipeline — embed 10 text chunks using `sentence-transformers`, store them in memory, embed a query, find the 3 most similar chunks using cosine similarity, and print them. |
| 🔴 Hard | Build a PDF Q&A tool — load a PDF with `pypdf`, chunk it, store embeddings in ChromaDB, and let the user ask questions. Retrieve the top 3 relevant chunks, inject them into Claude's context, and return a grounded answer that cites which chunk it came from. |

---

### Topic 10 — Vector Databases

#### What to Learn

**What a Vector Database is**
A database built specifically for storing and searching embeddings (vectors of numbers). Unlike SQL which searches by exact match, a vector DB searches by semantic similarity — "find me things with similar meaning."

**Why you need one**
A regular list of embeddings works for 100 items. For 100,000 documents, you need a vector DB — it uses efficient indexing (like HNSW) to search millions of vectors in milliseconds.

**ChromaDB — local, no setup required**
```python
import chromadb
from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()  # in-memory
# client = chromadb.PersistentClient(path="./chroma_db")  # save to disk

collection = client.create_collection("movies")

# Add documents
docs = [
    "A space crew fights alien invaders on Mars",
    "A detective solves a murder mystery in London",
    "Two robots fall in love in a post-apocalyptic world"
]
embeddings = embed_model.encode(docs).tolist()

collection.add(
    documents=docs,
    embeddings=embeddings,
    metadatas=[{"genre": "sci-fi"}, {"genre": "thriller"}, {"genre": "sci-fi"}],
    ids=["doc1", "doc2", "doc3"]
)

# Query
query = "space adventure with robots"
q_embed = embed_model.encode([query]).tolist()
results = collection.query(query_embeddings=q_embed, n_results=2)

for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
    print(f"[{meta['genre']}] {doc}")
```

**Key concepts**
| Term | Meaning |
|---|---|
| Collection | Like a table in SQL — a group of related documents |
| Embedding | The vector representation of a document |
| Metadata | Extra fields you attach (title, date, source) — filterable |
| n_results | How many similar results to return |
| Distance | How different two vectors are — lower = more similar |

**Filtering with metadata**
```python
# Only search within sci-fi movies
results = collection.query(
    query_embeddings=q_embed,
    n_results=2,
    where={"genre": "sci-fi"}
)
```

**Pinecone — cloud-hosted (for production)**
Same concept as ChromaDB but lives on their servers. Use when you need to share the DB across multiple machines or have millions of vectors.

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Install ChromaDB, create a collection, add 5 documents with metadata, then query it with a string and print the top 2 results. |
| 🟡 Medium | Build a movie recommendation engine — embed 20 movie descriptions, store in ChromaDB with metadata (title, genre, year), then given a query like "space adventure with robots" return the top 3 matching movies. |
| 🔴 Hard | Build a semantic search engine for your notes — index all `.txt` files from a folder into ChromaDB (each paragraph as a chunk), build a CLI where the user types a query and gets back the top 5 most relevant paragraphs with file name and preview. |

---

### Topic 11 — OpenAI & Gemini APIs

#### What to Learn

**OpenAI API setup**
```bash
pip install openai
export OPENAI_API_KEY="sk-..."
```
```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Explain recursion in one sentence."}]
)
print(response.choices[0].message.content)
print(f"Tokens used: {response.usage.total_tokens}")
```

**Gemini API setup**
```bash
pip install google-generativeai
export GEMINI_API_KEY="AIza..."
```
```python
import google.generativeai as genai
genai.configure(api_key="YOUR_KEY")

model = genai.GenerativeModel("gemini-1.5-pro")
response = model.generate_content("Explain recursion in one sentence.")
print(response.text)
```

**Vision (sending images)**
```python
import base64

with open("photo.jpg", "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

# OpenAI vision
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What is in this image?"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}
        ]
    }]
)
print(response.choices[0].message.content)
```

**Comparing providers**
| Provider | Best for | Pricing (approx) |
|---|---|---|
| Claude (Anthropic) | Long documents, reasoning, safety | ~$3 / 1M input tokens |
| GPT-4o (OpenAI) | General purpose, vision, function calling | ~$5 / 1M input tokens |
| Gemini 1.5 Pro | Very long context (1M tokens), multimodal | ~$3.50 / 1M input tokens |

**Building a provider-agnostic wrapper**
```python
def ask(prompt, provider="claude"):
    if provider == "claude":
        r = claude_client.messages.create(model="claude-sonnet-5", max_tokens=1024,
            messages=[{"role": "user", "content": prompt}])
        return r.content[0].text

    elif provider == "openai":
        r = openai_client.chat.completions.create(model="gpt-4o",
            messages=[{"role": "user", "content": prompt}])
        return r.choices[0].message.content

    elif provider == "gemini":
        r = gemini_model.generate_content(prompt)
        return r.text
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Call both the OpenAI and Gemini APIs with the same prompt: "Explain recursion in one paragraph." Print both responses side by side. |
| 🟡 Medium | Build a script that sends an image to the vision endpoint (OpenAI or Gemini) and asks "What is in this image?" — test it with 3 different images and print the descriptions. |
| 🔴 Hard | Build a provider-agnostic LLM wrapper — a single `ask(prompt, provider="claude")` function that routes to Claude, OpenAI, or Gemini, normalizes the response format, and tracks cost per provider. Run the same 5 prompts through all three and compare quality and cost. |

---

### Topic 12 — AI Projects (LLM Layer)

#### What to Learn

**Putting it all together: PDF Q&A pipeline**
```python
import anthropic
import chromadb
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

def load_pdf(path):
    reader = PdfReader(path)
    return " ".join(page.extract_text() for page in reader.pages)

def chunk(text, size=500):
    return [text[i:i+size] for i in range(0, len(text), size)]

def build_index(chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    client = chromadb.Client()
    col = client.create_collection("pdf")
    col.add(documents=chunks, embeddings=model.encode(chunks).tolist(),
            ids=[f"c{i}" for i in range(len(chunks))])
    return col, model

def answer(col, model, question):
    q_emb = model.encode([question]).tolist()
    results = col.query(query_embeddings=q_emb, n_results=3)
    context = "\n\n".join(results["documents"][0])

    claude = anthropic.Anthropic()
    r = claude.messages.create(model="claude-sonnet-5", max_tokens=1024,
        messages=[{"role": "user", "content":
            f"Answer using only this context:\n\n{context}\n\nQuestion: {question}"}])
    return r.content[0].text

text = load_pdf("document.pdf")
chunks = chunk(text)
col, model = build_index(chunks)

while True:
    q = input("Question: ")
    if q == "quit": break
    print(answer(col, model, q))
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Build an AI chatbot that answers questions about a single document (any PDF or text file you choose). Uses basic RAG. |
| 🟡 Medium | Build a PDF Q&A tool with a CLI — load any PDF, ask multiple questions in a loop, and have Claude answer using only content from the document (not its training data). |
| 🔴 Hard | Build an AI research assistant — given a topic, it searches 3 text files you provide, retrieves the most relevant sections, and produces a structured report with an introduction, key findings, and a conclusion — all grounded in the provided documents. |

---

## PHASE 3 — Weeks 7–9: Build AI Agents
**Goal: Build Autonomous AI Agents**

---

### Topic 13 — LangChain / LlamaIndex

#### What to Learn

**What LangChain is**
A framework for building LLM applications. It provides pre-built components for document loading, text splitting, embedding, vector stores, chains, and agents — so you don't build everything from scratch.

**LangChain — Document loading and splitting**
```python
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = TextLoader("document.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)
print(f"{len(chunks)} chunks created")
```

**LangChain — RAG chain**
```python
from langchain_anthropic import ChatAnthropic
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

embed = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(chunks, embed)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

llm = ChatAnthropic(model="claude-sonnet-5")
chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

answer = chain.invoke({"query": "What is this document about?"})
print(answer["result"])
```

**LangChain — Memory (conversation history)**
```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

conversation.predict(input="My name is Alice.")
response = conversation.predict(input="What is my name?")
print(response)  # Claude remembers: "Your name is Alice."
```

**LlamaIndex — multi-document routing**
```python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.tools import QueryEngineTool
from llama_index.core.query_engine import RouterQueryEngine

# Index each document separately
docs_a = SimpleDirectoryReader("folder_a").load_data()
docs_b = SimpleDirectoryReader("folder_b").load_data()

index_a = VectorStoreIndex.from_documents(docs_a)
index_b = VectorStoreIndex.from_documents(docs_b)

# Create a router that picks the right index
tools = [
    QueryEngineTool.from_defaults(index_a.as_query_engine(), description="About sales data"),
    QueryEngineTool.from_defaults(index_b.as_query_engine(), description="About HR policies"),
]
router = RouterQueryEngine.from_defaults(query_engine_tools=tools)
response = router.query("What is our vacation policy?")
print(response)
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Use LangChain to load a text file, split it into chunks, and run a simple question-answering chain that answers "What is this document about?" |
| 🟡 Medium | Build a LangChain RAG pipeline — load a PDF, embed it, store in a vector store, and create a retrieval chain that answers questions with cited sources. |
| 🔴 Hard | Build a multi-document research agent using LlamaIndex — index 5 different documents, build a router that picks the right document based on the query, and return a synthesized answer that draws from multiple sources when relevant. |

---

### Topic 14 — OpenAI Agents SDK

#### What to Learn

**What the OpenAI Agents SDK is**
A framework for building agents that can use tools, hand off tasks to other agents, and run autonomously. Think of it as a managed version of the agent loop.

**Basic agent with a tool**
```python
from agents import Agent, Runner, function_tool
import datetime

@function_tool
def get_current_time() -> str:
    """Returns the current time."""
    return datetime.datetime.now().strftime("%H:%M:%S")

agent = Agent(
    name="TimeBot",
    instructions="You are a helpful assistant. Use tools when needed.",
    tools=[get_current_time]
)

result = Runner.run_sync(agent, "What time is it?")
print(result.final_output)
```

**Handoffs between agents**
```python
coding_agent = Agent(
    name="Coding Assistant",
    instructions="You help with Python code questions only."
)

writing_agent = Agent(
    name="Writing Assistant",
    instructions="You help with writing, grammar, and essays only."
)

triage_agent = Agent(
    name="Triage",
    instructions="Route the user to the right specialist.",
    handoffs=[coding_agent, writing_agent]
)

result = Runner.run_sync(triage_agent, "Can you help me write a for loop?")
print(result.final_output)  # Handled by coding_agent
```

**Built-in tools**
```python
from agents import WebSearchTool

agent = Agent(
    name="Researcher",
    instructions="Research topics and give concise summaries.",
    tools=[WebSearchTool()]
)
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Create a basic OpenAI agent with one custom tool (`get_current_time`) — ask it "What time is it?" and verify it calls the tool and uses the result in its response. |
| 🟡 Medium | Build a two-agent system with handoffs — a triage agent that reads the user's message and hands off to either a "coding assistant" agent or a "writing assistant" agent depending on the topic. |
| 🔴 Hard | Build a research agent using the OpenAI Agents SDK with tools for web search, note saving, and note reading — give it the task "Research the top 3 uses of AI in healthcare and write a 300-word summary" — let it work autonomously and print the final output. |

---

### Topic 15 — CrewAI / PydanticAI

#### What to Learn

**What CrewAI is**
A framework for multi-agent workflows where each agent has a role, a goal, and a set of tools. Agents pass their output to the next one — like an assembly line.

**CrewAI basics**
```python
from crewai import Agent, Task, Crew, Process

researcher = Agent(
    role="Researcher",
    goal="Find key facts about the given topic",
    backstory="You are an expert researcher with access to the internet.",
    verbose=True
)

writer = Agent(
    role="Writer",
    goal="Write a clear blog post based on research findings",
    backstory="You are a skilled technical writer.",
    verbose=True
)

research_task = Task(
    description="Research the latest trends in AI agents for 2025.",
    expected_output="A bullet-point list of 5 key trends with 1-sentence explanations.",
    agent=researcher
)

writing_task = Task(
    description="Write a 300-word blog post based on the research.",
    expected_output="A complete blog post with a title, intro, body, and conclusion.",
    agent=writer
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential  # researcher → writer
)

result = crew.kickoff()
print(result)
```

**PydanticAI — structured, typed agents**
```python
from pydantic_ai import Agent
from pydantic import BaseModel

class BlogPost(BaseModel):
    title: str
    summary: str
    word_count: int

agent = Agent(
    "claude-sonnet-5",
    result_type=BlogPost,
    system_prompt="You are a content creator. Return structured blog post data."
)

result = agent.run_sync("Write a blog post about Python decorators.")
post = result.data  # typed BlogPost object
print(post.title)
print(post.summary)
print(post.word_count)
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Create a CrewAI crew with one agent (role: "Summarizer") and one task — summarize a paragraph of text you hardcode. Print the result. |
| 🟡 Medium | Build a 2-agent crew: a "Researcher" that finds key facts about a topic and a "Writer" that turns those facts into a short blog post. Chain them so the writer receives the researcher's output. |
| 🔴 Hard | Build a 3-agent content pipeline using PydanticAI — "Topic Analyst" identifies the audience and tone, "Content Writer" drafts the article, "Editor" reviews and improves it. Use Pydantic models for structured outputs at each stage. |

---

### Topic 16 — MCP (Model Context Protocol)

#### What to Learn

**What MCP is**
MCP is an open standard that lets AI models (like Claude) connect to external tools and data sources through a common interface — like a USB standard for AI tools. Instead of writing tool code inside your Python script, you expose it as an MCP server and any MCP-compatible client (Claude Desktop, etc.) can use it.

**MCP server structure**
```python
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types
import datetime

server = Server("my-tools")

@server.list_tools()
async def list_tools():
    return [
        types.Tool(
            name="get_time",
            description="Returns the current time",
            inputSchema={"type": "object", "properties": {}, "required": []}
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "get_time":
        return [types.TextContent(type="text", text=datetime.datetime.now().strftime("%H:%M:%S"))]

async def main():
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())

import asyncio
asyncio.run(main())
```

**Connecting to Claude Desktop**
Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "my-tools": {
      "command": "python3",
      "args": ["/path/to/your/mcp_server.py"]
    }
  }
}
```
Restart Claude Desktop — Claude can now call your tools in any conversation.

**MCP vs function calling**
| | Function Calling | MCP |
|---|---|---|
| Where tools live | Inside your Python script | Separate server process |
| Who can use them | Only your script | Any MCP client (Claude Desktop, etc.) |
| Setup | Simpler | More setup, more reusable |
| Best for | One-off agents | Tools you want to reuse everywhere |

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Set up a local MCP server with one tool — `get_time` — connect it to Claude Desktop and verify Claude can call it from a conversation. |
| 🟡 Medium | Build an MCP server that exposes 3 tools: `read_file`, `write_file`, and `list_files` — connect to Claude Desktop and ask it to "read my notes and create a summary file." |
| 🔴 Hard | Build a custom MCP server that wraps a SQLite database — tools: `run_query`, `list_tables`, `describe_table` — connect it to Claude and ask natural-language questions about your database, letting Claude write and execute the SQL. |

---

### Topic 17 — Function Calling

#### What to Learn

**What function calling is**
You define tools (functions) and pass them to the LLM. The LLM decides when to call them, what arguments to use, and then uses the result to form its final answer. The actual function runs in your code — the LLM just asks for it.

**Step 1 — Define the tool schema**
```python
tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city name, e.g. 'London'"
                }
            },
            "required": ["city"]
        }
    }
]
```

**Step 2 — Send to Claude with tools**
```python
import anthropic
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}]
)
print(response.stop_reason)  # "tool_use" — Claude wants to call a tool
```

**Step 3 — Detect and execute the tool call**
```python
import requests

def get_weather(city):
    r = requests.get(f"https://wttr.in/{city}?format=j1")
    data = r.json()
    return f"{data['current_condition'][0]['temp_C']}°C, {data['current_condition'][0]['weatherDesc'][0]['value']}"

for block in response.content:
    if block.type == "tool_use":
        tool_name = block.name
        tool_input = block.input
        if tool_name == "get_weather":
            result = get_weather(tool_input["city"])
```

**Step 4 — Send the result back (the full agent loop)**
```python
messages = [{"role": "user", "content": "What's the weather in Tokyo?"}]

while True:
    response = client.messages.create(model="claude-sonnet-5", max_tokens=1024,
        tools=tools, messages=messages)

    if response.stop_reason == "end_turn":
        print(response.content[0].text)
        break

    # Claude wants to use a tool
    messages.append({"role": "assistant", "content": response.content})

    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            result = get_weather(block.input["city"])  # run your function
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": result
            })

    messages.append({"role": "user", "content": tool_results})
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Define a `get_weather(city)` tool and a `get_time()` tool — ask Claude "What's the weather in Paris and what time is it there?" — verify both tools get called. |
| 🟡 Medium | Build a calculator agent — tools for `add`, `subtract`, `multiply`, `divide` — ask a multi-step word problem and watch Claude chain the tools to reach the answer. |
| 🔴 Hard | Build a file management agent — tools: `list_files`, `read_file`, `write_file`, `delete_file`, `search_file(keyword)` — implement the full agent loop and ask it tasks like "Find all files mentioning 'budget', summarize them, and save the summary to budget-summary.txt." |

---

### Topic 18 — Workflow Automation (n8n)

#### What to Learn

**What n8n is**
n8n is a visual workflow automation tool — like Zapier but open-source and self-hosted. You build workflows by connecting nodes: triggers, logic, AI, and external services (Gmail, Slack, databases).

**Core concepts**
| Term | Meaning |
|---|---|
| Trigger node | Starts the workflow (webhook, schedule, manual) |
| Action node | Does something (send email, call API, run code) |
| AI Agent node | Sends data to an LLM and gets a response |
| Webhook | A URL that triggers the workflow when called |

**Installing n8n locally**
```bash
npm install -g n8n
n8n start
# Open http://localhost:5678
```

**Basic workflow pattern**
```
Webhook Trigger → HTTP Request (fetch data) → AI Agent (Claude) → Gmail (send result)
```

**Calling your n8n webhook from Python**
```python
import requests

webhook_url = "http://localhost:5678/webhook/my-trigger"
payload = {"question": "What are the latest trends in AI?"}
response = requests.post(webhook_url, json=payload)
print(response.json())
```

**AI Agent node setup in n8n**
- Add an "AI Agent" node
- Select Claude as the provider (add your API key in credentials)
- Set the system prompt
- Connect input data using `{{ $json.question }}`
- Connect output to the next node

**Connecting to Slack**
- Add a "Slack" node after the AI Agent node
- Set channel and message: `{{ $json.output }}`
- Every time the webhook is hit, the answer appears in Slack

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Set up n8n locally, create a workflow with a manual trigger → HTTP request to a free API → print the result. Run it and verify it works. |
| 🟡 Medium | Build a workflow: Webhook trigger → AI Agent node (Claude) → Gmail send. Test it by hitting the webhook with a topic and verifying Claude's response arrives as an email. |
| 🔴 Hard | Build a research workflow: Webhook receives a question → n8n fetches 3 web pages → sends content to Claude with instructions to synthesize an answer → posts the answer to a Slack channel. |

---

### Topic 19 — Agent Projects

#### What to Learn

**Combining tools into a real agent — full pattern**
```python
import anthropic
import os
import json

client = anthropic.Anthropic()

# Define your tools
tools = [
    {"name": "read_file", "description": "Read a text file",
     "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}},
    {"name": "list_files", "description": "List files in a directory",
     "input_schema": {"type": "object", "properties": {"directory": {"type": "string"}}, "required": ["directory"]}},
    {"name": "save_report", "description": "Save a report to disk",
     "input_schema": {"type": "object",
                      "properties": {"filename": {"type": "string"}, "content": {"type": "string"}},
                      "required": ["filename", "content"]}}
]

# Implement the tools
def run_tool(name, args):
    if name == "read_file":
        with open(args["path"]) as f:
            return f.read()
    elif name == "list_files":
        return str(os.listdir(args["directory"]))
    elif name == "save_report":
        with open(args["filename"], "w") as f:
            f.write(args["content"])
        return f"Saved {args['filename']}"

# Agent loop
def run_agent(task):
    messages = [{"role": "user", "content": task}]
    while True:
        response = client.messages.create(
            model="claude-sonnet-5", max_tokens=4096, tools=tools, messages=messages)
        if response.stop_reason == "end_turn":
            return response.content[0].text
        messages.append({"role": "assistant", "content": response.content})
        results = []
        for block in response.content:
            if block.type == "tool_use":
                output = run_tool(block.name, block.input)
                results.append({"type": "tool_result", "tool_use_id": block.id, "content": output})
        messages.append({"role": "user", "content": results})

print(run_agent("List the files in my project folder, read any .txt files, and save a summary to summary.txt"))
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Build an email drafting agent — user describes who they're writing to and why, the agent drafts a professional email and asks for approval before "sending" (just printing). |
| 🟡 Medium | Build a research agent — user gives a topic, agent searches 3 sources (mock with files), synthesizes a report, and saves it as a markdown file. |
| 🔴 Hard | Build a customer support agent — has tools to look up orders (SQLite), check FAQs (vector search), and escalate to human (write to a log file) — handles 5 different simulated customer queries and routes each correctly. |

---

## PHASE 4 — Weeks 10–12: Deploy & Get Job Ready
**Goal: Deploy Real AI Applications**

---

### Topic 20 — FastAPI

#### What to Learn

**What FastAPI is**
A modern Python web framework for building APIs. It's fast, auto-generates documentation at `/docs`, and uses type hints to validate requests and responses automatically.

**Basic FastAPI app**
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}
```
```bash
pip install fastapi uvicorn
uvicorn main:app --reload   # starts server at localhost:8000
# Auto docs: localhost:8000/docs
```

**POST endpoint with Pydantic model**
```python
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

class ChatResponse(BaseModel):
    reply: str
    tokens_used: int

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # call Claude here
    reply = ask_claude(request.message)
    return ChatResponse(reply=reply, tokens_used=100)
```

**Query parameters**
```python
@app.get("/search")
def search(query: str, limit: int = 10):
    # GET /search?query=hello&limit=5
    return {"query": query, "limit": limit}
```

**Error handling**
```python
from fastapi import HTTPException

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id not in database:
        raise HTTPException(status_code=404, detail="User not found")
    return database[user_id]
```

**Async endpoints**
```python
import anthropic

client = anthropic.Anthropic()

@app.post("/summarize")
async def summarize(request: ChatRequest):
    response = client.messages.create(
        model="claude-sonnet-5", max_tokens=512,
        messages=[{"role": "user", "content": f"Summarize: {request.message}"}]
    )
    return {"summary": response.content[0].text}
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Build a FastAPI app with one GET endpoint `/health` that returns `{"status": "ok"}` and one POST endpoint `/echo` that returns whatever JSON body you send it. |
| 🟡 Medium | Build a FastAPI wrapper around Claude — POST `/chat` accepts `{"message": "..."}` and returns Claude's response. Add a GET `/history` endpoint that returns the last 10 messages from an in-memory list. |
| 🔴 Hard | Build a full FastAPI AI service with: `/chat` (multi-turn with session IDs), `/summarize` (accepts text, returns summary), `/analyze` (sentiment + keywords) — all backed by Claude. Add Pydantic models for every request and response, and proper HTTP error handling. |

---

### Topic 21 — Docker

#### What to Learn

**What Docker is**
Docker packages your app and all its dependencies into a container — a standardized unit that runs the same way on any machine. No more "it works on my machine."

**Key concepts**
| Term | Meaning |
|---|---|
| Image | A blueprint (like a recipe) — read-only |
| Container | A running instance of an image — like a live kitchen using that recipe |
| Dockerfile | A text file with instructions to build an image |
| docker-compose | A tool to run multiple containers together |

**Basic Dockerfile for FastAPI**
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Build and run**
```bash
docker build -t my-ai-app .
docker run -p 8000:8000 -e ANTHROPIC_API_KEY=sk-... my-ai-app
# App is live at localhost:8000
```

**docker-compose.yml — multiple services**
```yaml
version: "3.9"

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

```bash
docker-compose up      # start everything
docker-compose down    # stop everything
docker-compose logs    # see output from all containers
```

**.dockerignore** — don't copy these into the image
```
.env
__pycache__
*.pyc
.git
venv/
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Write a `Dockerfile` for your FastAPI app, build the image, run it as a container, and confirm the `/health` endpoint responds at `localhost:8000`. |
| 🟡 Medium | Use `docker-compose` to run your FastAPI app + a PostgreSQL database together. The API should connect to the DB on startup. Include a `.env` file for secrets. |
| 🔴 Hard | Build a multi-container setup with docker-compose: FastAPI app, PostgreSQL, and an n8n instance. All three communicate over a Docker network. Write a `Makefile` with commands `make up`, `make down`, `make logs`. |

---

### Topic 22 — Cloud Deployment

#### What to Learn

**Deployment options**
| Platform | Best for | Free tier |
|---|---|---|
| Railway | Fastest deploy, great for side projects | Yes |
| Render | Easy Docker deploys, free PostgreSQL | Yes |
| AWS EC2 | Full control, production-grade | 12 months free |
| AWS ECS | Docker at scale | Pay per use |

**Deploy to Railway (simplest)**
```bash
# Install Railway CLI
npm install -g @railway/cli

railway login
railway init        # in your project folder
railway up          # deploy
railway domain      # get your public URL
```
Set env vars in Railway dashboard → Variables tab.

**Deploy to Render**
1. Push your code to GitHub
2. Go to render.com → New → Web Service
3. Connect your GitHub repo
4. Set Build Command: `pip install -r requirements.txt`
5. Set Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add environment variables (ANTHROPIC_API_KEY, etc.)
7. Deploy — live URL in ~2 minutes

**GitHub Actions CI/CD — auto deploy on push**
```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Render
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

**Environment variables in production**
Never hardcode secrets. Use environment variables — set them in the platform dashboard, never in code.
```python
import os
api_key = os.environ["ANTHROPIC_API_KEY"]  # reads from environment
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Deploy your FastAPI app to Railway or Render — set the `ANTHROPIC_API_KEY` as an environment variable — confirm the live URL works by hitting `/health`. |
| 🟡 Medium | Set up a GitHub Actions workflow that automatically deploys your app to Render on every push to `main`. The workflow should run `pytest` first and only deploy if tests pass. |
| 🔴 Hard | Deploy a Dockerized FastAPI + PostgreSQL app to AWS (EC2 or ECS) — configure a proper security group, store secrets in AWS Secrets Manager, set up a health check, and document the full deployment steps in a `DEPLOYMENT.md`. |

---

### Topic 23 — Authentication

#### What to Learn

**API Key Auth — simplest approach**
```python
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()
VALID_API_KEY = "my-secret-key-123"

@app.get("/protected")
def protected_route(x_api_key: str = Header(None)):
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return {"message": "Access granted"}
```
```bash
# Test with curl
curl -H "X-API-Key: my-secret-key-123" http://localhost:8000/protected
```

**JWT Authentication — stateless tokens**
JWT (JSON Web Token) = a signed token that contains user info. The server doesn't store sessions — it just verifies the signature.

```
Header.Payload.Signature
eyJhbGci...  eyJ1c2VySW...  abc123...
```

```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI()

fake_users = {"alice": {"password": pwd_context.hash("password123")}}

def create_token(username: str):
    expire = datetime.utcnow() + timedelta(hours=24)
    return jwt.encode({"sub": username, "exp": expire}, SECRET_KEY, ALGORITHM)

@app.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = fake_users.get(form.username)
    if not user or not pwd_context.verify(form.password, user["password"]):
        raise HTTPException(status_code=401, detail="Wrong credentials")
    return {"access_token": create_token(form.username), "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, [ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/me")
def get_me(user: str = Depends(get_current_user)):
    return {"username": user}
```

**Password hashing — never store plain text**
```python
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"])

hashed = pwd_context.hash("mypassword123")  # store this in DB
valid = pwd_context.verify("mypassword123", hashed)  # True
wrong = pwd_context.verify("wrongpassword", hashed)  # False
```

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Add API key authentication to your FastAPI app — requests without the correct key in the `X-API-Key` header get a 401 response. Test with both valid and invalid keys. |
| 🟡 Medium | Implement JWT authentication — POST `/login` with username/password returns a token, protected routes require `Authorization: Bearer <token>` header. Use `python-jose` for JWT and `passlib` for password hashing. |
| 🔴 Hard | Build a full auth system — user registration, login (returns JWT), refresh tokens, logout (token blacklist in Redis or SQLite), and role-based access control (admin vs regular user). Admin-only endpoints return 403 for regular users. |

---

### Topic 24 — Portfolio Projects

#### What to Learn

**What makes a portfolio project stand out**
- Solves a real, specific problem
- Has a live demo URL (not just a GitHub link)
- Clean README with a screenshot
- Uses at least 2–3 skills from the roadmap
- Less than 5 minutes from clone to running locally

**Anatomy of a great README**
```markdown
# PDF Q&A Bot

Ask questions about any PDF using Claude AI.

## Demo
[Live demo](https://your-app.railway.app) | [Screenshot](./screenshot.png)

## Features
- Upload any PDF
- Ask natural language questions
- Answers grounded in document content only

## Tech Stack
Python · FastAPI · ChromaDB · Claude API · Docker

## Setup
git clone https://github.com/you/pdf-qa
cd pdf-qa
cp .env.example .env   # add your ANTHROPIC_API_KEY
docker-compose up

## How it works
1. PDF is chunked into 500-char segments
2. Each chunk is embedded and stored in ChromaDB
3. On query, top 3 matching chunks are retrieved
4. Claude answers using only those chunks as context
```

**3 strong portfolio project ideas**
1. **PDF Q&A Bot** — upload a PDF, ask questions → demonstrates RAG, FastAPI, Docker
2. **AI Research Agent** — give a topic, get a structured report → demonstrates agents, tool use, LangChain
3. **Customer Support Bot** — FAQ answers via vector search + escalation → demonstrates SQLite, RAG, authentication

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Take your best Week 1–3 project, add a proper `README.md` (what it does, how to install, how to run, example output), and make sure it runs cleanly on a fresh machine. |
| 🟡 Medium | Build and deploy a public-facing AI tool — e.g. a PDF summarizer or chatbot — with FastAPI + Docker + cloud hosting. It should be accessible via a real URL that you can share with anyone. |
| 🔴 Hard | Build a full-stack AI project: FastAPI backend + simple HTML/JS frontend + authentication + database + Docker + cloud deployment. Should demonstrate at least 3 skills from the roadmap. Write a clean README with architecture diagram, tech stack, and setup instructions. |

---

### Topic 25 — GitHub, Resume & LinkedIn

#### What to Learn

**GitHub profile best practices**
- Profile README: add one at `github.com/yourname/yourname` — briefly introduce yourself and your tech stack
- Pin 3–6 projects at the top of your profile (the ones with the best READMEs)
- Every pinned repo must have: a description, a README, and ideally a live link

**How to write each resume section**

*Skills section*
```
Languages: Python
Frameworks: FastAPI, LangChain, CrewAI
AI/ML: Claude API, OpenAI API, RAG, Vector Databases (ChromaDB)
Infrastructure: Docker, AWS, GitHub Actions
Databases: PostgreSQL, SQLite
```

*Projects section (one entry)*
```
PDF Q&A Bot                                          github.com/you/pdf-qa | live.app
AI-powered document question-answering system using RAG and Claude API.
• Built RAG pipeline chunking PDFs into ChromaDB vector store for semantic retrieval
• FastAPI backend with JWT auth deployed via Docker to Railway
• Reduced answer hallucination by grounding responses in source document context only
Tech: Python, FastAPI, ChromaDB, Claude API, Docker, Railway
```

*The formula for a good bullet point*
```
[Action verb] + [what you built] + [specific result or metric]

"Built RAG pipeline reducing irrelevant answers by 80% on benchmark dataset"  ✅
"Worked on AI stuff"  ❌
```

**LinkedIn**
- Headline: `Python Developer | Building AI Agents with LLMs`
- About: 3–4 sentences — what you build, what problems you solve, what you're looking for
- Featured: pin your 3 live projects with screenshots
- Experience: even self-projects count — list them as "Independent Projects"

---

#### Exercises

| Level | Problem |
|---|---|
| 🟢 Easy | Pin your 3 best projects on GitHub. Each repo must have: a title, a 1-sentence description, a README with setup instructions, and at least one screenshot or code example. |
| 🟡 Medium | Write your resume — include a Skills section (Python, FastAPI, Docker, LangChain, Claude API, SQL), a Projects section with 3 projects (name, 1-sentence description, tech stack, link), and an Experience section. Keep it to 1 page. |
| 🔴 Hard | Update your LinkedIn: headline should say "AI Engineer" or "Python Developer building AI agents", About section should explain what you build and what problems you solve, add all 3 projects under Featured. Write 3 posts about what you learned during this 12-week journey and publish them. |

---

## Final Goal

By the end of 12 weeks you will have:

- [ ] 3–5 production-ready AI projects deployed to the cloud
- [ ] A strong GitHub portfolio with clean READMEs
- [ ] A resume tailored for AI engineering roles
- [ ] Experience with: Python · Git · SQL · REST APIs · LLMs · RAG · Agents · FastAPI · Docker · Cloud

---

> Build > Read. Every topic should produce working code.
> Hard problems are optional but doing them separates you from 90% of candidates.
