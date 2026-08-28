# A2 9618 Chapter 18: Artificial Intelligence

<div class="chapter-meta"><strong>A2 9618 · Paper 3</strong><span>9618 · 2027–2029 · Version 2</span></div>

## Official Syllabus Checklist

Revise: graphs and route search; machine-learning categories; neural networks and backpropagation.

> The checklist paraphrases the syllabus for revision. Use the official syllabus as the final authority.

## Core Knowledge

Use the topic sections below to connect definitions, processes, comparisons and calculations.


<span id="_3-one-page-mind-map" class="legacy-anchor" aria-hidden="true"></span>

## Chapter at a Glance

Use this overview to model routes, choose learning, train networks and evaluate results.

### Model graphs and search

<span lang="zh-CN">先定义节点、边和权重，再按算法更新路径代价。</span>

- A graph represents entities as vertices and relationships or routes as weighted edges.
- Dijkstra's algorithm expands the lowest known accumulated cost.
- A* combines accumulated cost with a heuristic estimate to guide the search.

**Exam cue:** Record visited nodes, tentative costs and the chosen route at each step.

### Choose a learning approach

<span lang="zh-CN">根据训练数据是否有标签以及是否使用奖励来分类。</span>

- Supervised learning trains from labelled input-output examples.
- Unsupervised learning discovers structure or clusters in unlabelled data.
- Reinforcement learning improves actions through rewards, penalties and repeated experience.

**Exam cue:** Identify the training signal and relate it to the required outcome.

### Train a neural network

<span lang="zh-CN">跟踪输入、权重、偏置、激活和误差更新。</span>

- Input values pass through weighted connections and biases to hidden and output layers.
- The network compares its prediction with the expected output to calculate error.
- Backpropagation adjusts weights to reduce future error; deep learning uses many hidden layers.

**Exam cue:** Explain how training changes weights rather than saying the network “remembers”.

### Evaluate results

<span lang="zh-CN">模型效果取决于数据、误差指标和对新数据的表现。</span>

- Regression predicts a continuous value from learned relationships.
- Training data quality and representativeness affect accuracy and bias.
- Validation on unseen data checks whether the model generalises beyond its training examples.

**Exam cue:** Connect the evaluation measure to the stated prediction or classification task.

---

## 18.1 Artificial Intelligence Overview

### What is Artificial Intelligence?

#### Student-friendly explanation
Artificial Intelligence means using computer systems to carry out tasks that normally need human intelligence.
For example, recognising patterns, making decisions, finding routes, making predictions, or learning from data.

#### Mark scheme style answer
> Artificial intelligence is the use of computer systems to perform tasks that normally require human intelligence, such as learning, reasoning, recognising patterns, making predictions, or making decisions.

#### Required ideas / marking points
+ **learning**
+ **reasoning**
+ **decision-making**
+ **pattern recognition**
+ **prediction**
+ **data**

#### Common weak answer
> AI means computers are smart.

This is too vague. You need to explain **what the computer does**.

---

### AI vs Machine Learning vs Deep Learning

| Term | Meaning | Exam focus |
| --- | --- | --- |
| Artificial Intelligence | broad area where computers perform intelligent tasks | general definition |
| Machine Learning | AI system learns from data instead of being explicitly programmed for every rule | categories and training |
| Deep Learning | type of machine learning using neural networks with many hidden layers | layers, features, predictions |


#### Simple relationship

```mermaid
flowchart TD
A[Artificial Intelligence<br/>broad field] --> B[Machine Learning<br/>learns from data]
B --> C[Deep Learning<br/>many hidden layers in neural networks]
```

#### Mark scheme style phrase
> Machine learning is a subset of AI where the system improves by learning from data. Deep learning is a subset of machine learning that uses artificial neural networks with multiple hidden layers.

---

## Graphs in Artificial Intelligence

### What is a graph?

A graph is a data structure used to show relationships between items.

