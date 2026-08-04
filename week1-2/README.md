# Week 1 & 2 — Python Foundations + First AI Agent

> **Goal**: Go from zero Python to building a working AI agent that calls tools autonomously.

---

## Week 1 — Python + Terminal Foundations

| Day | Topic | You'll Build |
|-----|-------|--------------|
| 1 | Setup & First Script | A greeting script that takes input |
| 2 | Variables, Strings, Numbers | Tip calculator, unit converter |
| 3 | Lists, Loops, Conditions | Number guessing game, grocery list app |
| 4 | Dictionaries & Functions | Contact book with search/add/delete |
| 5 | Files & JSON | Persistent contact book (saves to disk) |
| 6 | pip & API Calls | Weather fetcher using a real API |
| 7 | Git + Review | Push to GitHub, rewrite from memory |

---

## Week 2 — First Steps with AI (Claude API)

| Day | Topic | You'll Build |
|-----|-------|--------------|
| 8 | Claude API Access | Your first AI script — ask Claude a question |
| 9 | System Prompts & JSON | Text summarizer with structured output |
| 10 | Multi-turn Conversations | Terminal chatbot with memory and save/load |
| 11 | Tool Use (Function Calling) | Give Claude tools it can call |
| 12 | Agent Loop | The core pattern — Claude chains tools autonomously |
| 13 | Build Something Real | Solve YOUR problem with an agent |
| 14 | Review & Ship | Push to GitHub, explain the agent loop |

---

## How to Use This Plan

1. **One day at a time** — don't skip ahead until every checkbox is done
2. **Build > Read** — always code before reading docs
3. **Copy into Apple Notes** — checkboxes become tappable circles on macOS/iOS

---

## Daily Checklist

### Day 1 — Setup & First Script
- [ ] Install Python 3.12+ from python.org
- [ ] Open Terminal, type `python3 --version` — confirm it works
- [ ] Install VS Code (code editor)
- [ ] Create a folder: `mkdir ~/ai-learning && cd ~/ai-learning`
- [ ] Create `hello.py` with: `print("Hello, AI world")`
- [ ] Run it: `python3 hello.py`
- [ ] Modify it to ask your name and greet you (`input()` function)
- [ ] Done when: you can create and run a Python script from Terminal