| Graph part | Meaning | Example |
| --- | --- | --- |
| Node / vertex | an entity / point | city, person, web page, game location |
| Edge | a connection between nodes | road, relationship, link |
| Weight | cost of moving along an edge | distance, time, cost, risk |
| Path | a sequence of connected nodes | A → B → C |
| Cycle | a path that returns to the starting node | A → B → C → A |


#### Mark scheme answer
> A graph uses vertices / nodes to represent entities and edges to represent connections or relationships between them. Edges can be weighted to represent cost, distance, time, or another value.

#### Required ideas / marking points
+ **nodes / vertices**
+ **edges**
+ **relationships**
+ **weights**
+ **cost / distance / time**

---

### Why graphs are useful in AI

Graphs help AI represent a problem as connected possibilities.

Examples:

| Scenario | Nodes represent | Edges represent | Weight may represent |
| --- | --- | --- | --- |
| route planning | towns / cities | roads | distance / time |
| game AI | map positions | possible moves | movement cost |
| social network | people | friendships / follows | strength of connection |
| web search | webpages | hyperlinks | page importance |
| recommendation system | users / items | similarity | similarity score |


#### Mark scheme style answer
> Graphs are used in AI to record relationships between entities using nodes and edges. For example, places on a map can be represented as nodes, with edges showing routes and weights showing distance or cost.

---

### Directed and undirected graphs

| Type | Meaning | Example |
| --- | --- | --- |
| Undirected graph | edge works both ways | two-way road |
| Directed graph | edge has direction | one-way road / hyperlink |


#### Exam tip
<span lang="zh-CN">如果题目没有特别强调</span> directed graph，<span lang="zh-CN">不要主动写太复杂</span>。<span lang="zh-CN">通常写</span> **nodes, edges, weights, shortest route** <span lang="zh-CN">已经足够</span>。

---

### Weighted graph

A weighted graph has values on edges.

Example:

```mermaid
graph LR
A((A)) -- 5 --> B((B))
A -- 2 --> C((C))
C -- 1 --> B
B -- 4 --> D((D))
C -- 8 --> D
```

In this graph:

+ A to B directly costs 5
+ A to C to B costs 2 + 1 = 3
+ Therefore A → C → B is cheaper than A → B

#### Mark scheme phrase
> A weight on an edge can represent the cost of travelling between two nodes.

---

## A* and Dijkstra's Algorithms

### What these algorithms are used for

A* and Dijkstra's algorithm are graph search algorithms.
They are used to find the best route through a graph.

#### Mark scheme answer
> A* and Dijkstra's algorithms search for a shortest / lowest-cost route between two nodes in a weighted graph. Dijkstra uses accumulated edge costs; A* also uses a heuristic estimate to guide the search.

#### Required ideas / marking points
+ **shortest route**
+ **optimal route when the required conditions are met**
+ **lowest cost**
+ **between two nodes**
+ **graph**
+ **distance / cost / time**

---

### Dijkstra's algorithm

#### Student-friendly explanation
Dijkstra looks for the shortest path from a starting node by repeatedly choosing the unvisited node with the smallest known cost so far.

#### What students need to know
+ It finds the shortest path in a weighted graph.
+ It uses known edge weights.
+ It does not use a heuristic.
+ It guarantees the shortest path when edge weights are non-negative.
+ In 9618, you normally need to **use / describe purpose**, not write full code.

#### Mark scheme style answer
> Dijkstra's algorithm finds the shortest path from a start node to other nodes in a weighted graph by using the known cost / distance of edges.

---

### A* algorithm

#### Student-friendly explanation
A* also finds a route, but it uses both:

1. the cost already travelled
2. an estimated cost to the goal

This estimate is called a **heuristic**.

#### What students need to know
+ It searches for a lowest-cost route using the cost so far and an estimate of the remaining cost.
+ It uses a heuristic estimate.
+ It can be faster than Dijkstra when a good heuristic is used.
+ It is guaranteed to find an optimal route only when the heuristic does not overestimate the remaining cost.
+ It is common in game AI and route planning.

#### Mark scheme style answer
> A* searches for a lowest-cost path between nodes in a graph. It uses the cost so far and a heuristic estimate of the remaining cost to guide the search. It is guaranteed to find an optimal path when the heuristic does not overestimate the remaining cost.

---

### Dijkstra vs A*

| Feature | Dijkstra | A* |
| --- | --- | --- |
| Main purpose | shortest path | lowest-cost path guided by an estimate |
| Uses edge weights | yes | yes |
| Uses heuristic | no | yes |
| Typical strength | guaranteed shortest path with non-negative weights | can be faster if the heuristic guides the search well |
| Optimality condition | edge weights are non-negative | heuristic does not overestimate remaining cost |
| Exam wording | shortest / lowest-cost route | cost so far plus heuristic estimate |


#### Common mistake
| Mistake | Correction |
| --- | --- |
| saying A* is only for games | It can be used for any suitable graph pathfinding problem |
| saying Dijkstra uses trial and error | It systematically selects smallest known cost |
| saying A* is always optimal | Its optimality guarantee depends on a heuristic that does not overestimate remaining cost |
| forgetting graph keywords | Always mention **nodes / edges / weights** |
| writing full code | Not required by syllabus |

---

## Worked Graph Searches

Use the same directed weighted graph for both methods. The numbers on the edges are travel costs.

```mermaid
graph LR
S((Start S)) -- 2 --> A((A))
S -- 5 --> B((B))
A -- 1 --> B
A -- 4 --> C((C))
B -- 1 --> C
B -- 7 --> G((Goal G))
C -- 3 --> G
```

### Dijkstra worked search

Record a tentative cost and predecessor for every discovered node. Always select the unvisited node with the smallest tentative cost.

| Selected node | Cost made final | Updates after following its outgoing edges |
| --- | ---: | --- |
| `S` | `0` | `A=2 via S`; `B=5 via S` |
| `A` | `2` | improve `B` to `3 via A`; set `C=6 via A` |
| `B` | `3` | improve `C` to `4 via B`; set `G=10 via B` |
| `C` | `4` | improve `G` to `7 via C` |
| `G` | `7` | goal selected; stop |

The predecessor chain is `G ← C ← B ← A ← S`, so reverse it to obtain:

```text
S → A → B → C → G
total cost = 2 + 1 + 1 + 3 = 7
```

Do not stop when the goal is first discovered with cost `10`. Stop when it is selected as the lowest-cost unvisited node; by then its cost has improved to `7`.

### A* worked search

For A*, calculate:

```text
f(node) = g(node) + h(node)
```

- `g` is the known cost from `S`.
- `h` is the heuristic estimate from the node to `G`.
- Select the open node with the smallest `f`.

Use these non-overestimating heuristic values:

| Node | `S` | `A` | `B` | `C` | `G` |
| --- | ---: | ---: | ---: | ---: | ---: |
| `h` | 6 | 4 | 3 | 2 | 0 |

| Selected node | `g` | `h` | `f` | Important open-list update |
| --- | ---: | ---: | ---: | --- |
| `S` | 0 | 6 | 6 | add `A: g=2, f=6`; `B: g=5, f=8` |
| `A` | 2 | 4 | 6 | improve `B: g=3, f=6`; add `C: g=6, f=8` |
| `B` | 3 | 3 | 6 | improve `C: g=4, f=6`; add `G: g=10, f=10` |
| `C` | 4 | 2 | 6 | improve `G: g=7, f=7` |
| `G` | 7 | 0 | 7 | goal selected; stop |

A* therefore reconstructs the same route `S → A → B → C → G`, with total cost `7`. The heuristic changes which open node is preferred; it does not replace the accumulated cost or predecessor record.

---

## Machine Learning

### What is machine learning?

#### Student-friendly explanation
Machine learning means the computer learns from data. Instead of manually programming every rule, the system finds patterns and improves its predictions or decisions.

#### Mark scheme answer
> Machine learning is a component of AI where a system learns from data and improves its performance or predictions without being explicitly programmed for every rule.