### Day 2 — Variables, Strings, Numbers
- [ ] Learn: variables, f-strings, type(), int/float/str
- [ ] Build: a tip calculator (input bill + tip %, output total)
- [ ] Build: a unit converter (km to miles, celsius to fahrenheit)
- [ ] Practice: use f-strings to format output nicely
- [ ] Resource: [Python Tutorial — Introduction](https://docs.python.org/3/tutorial/introduction.html)
- [ ] Done when: you can take input, do math, print formatted output

### Day 3 — Lists, Loops, Conditions
- [ ] Learn: lists, for loops, while loops, if/elif/else
- [ ] Build: a number guessing game (random number, user guesses, hints)
- [ ] Build: a grocery list app (add items, show list, count items)
- [ ] Practice: use `range()`, `len()`, `enumerate()`
- [ ] Resource: [Python Tutorial — Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [ ] Done when: you can loop through data and make decisions in code

### Day 4 — Dictionaries & Functions
- [ ] Learn: dictionaries (key-value pairs), functions with `def`
- [ ] Build: a contact book (name → phone number, add/search/delete)
- [ ] Build: rewrite Day 2's calculator as reusable functions
- [ ] Learn: return values vs print (know the difference)
- [ ] Resource: [Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [ ] Done when: you can write functions that take input and return output

### Day 5 — Files & JSON
- [ ] Learn: open(), read(), write() for text files
- [ ] Learn: `import json`, json.loads(), json.dumps()
- [ ] Build: save your contact book to a JSON file
- [ ] Build: load contacts from file on startup
- [ ] Practice: pretty-print a JSON object with `json.dumps(data, indent=2)`
- [ ] Done when: your program remembers data between runs using a file

### Day 6 — pip & Your First API Call
- [ ] Learn: `pip install` — what it does, where packages come from
- [ ] Run: `pip install requests`
- [ ] Build: call a free API (e.g., `https://api.agify.io?name=yourname`)
- [ ] Print the JSON response nicely
- [ ] Learn: what are HTTP methods (GET, POST), status codes (200, 404, 500)
- [ ] Build: a script that takes a city name and returns its weather (use wttr.in)
- [ ] Done when: you can call any public API and use its response in Python

### Day 7 — Git Basics + Review
- [ ] Install Git: `git --version` (usually pre-installed on macOS)
- [ ] Run: `cd ~/ai-learning && git init`
- [ ] Run: `git add . && git commit -m "week 1 projects"`
- [ ] Create a GitHub account (if you don't have one)
- [ ] Create a repo, push your code
- [ ] Review: rewrite any Day 1–6 script from scratch without looking
- [ ] Done when: your week 1 code is on GitHub and you can rewrite at least 2 projects from memory

### Day 8 — Get Claude API Access
- [ ] Go to [Anthropic Console](https://console.anthropic.com) — create an account
- [ ] Generate an API key
- [ ] Store it safely: `export ANTHROPIC_API_KEY="sk-..."` in your `~/.zshrc`
- [ ] Run: `source ~/.zshrc` then `echo $ANTHROPIC_API_KEY` — confirm it shows
- [ ] Run: `pip install anthropic`
- [ ] Create and run `first_ai.py` — see Claude respond
- [ ] Done when: you can send a message to Claude and print the response

### Day 9 — System Prompts & Structured Output
- [ ] Add a system prompt: make Claude respond as a pirate, then as a teacher
- [ ] Ask Claude to return JSON (e.g., `{"summary": "...", "keywords": [...]}`)
- [ ] Parse the JSON response with `json.loads()`
- [ ] Build: a script that summarizes any text, returns title + 3 bullet points as JSON
- [ ] Experiment: change `temperature` (0.0 vs 1.0) — observe the difference
- [ ] Done when: you can control Claude's persona and get structured JSON back reliably

### Day 10 — Multi-turn Conversations
- [ ] Learn: the messages array — how conversation history works
- [ ] Build: a chatbot loop (`while True` → input → send → print → repeat)
- [ ] Add conversation history: each message appends to the list
- [ ] Test: ask a follow-up question — confirm Claude remembers context
- [ ] Add a quit command (`type 'quit' to exit`)
- [ ] Save conversation to a JSON file when user quits
- [ ] Done when: you have a working terminal chatbot with memory and save/load

### Day 11 — Your First Tool (Function Calling)
- [ ] Read: [Claude Tool Use Docs](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- [ ] Define a simple tool: `get_current_time` that returns the current time
- [ ] Send it to Claude with the `tools` parameter
- [ ] Handle the `tool_use` response: detect when Claude wants to call your function
- [ ] Execute the function, send the result back as `tool_result`
- [ ] Build: add a second tool — `calculate` that evaluates a math expression
- [ ] Done when: Claude can decide to call your tools and use the results in its answer

### Day 12 — Agent Loop (The Big Unlock)
- [ ] Combine Day 11 into a loop:
  1. Send message to Claude (with tools)
  2. If Claude returns text → print it, done
  3. If Claude returns tool_use → run the tool → send result back → go to step 1
- [ ] Add 3 tools: `read_file`, `list_files`, `get_time`
- [ ] Test: ask Claude "what files are in my project folder?"
- [ ] Watch Claude call `list_files`, then maybe `read_file`, then answer
- [ ] This is the core agent pattern — everything else builds on this loop
- [ ] Done when: Claude autonomously decides which tools to call and chains them

### Day 13 — Build Something Real
- [ ] Pick ONE real problem you have
- [ ] Build an agent that solves it using 2–3 tools
- [ ] Ideas:
  - A script that reads your notes folder and answers questions about them
  - A script that checks your calendar API and summarizes your day
  - A script that reads a CSV and generates a plain-English summary
  - A script that takes a URL, fetches the page, and summarizes it
- [ ] This must solve YOUR problem, not a tutorial's problem
- [ ] Done when: you've built something you'll actually use again

### Day 14 — Review, Reflect, Git Push
- [ ] Push all week 2 code to GitHub
- [ ] Write a README explaining what each script does
- [ ] Rewrite the agent loop (Day 12) from scratch without looking
- [ ] List 3 things that surprised you this week
- [ ] List 3 things you want to build next
- [ ] Done when: code is on GitHub, you can explain the agent loop to someone else

---

## Progress Tracker

- [ ] Week 1 complete — I can write Python scripts that call APIs and save data
- [ ] Week 2 complete — I can build AI agents that use tools to solve problems
- [ ] I have pushed all code to GitHub
- [ ] I have built at least 1 thing that solves a real problem I have

---

## What's Next?

After completing Weeks 1–2, you're ready for:
- **Week 3–4**: RAG — make Claude answer questions about your own documents
- **Week 5–6**: Agentic patterns — error recovery, multi-step planning
- **Week 7–8**: MCP — expose your tools as a standard protocol

> Remember: Build > Read. Always.