#### Required ideas / marking points
+ **learns from data**
+ **patterns**
+ **training**
+ **prediction**
+ **improves performance**
+ **not explicitly programmed for every rule**

---

### Why use machine learning?

Machine learning is useful when:

+ rules are too complex to write manually
+ there is a lot of data
+ patterns are hidden or difficult for humans to identify
+ the system needs to improve from experience
+ predictions are needed from previous examples

#### Scenario answer
> Machine learning is suitable because the system can learn patterns from large amounts of data and use these patterns to make predictions or decisions.

---

## Supervised Learning

### Definition

Supervised learning uses labelled training data.

A label is the correct answer already attached to an example.

#### Example
| Input data | Label |
| --- | --- |
| email text | spam / not spam |
| house size, location | house price |
| image of animal | cat / dog |
| symptoms | disease type |


#### Mark scheme answer
> Supervised learning uses labelled data, where known outcomes are applied to specific inputs so that the AI can learn to predict outcomes for new data.

#### Required ideas / marking points
+ **labelled data**
+ **known outcomes**
+ **input-output pairs**
+ **training data**
+ **predict outcomes**

---

### When to use supervised learning

Use supervised learning when:

+ you already have many examples with correct answers
+ the task is classification or prediction
+ the system should learn the mapping from input to output

#### Example answer
> Supervised learning would be suitable because historical examples already include the correct outcome, so the model can learn from labelled input-output pairs.

---

## Unsupervised Learning

### Definition

Unsupervised learning uses unlabelled data.
The system has to find patterns by itself.

#### Example
| Input data | What AI may find |
| --- | --- |
| customer shopping history | groups of similar customers |
| website behaviour | user behaviour patterns |
| image dataset | similar image clusters |
| network traffic | unusual patterns |


#### Mark scheme answer
> Unsupervised learning uses unlabelled data. The system searches for hidden patterns, structures, or clusters within the data without known outcomes.

#### Required ideas / marking points
+ **unlabelled data**
+ **no known outcomes**
+ **hidden patterns**
+ **structures**
+ **clusters**
+ **no initial human labelling**

---

### Supervised vs unsupervised learning

| Feature | Supervised learning | Unsupervised learning |
| --- | --- | --- |
| Data type | labelled data | unlabelled data |
| Output known during training? | yes | no |
| Human input | labels are provided | labels are not provided |
| Main purpose | predict known output | discover hidden patterns |
| Example | classify emails as spam/not spam | group customers by behaviour |


#### Mark scheme style comparison
> Supervised learning uses labelled data with known outcomes, while unsupervised learning uses unlabelled data where outcomes are not known. Unsupervised learning searches for hidden patterns or clusters in the data.

---

## Reinforcement Learning

### Definition

Reinforcement learning is learning by trial and error.

The AI interacts with an environment, takes actions, and receives rewards or penalties.

#### Example
| Scenario | Action | Reward / penalty |
| --- | --- | --- |
| game AI | move left/right/attack | win points / lose health |
| robot navigation | choose direction | closer to target / collision |
| self-driving simulation | accelerate / brake | safe travel / crash |
| trading bot | buy / sell | profit / loss |


#### Mark scheme answer
> Reinforcement learning enables learning in an interactive environment by trial and error using rewards and penalties from its own experiences.

#### Required ideas / marking points
+ **interactive environment**
+ **trial and error**
+ **actions**
+ **reward**
+ **penalty**
+ **experience**
+ **maximise reward**

---

### Why use reinforcement learning?

Use reinforcement learning when:

+ the system must make a sequence of decisions
+ there is no simple labelled answer for every action
+ the AI can learn by receiving feedback
+ the best action depends on the current state
+ the goal is to maximise reward over time

#### Scenario answer
> Reinforcement learning is suitable because the agent can try different actions in an environment and improve by using rewards or penalties as feedback.

---

### Common mistake

| Mistake | Correction |
| --- | --- |
| saying reinforcement learning uses labelled examples | It learns from reward / penalty feedback, not labelled input-output pairs |
| saying it is the same as unsupervised learning | Reinforcement learning uses interaction with an environment |
| forgetting reward | Reward / penalty is the key phrase |
| writing only "trial and error" | Add **interactive environment** and **rewards / penalties** |

---

## Artificial Neural Networks (ANNs)

### What is an artificial neural network?

An artificial neural network is a computer model inspired by the human brain.
It uses many connected processing units called nodes / neurons.

#### Mark scheme answer
> An artificial neural network is designed to work in a similar way to the human brain. It has many connected processing units / nodes arranged in layers that work together to process data and learn from data.

#### Required ideas / marking points
+ **human brain**
+ **connected processing units**
+ **nodes / neurons**
+ **layers**
+ **weights**
+ **learn from data**
+ **process data**

---

### Structure of an ANN

```mermaid
flowchart LR
I1((Input 1)) --> H1((Hidden node))
I2((Input 2)) --> H1
I1 --> H2((Hidden node))
I2 --> H2
H1 --> O((Output))
H2 --> O
```

| Layer | Purpose |
| --- | --- |
| Input layer | receives input data |
| Hidden layer | processes data and extracts features |
| Output layer | gives prediction / classification |


#### Mark scheme phrase
> Artificial neural networks have input, hidden and output layers, with nodes connected by weighted links.

---

### Weights and biases

Each connection can have a **weight**.
The weight controls how strongly one node affects another node.

During training:

+ the network makes a prediction
+ the prediction is compared with the correct output
+ an error is calculated
+ weights are adjusted
+ the model becomes more accurate

#### Mark scheme phrase
> Weights are adjusted through training to reduce error and give a more accurate result.

---

## Deep Learning

### Definition

Deep learning is a type of machine learning that uses artificial neural networks with many hidden layers.

#### Mark scheme answer
> Deep learning uses artificial neural networks with multiple hidden layers to extract complex features from data and make predictions or decisions.

#### Required ideas / marking points
+ **artificial neural network**
+ **multiple hidden layers**
+ **complex features**
+ **learn from data**
+ **predictions**
+ **large amounts of data**

---

### Why deep learning is useful

Deep learning is useful when:

+ the problem is complex
+ there is a large amount of data
+ useful features are difficult for humans to define manually
+ the system needs to identify hidden patterns
+ tasks involve images, speech, language, or complex prediction

#### Example
| Task | Why deep learning helps |
| --- | --- |
| image recognition | detects complex visual features |
| speech recognition | finds patterns in audio signals |
| medical scan analysis | detects subtle image patterns |
| natural language processing | identifies meaning and relationships in text |


#### Mark scheme style answer
> Deep learning is useful because multiple hidden layers allow the model to extract complex features from large amounts of data and make more accurate predictions.

---

### Deep learning vs normal machine learning

| Feature | Machine learning | Deep learning |
| --- | --- | --- |
| Broadness | wider category | subset of machine learning |
| Model | many possible models | neural networks with many layers |
| Feature extraction | may need human-designed features | can learn features automatically |
| Data need | can work with smaller datasets | usually needs large datasets |
| Processing | often less demanding | usually more processing power |


---

## Back Propagation of Errors

### What is back propagation?

Back propagation is a training method used in neural networks.

The network:

1. makes an output prediction
2. compares the prediction with the expected output
3. calculates the error
4. sends the error backwards through the network
5. adjusts weights to reduce future error

#### Mermaid process

```mermaid
flowchart TD
A[Input data] --> B[Forward pass through network]
B --> C[Output prediction]
C --> D[Compare with expected output]
D --> E[Calculate error]
E --> F[Send error backwards<br/>back propagation]
F --> G[Adjust weights]
G --> H[Prediction becomes more accurate]
```

#### Mark scheme answer
> Back propagation is where the error between the predicted output and expected output is passed backwards through the network so that weights can be adjusted to reduce the error.

#### Required ideas / marking points
+ **predicted output**
+ **expected output**
+ **error**
+ **passed backwards**
+ **adjust weights**
+ **reduce error**
+ **training**

---

### Common mistake

| Mistake | Correction |
| --- | --- |
| saying "it sends data backwards" | It sends **error information** backwards |
| saying "it fixes the answer" | It adjusts weights to reduce future error |
| giving calculus explanation | Not needed for 9618 |
| missing weights | Weight adjustment is central |

---

## Regression Methods in Machine Learning

### What is regression?

Regression is used to predict a continuous numeric value.

#### Examples
| Data | Predicted value |
| --- | --- |
| house size, location | house price |
| hours studied | exam score |
| temperature, humidity | energy demand |
| previous sales | future sales |


#### Mark scheme style answer
> Regression is a machine learning method used to model the relationship between variables and predict a continuous numerical value.

#### Required ideas / marking points
+ **relationship between variables**
+ **predict**
+ **continuous value**
+ **numeric output**
+ **trend / pattern**

---

### Classification vs regression

| Feature | Classification | Regression |
| --- | --- | --- |
| Output type | category / class | continuous number |
| Example output | spam / not spam | price = 250000 |
| Question type | "Which class?" | "How much / how many?" |
| Example | disease type | blood pressure value |


#### Exam tip
<span lang="zh-CN">如果题目是预测</span> **price, score, temperature, distance, time, demand**，<span lang="zh-CN">通常是</span> regression。
<span lang="zh-CN">如果题目是预测</span> **cat/dog, spam/not spam, pass/fail**，<span lang="zh-CN">通常是</span> classification。

---

## Mark Scheme Keywords

### Graphs in AI
+ **nodes / vertices**
+ **edges**
+ **relationships**
+ **weighted edges**
+ **cost / distance / time**
+ **shortest route**
+ **optimal path when the algorithm conditions are met**

### A* and Dijkstra
+ **shortest path**
+ **lowest-cost path**
+ **between two nodes**
+ **weighted graph**
+ **heuristic** for A*
+ **known edge costs** for Dijkstra

### Supervised learning
+ **labelled data**
+ **known outcomes**
+ **input-output pairs**
+ **training data**
+ **predict outcomes**

### Unsupervised learning
+ **unlabelled data**
+ **unknown outcomes**
+ **hidden patterns**
+ **clusters**
+ **structures in data**

### Reinforcement learning
+ **trial and error**
+ **interactive environment**
+ **agent**
+ **actions**
+ **reward**
+ **penalty**
+ **learns from experience**

### Artificial neural networks
+ **human brain**
+ **connected processing units**
+ **nodes / neurons**
+ **input layer**
+ **hidden layers**
+ **output layer**
+ **weights**
+ **biases**
+ **training**

### Deep learning
+ **multiple hidden layers**
+ **extract complex features**
+ **large amounts of data**
+ **make predictions**
+ **adjust weights**

### Back propagation
+ **error**
+ **predicted output**
+ **expected output**
+ **passed backwards**
+ **adjust weights**
+ **reduce error**

### Regression
+ **relationship between variables**
+ **continuous numerical value**
+ **prediction**
+ **trend**
+ **model**

---

## Topic-Specific Common Confusions

| Mistake | Why it loses marks | Better answer |
| --- | --- | --- |
| AI = robot | Too narrow | AI performs tasks requiring human intelligence |
| graph = chart | Wrong meaning in CS | graph = nodes and edges |
| edge = node | Confuses graph structure | node = entity, edge = connection |
| A* and Dijkstra are sorting algorithms | Wrong topic | They search for shortest / lowest-cost routes in graphs |
| supervised learning = someone gives the computer answers | Too vague | supervised learning uses labelled data |
| unsupervised learning = no training | Wrong | it uses unlabelled data and finds hidden patterns |
| reinforcement learning = repeating practice | Too vague | trial and error with rewards/penalties |
| deep learning = AI learns deeply | Not technical | neural network with multiple hidden layers |
| ANN = normal program | Wrong | connected nodes arranged in layers, weights adjusted |
| back propagation = data goes backward | Incomplete | error is passed backward to adjust weights |
| regression = going backwards | Wrong English interpretation | predicts continuous numeric values |

---

## Scenario Answer Bank

### Route-finding AI
#### Scenario
A delivery company wants to find the fastest route between warehouses.

#### Answer template
> A graph can be used because the warehouses can be represented as nodes and roads can be represented as edges. The edges can be weighted using distance or travel time. A* or Dijkstra's algorithm can then be used to find the shortest / lowest-cost route between two nodes.

---

### Game character movement
#### Scenario
A game enemy needs to move from its current position to the player.

#### Answer template
> The map can be represented as a graph, with positions as nodes and possible movements as edges. Weights can represent distance or movement cost. A* is suitable because it can use a heuristic estimate of the remaining distance to guide the search towards the target.

---

### Email spam detection
#### Scenario
A company has thousands of emails already labelled as spam or not spam.

#### Answer template
> Supervised learning is suitable because the training data is labelled with known outcomes. The model can learn the relationship between email features and the correct label, then predict whether new emails are spam.

---

### Customer grouping
#### Scenario
A shop has customer purchase data but no pre-defined customer categories.

#### Answer template
> Unsupervised learning is suitable because the data is unlabelled. The AI can search for hidden patterns or clusters in the customer behaviour and group similar customers together.

---

### Robot learning to navigate
#### Scenario
A robot learns to move through a maze.

#### Answer template
> Reinforcement learning is suitable because the robot can learn by trial and error in an interactive environment. It receives rewards for moving closer to the goal and penalties for hitting walls or taking inefficient routes.

---

### Predicting house prices
#### Scenario
A model predicts a house price from size, location and number of bedrooms.

#### Answer template
> Regression is suitable because the output is a continuous numerical value. The model can learn the relationship between input variables and house price from training data.

---

### Medical image recognition
#### Scenario
A system analyses medical scans to detect signs of disease.

#### Answer template
> Deep learning is suitable because artificial neural networks with multiple hidden layers can extract complex features from image data. The model can learn patterns that may be difficult for humans to define manually.

---

## Mermaid Process Diagrams

### Machine learning category decision

```mermaid
flowchart TD
A[Machine learning task] --> B{Does training data have labels?}
B -->|Yes| C[Supervised learning<br/>labelled data / known outcomes]
B -->|No| D{Does the system learn by actions<br/>with rewards or penalties?}
D -->|Yes| E[Reinforcement learning<br/>trial and error]
D -->|No| F[Unsupervised learning<br/>hidden patterns / clusters]
```

### ANN training process

```mermaid
flowchart LR
A[Training data] --> B[Input layer]
B --> C[Hidden layers]
C --> D[Output layer]
D --> E[Prediction]
E --> F[Compare with expected output]
F --> G[Calculate error]
G --> H[Back propagation]
H --> I[Adjust weights]
I --> C
```

### Graph search idea

```mermaid
flowchart LR
A((Start)) -- cost 4 --> B((B))
A -- cost 2 --> C((C))
C -- cost 1 --> B
B -- cost 3 --> D((Goal))
C -- cost 8 --> D
```

Best path by cost:

```text
A → C → B → D = 2 + 1 + 3 = 6
A → B → D = 4 + 3 = 7
A → C → D = 2 + 8 = 10
```

---

## Required Ideas and Exam Language

Use technical terms as part of a complete statement: identify the component or method, state what it does, then link its effect to the question context. A keyword without a correct relationship is not a complete marking point.

## Common Confusions

- Do not substitute a related term for the process named in the question.
- Do not list advantages or definitions without linking them to the stated context.

## Worked Examples

The worked calculations, process templates and scenario answers above model the chain of reasoning expected in examination responses. Rework each example before reading its answer.

## 10-Mark Quick Check

**Total: 10 marks**

### Questions
1. State two components of a graph. [2]
2. State what a weight on an edge may represent. [1]
3. State the purpose of Dijkstra's algorithm. [1]
4. Give one difference between supervised and unsupervised learning. [2]
5. State what reinforcement learning uses to improve behaviour. [1]
6. State the three main layers of an artificial neural network. [3]

## Quick Check Answers
1. Nodes / vertices [1], edges [1]
2. Cost / distance / time / risk [1]
3. To find the shortest / lowest-cost path between nodes in a graph [1]
4. Supervised learning uses labelled data / known outcomes [1], unsupervised learning uses unlabelled data / finds hidden patterns [1]
5. Rewards and penalties / trial and error feedback [1]
6. Input layer [1], hidden layer(s) [1], output layer [1]

---

## 20-Mark Exam Practice

**Total: 20 marks**

### Question 1: Graphs and route searching [6]
A delivery company uses the following directed weighted graph. Edge weights represent travel time.

```mermaid
graph LR
P((P)) -- 2 --> Q((Q))
P -- 6 --> R((R))
Q -- 1 --> R
Q -- 7 --> T((T))
R -- 3 --> T
```

(a) Explain how the graph represents the route problem, including the meaning of its weights. [2]

(b) Use Dijkstra's algorithm from `P` to `T`. State the order in which nodes become final, then give the lowest-cost route and total cost. [2]

(c) For A*, use `h(P)=5`, `h(Q)=4`, `h(R)=2`, `h(T)=0`. State the order in which nodes are selected, then give the route and total cost. [2]

#### Question 1 mark scheme
(a)
+ towns/locations are represented as nodes and possible routes as directed edges [1]
+ weights represent travel time / the cost of following each route [1]

(b)
+ selected/final order `P, Q, R, T`; valid tentative updates include `Q=2`, `R` improving from `6` to `3`, and `T` improving from `9` to `6` [1]
+ route `P → Q → R → T`, total cost `2 + 1 + 3 = 6` [1]

(c)
+ selected order `P, Q, R, T`, using the smallest `f=g+h` at each step [1]
+ route `P → Q → R → T`, total cost `6` [1]

---

### Question 2: Machine learning categories [5]
A website wants to recommend products to users. It has a large amount of shopping data but no pre-defined customer categories.

(a) Identify the most suitable machine learning category. [1]

(b) Explain your answer. [2]

(c) Explain why supervised learning may not be suitable. [2]

#### Question 2 mark scheme
(a) Unsupervised learning [1]

(b)
+ data is unlabelled / categories are not already known [1]
+ system can find hidden patterns / group customers into clusters based on behaviour [1]

(c)
+ supervised learning needs labelled data / known outcomes [1]
+ there are no pre-defined correct customer categories / labels [1]

---

### Question 3: Neural networks, deep learning and regression [9]
A hospital uses an AI system to analyse medical images.

(a) Describe the structure of an artificial neural network. [3]

(b) Explain what is meant by deep learning. [2]

(c) Explain how back propagation helps the model improve. [2]

(d) A second model uses patient age, treatment data and test results to predict the number of recovery days. Explain why regression is suitable for this prediction. [2]

#### Question 3 mark scheme
(a)
+ has connected processing units / nodes / neurons [1]
+ arranged in layers: input, hidden and output [1]
+ connections have weights / weights affect output [1]

(b)
+ uses artificial neural networks [1]
+ uses multiple hidden layers to extract increasingly complex features [1]

(c)
+ error between predicted and expected output is calculated and passed backwards [1]
+ weights are adjusted to reduce future error / improve accuracy [1]

(d)
+ regression models the relationship between the patient input variables and the predicted result [1]
+ recovery time is a continuous numerical value rather than a class / category [1]

---

## Final Revision Checklist

- [ ] I can model graph search and compare traversal strategies.
- [ ] I can distinguish supervised, unsupervised and reinforcement learning.
- [ ] I can explain neural-network training and backpropagation.
- [ ] I can distinguish classification from regression and evaluate results.
- [ ] I can complete and self-mark both chapter practices.
