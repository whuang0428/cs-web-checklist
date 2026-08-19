# A2 9618 Chapter 17: Security

<div class="chapter-meta"><strong>A2 9618 · Paper 3</strong><span>9618 · 2027–2029 · Version 2</span></div>

## Official Syllabus Checklist

Revise: symmetric and asymmetric cryptography; TLS; certificates, signatures and quantum cryptography.

> The checklist paraphrases the syllabus for revision. Use the official syllabus as the final authority.

## Core Knowledge

Use the topic sections below to connect definitions, processes, comparisons and calculations.


<span id="_3-one-page-mind-map" class="legacy-anchor" aria-hidden="true"></span>

## Chapter at a Glance

Use this overview to choose encryption, protect or verify messages, establish trust and evaluate quantum methods.

### Choose encryption

<span lang="zh-CN">根据速度、密钥分发和通信阶段选择对称或非对称加密。</span>

- Symmetric encryption uses one shared secret key for encryption and decryption.
- Asymmetric encryption uses a mathematically related public and private key pair.
- Symmetric methods are faster, while asymmetric methods solve initial shared-key distribution.

**Exam cue:** Compare key use and explain why the method fits the stage of communication.

### Secure or verify messages

<span lang="zh-CN">保密使用接收者密钥，身份验证使用发送者密钥。</span>

- Encrypt confidential data with the receiver's public key so only their private key decrypts it.
- Sign a digest with the sender's private key so the sender's public key verifies it.
- A digital signature supports authenticity and integrity but does not itself hide the message.

**Exam cue:** Identify whose key is used, whether it is public or private, and the intended property.

### Establish TLS trust

<span lang="zh-CN">证书验证服务器身份，握手建立后续会话密钥。</span>

- A certificate authority signs a certificate that binds an identity to a public key.
- The client validates the certificate, issuer, domain and validity period.
- The TLS handshake establishes secure session keys used for efficient encrypted communication.

**Exam cue:** Separate certificate validation from later symmetric session encryption.

### Evaluate quantum cryptography

<span lang="zh-CN">评价量子密钥分发时同时考虑窃听检测和现实限制。</span>

- Quantum states can reveal interception because measurement changes the transmitted state.
- The method can distribute key material with evidence of eavesdropping.
- High cost, specialist hardware, noise and distance limit practical deployment.

**Exam cue:** Give both the security advantage and an implementation limitation.

---

## 17.1 Encryption, Encryption Protocols and Digital Certificates

### Core encryption vocabulary

| Term | Chinese explanation | Mark scheme style phrase |
| --- | --- | --- |
| Plaintext | <span lang="zh-CN">原始可读信息</span> | original readable message/data |
| Ciphertext | <span lang="zh-CN">加密后的不可读信息</span> | encrypted unreadable message/data |
| Encryption | <span lang="zh-CN">把明文变成密文</span> | converting plaintext into ciphertext using an algorithm and key |
| Decryption | <span lang="zh-CN">把密文还原成明文</span> | converting ciphertext back into plaintext using a key |
| Key | <span lang="zh-CN">控制加密</span>/<span lang="zh-CN">解密过程的数据</span> | value used by the encryption/decryption algorithm |
| Cryptography | <span lang="zh-CN">加密通信的方法</span> | method of protecting data using encryption techniques |

#### Mark scheme answer

> Encryption is the process of converting plaintext into ciphertext using an encryption algorithm and a key, so that the data cannot be understood if intercepted.

#### Required ideas / marking points

+ **plaintext**
+ **ciphertext**
+ **algorithm**
+ **key**
+ **encrypted / decrypted**
+ **intercepted data cannot be read**

#### Common weak answer

> Encryption makes data secure.

This is too vague. You must say **how**: plaintext becomes ciphertext using a key.

---

### Symmetric key cryptography

#### Definition

> Symmetric cryptography uses the same shared secret key to encrypt and decrypt data.

```mermaid
sequenceDiagram
    participant A as Sender
    participant B as Receiver
    A->>A: Encrypt plaintext using shared secret key
    A->>B: Send ciphertext
    B->>B: Decrypt ciphertext using the same shared key
```

#### Key points

| Feature | Explanation |
| --- | --- |
| Number of keys | one shared secret key |
| Encryption | sender uses the shared key |
| Decryption | receiver uses the same shared key |
| Speed | usually faster than asymmetric encryption |
| Main problem | key must be shared securely before communication |

#### Benefit

> Symmetric encryption is fast and efficient, so it is suitable for encrypting large amounts of data.

#### Drawback

> The shared key must be sent or agreed securely; if the key is intercepted, the encrypted data can be decrypted.

#### Exam sentence bank

| Question style | Answer template |
| --- | --- |
| Describe symmetric cryptography | It uses the same key for both encryption and decryption. Both sender and receiver must know the shared secret key. |
| Give a benefit | It is faster / requires less processing power, so it is suitable for large data transfers. |
| Give a drawback | The key distribution problem: the shared key must be sent securely before communication. |
| Compare with asymmetric | Symmetric uses one shared key, while asymmetric uses a public/private key pair. |

---

### Asymmetric key cryptography

#### Definition

> Asymmetric cryptography uses a matching pair of keys: a public key and a private key. Data encrypted with one key can only be decrypted with the matching key.

| Key | Who can access it? | Role |
| --- | --- | --- |
| Public key | can be shared openly | used by others to encrypt data or verify signatures |
| Private key | kept secret by owner | used by owner to decrypt data or create digital signatures |

#### Important rule

> The public key and private key are mathematically linked, but the private key should not be derivable from the public key.

#### Benefit

> The sender does not need to share a secret key before sending a private message.

#### Drawback

> Asymmetric encryption is usually slower and needs more processing than symmetric encryption.

---

## Two Different Uses of Public and Private Keys

This is the most important part of Chapter 17. Students lose marks because they mix up these two cases.

---

### Case 1: Sending a private message to an individual / organisation

#### Scenario

Fred wants to send a private message to Sheila. Only Sheila should be able to read it.

#### Correct key direction

```mermaid
sequenceDiagram
    participant F as Fred / Sender
    participant S as Sheila / Receiver
    S->>F: Sheila's public key is available
    F->>F: Encrypt plaintext using Sheila's public key
    F->>S: Send ciphertext
    S->>S: Decrypt ciphertext using Sheila's private key
```

#### Mark scheme answer

> The sender encrypts the plaintext using the receiver's public key. The ciphertext is sent to the receiver. Only the receiver can decrypt it using the receiver's private key.

#### Why this works

+ Everyone may know Sheila's **public key**.
+ Only Sheila has Sheila's **private key**.
+ Therefore only Sheila can decrypt the ciphertext.

#### Common mistake

| Mistake | Correction |
| --- | --- |
| encrypt with sender's public key | use receiver's public key for privacy |
| receiver decrypts with public key | receiver decrypts with their private key |
| private key is sent to sender | private key is never sent |
| public key must be hidden | public key can be shared openly |

---

### Case 2: Sending a verified message to the public

#### Scenario

A school wants to publish a message and prove that the message really came from the school.

This is not mainly about secrecy. It is about:

+ **authentication**: proving who sent it
+ **integrity**: showing the message has not been changed
+ **non-repudiation**: sender cannot easily deny sending it

#### Correct key direction

```mermaid
sequenceDiagram
    participant S as Sender / Organisation
    participant P as Public / Receiver
    S->>S: Create hash/digest of message
    S->>S: Encrypt/sign digest using sender's private key
    S->>P: Send message + digital signature
    P->>P: Use sender's public key to verify signature
```

#### Mark scheme answer

> The sender creates a digital signature using their private key. The receiver uses the sender's public key to check the signature. If the check is successful, the receiver can verify the sender's identity and that the message has not been altered.

#### Why this works

+ Only the sender has the sender's **private key**.
+ Anyone can use the sender's **public key** to check the signature.
+ If verification succeeds, the message can be linked to the sender.

#### Common mistake

| Mistake | Correction |
| --- | --- |
| using receiver's public key for signature | sender signs using sender's private key |
| saying digital signature hides the message | digital signature verifies identity / integrity |
| saying public key decrypts the whole private message | public key verifies the signature, not necessarily the whole message |

---

## Symmetric vs Asymmetric Cryptography

| Feature | Symmetric cryptography | Asymmetric cryptography |
| --- | --- | --- |
| Keys used | one shared secret key | public key + private key pair |
| Encryption/decryption | same key | matching key pair |
| Speed | faster | slower |
| Key distribution | difficult because shared key must be exchanged securely | easier because public key can be shared |
| Main use | bulk data encryption / session data | key exchange, digital signatures, secure initial communication |
| Risk | if shared key is intercepted, messages can be read | if private key is stolen, identity/security is compromised |

### Exam-style comparison

> Symmetric cryptography uses a single shared key to encrypt and decrypt data, while asymmetric cryptography uses a public/private key pair. Symmetric cryptography is faster, but the shared key must be distributed securely. Asymmetric cryptography avoids sending a shared secret key first, but it is slower and requires more processing.

---

## SSL / TLS

### Purpose of SSL/TLS

SSL means **Secure Socket Layer**. TLS means **Transport Layer Security**.

In modern wording, TLS is the newer and more secure protocol, but exam answers often accept SSL/TLS together.

#### Mark scheme answer

> SSL/TLS provides secure client-server communication over a network by encrypting data, authenticating the server, and helping maintain data integrity.

#### Required ideas / marking points

+ **secure communication**
+ **client-server**
+ **encryption**
+ **authentication**
+ **data integrity**
+ **digital certificate**
+ **session key**
+ **HTTPS**

---

### Where SSL/TLS is appropriate

| Situation | Why SSL/TLS is suitable |
| --- | --- |
| online banking | protects account and transaction details |
| online shopping | protects card/payment details |
| login page | protects username and password |
| sending personal data | keeps confidential data encrypted |
| webmail | protects message content and login details |
| API communication | protects data between client and server |

#### Scenario answer

> SSL/TLS is appropriate for online banking because confidential data such as login details and transaction information is transmitted between a client and a server. SSL/TLS encrypts the data, authenticates the server using a digital certificate, and helps protect the data from being altered during transmission.

---

### Simplified TLS handshake process

You do not need full industry-level TLS detail, but you should know the logic.

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    C->>S: Request secure connection
    S->>C: Send digital certificate + public key
    C->>C: Validate certificate using CA
    C->>S: Send encrypted data for session key setup
    S->>S: Decrypt using server private key
    C->>S: Encrypted session starts
    S->>C: Data exchanged using symmetric session key
```

#### Step-by-step version

1. Client connects to server and requests a secure session.
2. Server sends a **digital certificate** containing the server's public key.
3. Client checks / validates the certificate using a **Certificate Authority**.
4. Client and server establish a **session key**.
5. The session key is used for symmetric encryption during the session.
6. Encrypted data is exchanged.

#### Why both asymmetric and symmetric are used

| Stage | Method | Reason |
| --- | --- | --- |
| initial handshake | asymmetric | allows secure key exchange and server authentication |
| data transfer | symmetric session key | faster for large amounts of data |

#### Common mistake

| Mistake | Correction |
| --- | --- |
| SSL/TLS only uses asymmetric encryption | it normally uses asymmetric for setup and symmetric for session data |
| certificate encrypts the data | certificate helps authenticate identity and provide public key |
| TLS only checks password | TLS secures communication, not just passwords |

---

## Digital Certificates

### What is a digital certificate?

A digital certificate is an electronic document used to prove the identity of a website, person or organisation.

It normally contains:

+ owner's identity / domain name
+ owner's public key
+ certificate issuer / Certificate Authority
+ validity period
+ digital signature of the CA

#### Mark scheme answer

> A digital certificate is an electronic document issued by a Certificate Authority that links an entity's identity to its public key.

---

### Certificate Authority (CA)

A **Certificate Authority** is a trusted organisation that issues digital certificates.

#### What the CA does

1. checks the identity of the website / organisation
2. issues a digital certificate
3. digitally signs the certificate
4. allows users/browsers to verify that the certificate is trusted

#### Mark scheme answer

> A Certificate Authority verifies the identity of an organisation and issues a digital certificate containing the organisation's public key.

---

### How a digital certificate is acquired

```mermaid
flowchart TD
A[Organisation generates key pair] --> B[Organisation creates certificate request]
B --> C[Request sent to Certificate Authority]
C --> D[CA checks identity / domain ownership]
D --> E[CA issues digital certificate]
E --> F[Certificate includes public key + identity]
F --> G[CA digitally signs certificate]
```

#### Exam answer

> The organisation generates a public/private key pair and sends a certificate request to a Certificate Authority. The CA checks the organisation's identity or domain ownership. If valid, the CA issues a digital certificate containing the organisation's public key and identity details, signed by the CA.

---

### How a digital certificate is used in TLS

```mermaid
flowchart LR
A[Client visits HTTPS website] --> B[Server sends digital certificate]
B --> C[Browser checks CA signature]
C --> D[Browser checks domain name and validity date]
D --> E{Certificate trusted?}
E -->|Yes| F[Secure connection continues]
E -->|No| G[Warning / connection blocked]
```

#### Mark scheme phrases

+ **authenticate the identity of a website**
+ **contains the public key**
+ **issued by a Certificate Authority**
+ **CA signature can be checked**
+ **used to establish secure communication**

---

## Digital Signatures

### Purpose

A digital signature is used to prove:

1. **authentication** — who sent the message
2. **integrity** — message has not been changed
3. **non-repudiation** — sender cannot easily deny sending it

### How a digital signature is produced

```mermaid
flowchart TD
A[Original message] --> B[Hash algorithm]
B --> C[Message digest]
C --> D[Encrypt digest with sender private key]
D --> E[Digital signature]
E --> F[Send message + signature]
```

### How a digital signature is verified

```mermaid
flowchart TD
A[Receiver gets message + signature] --> B[Receiver hashes received message]
C[Receiver decrypts signature using sender public key] --> D[Original digest]
B --> E{Digests match?}
D --> E
E -->|Yes| F[Sender verified + message unchanged]
E -->|No| G[Invalid signature / message altered]
```

#### Mark scheme answer

> The sender creates a hash of the message and encrypts the hash using their private key to create a digital signature. The receiver decrypts the signature using the sender's public key and compares the result with a newly calculated hash of the received message. If they match, the message has not been changed and the sender is verified.

#### Common mistakes

| Mistake | Why wrong |
| --- | --- |
| digital signature encrypts the whole message | usually signs a hash/digest, not necessarily the whole message |
| digital signature keeps message secret | it proves identity/integrity; encryption gives secrecy |
| receiver uses receiver's public key | receiver uses sender's public key to verify |

---

## Quantum Cryptography

### Purpose

Quantum cryptography is used to create highly secure communication, especially for key exchange.

#### Mark scheme answer

> Quantum cryptography uses the principles of quantum mechanics / properties of photons to provide secure communication and detect eavesdropping.

### Benefits

| Benefit | Mark scheme style explanation |
| --- | --- |
| eavesdropping can be detected | observing quantum states changes them, so interception can be noticed |
| very high security | security is based on physics rather than only mathematical difficulty |
| useful for sensitive data | suitable for government / financial / military data |
| supports secure key exchange | keys can be exchanged with detection of interception |

### Drawbacks

| Drawback | Explanation |
| --- | --- |
| expensive | specialist equipment is required |
| limited distance | current systems may work only over limited distances without trusted nodes/repeaters |
| still developing | not as widely deployed as conventional cryptography |
| does not solve every security issue | endpoints can still be attacked |
| high error rates / environmental sensitivity | transmission can be affected by noise or fibre conditions |

#### Exam answer: benefit and drawback

> A benefit of quantum cryptography is that eavesdropping can be detected because measuring quantum states changes them. A drawback is that it requires expensive specialist equipment and is not yet widely practical over long distances.

---

## Mark Scheme Keywords

### Encryption

+ **plaintext**
+ **ciphertext**
+ **algorithm**
+ **key**
+ **encrypt**
+ **decrypt**
+ **intercepted data cannot be understood**

### Symmetric cryptography

+ **same key**
+ **shared secret key**
+ **encrypt and decrypt**
+ **fast / efficient**
+ **key distribution problem**
+ **key must be kept secret**

### Asymmetric cryptography

+ **public key**
+ **private key**
+ **key pair**
+ **matching key**
+ **public key can be shared**
+ **private key kept secret**
+ **encrypted with one key, decrypted with the other**

### SSL/TLS

+ **secure communication**
+ **client-server**
+ **digital certificate**
+ **server authentication**
+ **session key**
+ **encrypted session**
+ **data integrity**
+ **HTTPS**

### Digital certificate

+ **electronic document**
+ **Certificate Authority / CA**
+ **identity of website / organisation**
+ **public key**
+ **CA digital signature**
+ **validity period**
+ **authenticate**

### Digital signature

+ **hash / message digest**
+ **sender's private key**
+ **sender's public key**
+ **authentication**
+ **integrity**
+ **non-repudiation**
+ **message has not been altered**

### Quantum cryptography

+ **quantum mechanics**
+ **photons**
+ **eavesdropping detected**
+ **properties change when observed**
+ **high cost**
+ **limited distance**
+ **specialist equipment**

---

## Topic-Specific Common Confusions

| Mistake | Why it loses marks | Correct answer |
| --- | --- | --- |
| Public key is secret | Public key is designed to be shared | Private key is secret |
| Private key is sent to receiver | Private key must never be shared | Send/use public key instead |
| Symmetric uses two keys | That is asymmetric | Symmetric uses one shared key |
| Asymmetric is always used for all data | Too slow for bulk data | Often used to exchange session key, then symmetric used |
| Digital certificate = digital signature | They are different concepts | Certificate links identity to public key; signature verifies message/sender |
| Digital signature hides the message | Signature verifies, not hides | Encryption hides content |
| TLS is just encryption | Too narrow | TLS also authenticates and helps protect integrity |
| CA encrypts all web traffic | CA issues/signs certificates | Session encryption is done by client/server |
| Quantum cryptography means quantum computer | Not exactly | It uses quantum properties for security/key exchange |
| Saying “more secure” without reason | Vague | Explain eavesdropping detection / private key / CA authentication |

---

## Scenario Answer Bank

### Online banking uses HTTPS

> HTTPS uses SSL/TLS to create a secure client-server session. The bank server sends a digital certificate containing its public key. The browser checks that the certificate is trusted and issued by a Certificate Authority. A session key is established and used to encrypt data such as passwords and transaction details. This helps provide confidentiality, authentication and data integrity.

---

### A customer sends a private message to a company

> The customer obtains the company's public key, often from a digital certificate. The customer encrypts the plaintext using the company's public key to produce ciphertext. The ciphertext is sent to the company. Only the company can decrypt the message because only the company has the matching private key.

---

### A software company signs an update

> The software company creates a hash of the update and encrypts the hash using its private key to create a digital signature. The user's computer uses the company's public key to verify the signature. If the calculated hash matches the decrypted hash, the update is verified as coming from the company and not being altered.

---

### A school wants to prove its website is genuine

> The school applies to a Certificate Authority for a digital certificate. The CA checks the school's identity or domain ownership and issues a certificate containing the school's public key. When users visit the website, their browser checks the CA signature and certificate details to authenticate the website.

---

### A government department considers quantum cryptography

> Quantum cryptography may be suitable because it can detect eavesdropping and offers very high security for sensitive data. However, it can be expensive, requires specialist equipment and may have distance limitations, so it may not be suitable for every network.

---

## Process Diagrams

### Private message using asymmetric cryptography

```mermaid
flowchart TD
A[Receiver creates public/private key pair] --> B[Receiver shares public key]
B --> C[Sender encrypts plaintext using receiver public key]
C --> D[Ciphertext sent over network]
D --> E[Receiver decrypts using receiver private key]
E --> F[Plaintext recovered]
```

### Digital signature process

```mermaid
flowchart TD
A[Sender writes message] --> B[Hash message]
B --> C[Encrypt hash with sender private key]
C --> D[Digital signature created]
D --> E[Message + signature sent]
E --> F[Receiver hashes received message]
E --> G[Receiver decrypts signature with sender public key]
F --> H{Hashes match?}
G --> H
H -->|Yes| I[Authentic and unchanged]
H -->|No| J[Invalid / altered]
```

### TLS simplified process

```mermaid
flowchart TD
A[Client requests HTTPS connection] --> B[Server sends digital certificate]
B --> C[Client validates certificate using CA]
C --> D[Client and server establish session key]
D --> E[Encrypted session begins]
E --> F[Data transferred securely]
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

1. Define plaintext and ciphertext. [2]  
2. State one difference between symmetric and asymmetric cryptography. [1]  
3. A user wants to send a private message to a company. Which key should be used to encrypt the message? [1]  
4. State two items that may be contained in a digital certificate. [2]  
5. Give one purpose of SSL/TLS. [1]  
6. Give one benefit of quantum cryptography. [1]  
7. Explain why a digital signature can show that a message has not been changed. [2]

## Quick Check Answers

1. Plaintext is the original readable message/data. Ciphertext is the encrypted unreadable message/data. [2]  
2. Symmetric uses one shared key; asymmetric uses a public/private key pair. [1]  
3. The company's / receiver's public key. [1]  
4. Any two: owner's identity/domain name, public key, issuer/CA, validity period, CA digital signature. [2]  
5. To provide secure encrypted client-server communication / authenticate a server / protect data integrity. [1]  
6. Eavesdropping can be detected / very high security / based on quantum properties. [1]  
7. The sender signs a hash of the message. The receiver recalculates the hash and compares it with the decrypted signature; if they match, the message has not changed. [2]

---

## 20-Mark Exam Practice

**Total: 20 marks**

### Question 1 — Asymmetric cryptography and private messages [5]

A hospital wants patients to send confidential medical information through a web portal.

Explain how asymmetric cryptography can be used so that only the hospital can read the message.

#### Mark scheme

One mark per point, max 5:

+ Hospital has a public/private key pair.  
+ The public key is made available to the patient / through a certificate.  
+ The patient encrypts the plaintext using the hospital's public key.  
+ The encrypted message / ciphertext is sent to the hospital.  
+ Only the hospital can decrypt it using the hospital's private key.  
+ The private key is kept secret by the hospital.  

---

### Question 2 — Symmetric vs asymmetric cryptography [4]

Compare symmetric key cryptography and asymmetric key cryptography.

#### Mark scheme

One mark per comparison, max 4:

+ Symmetric uses the same shared key for encryption and decryption, whereas asymmetric uses a public/private key pair.  
+ Symmetric is usually faster / more efficient, whereas asymmetric is slower / needs more processing.  
+ Symmetric has a key distribution problem, whereas asymmetric allows the public key to be shared openly.  
+ Symmetric requires both parties to know the shared secret key, whereas asymmetric requires the private key to be kept only by the owner.  
+ Symmetric is often used for bulk/session data, while asymmetric is often used for key exchange or digital signatures.  

---

### Question 3 — SSL/TLS [4]

A user logs in to an online banking website using HTTPS.

Explain how SSL/TLS helps protect the communication.

#### Mark scheme

One mark per point, max 4:

+ SSL/TLS provides secure client-server communication.  
+ The server sends a digital certificate / proves its identity.  
+ The certificate is checked using a Certificate Authority.  
+ A session key is established.  
+ Data is encrypted during transmission.  
+ It helps maintain data integrity / detect alteration.  
+ It protects confidential data such as login or transaction details.  

---

### Question 4 — Digital certificates and signatures [4]

Explain the difference between a digital certificate and a digital signature.

#### Mark scheme

One mark per point, max 4:

+ A digital certificate is an electronic document linking an entity's identity to its public key.  
+ It is issued / signed by a Certificate Authority.  
+ A digital signature is created using the sender's private key.  
+ A digital signature can verify the sender's identity.  
+ A digital signature can show that a message has not been altered.  
+ A certificate helps the receiver know which public key belongs to the sender/website.  

---

### Question 5 — Quantum cryptography [3]

State one benefit and two drawbacks of quantum cryptography.

#### Mark scheme

Max 3:

Benefit, one mark:

+ Eavesdropping can be detected because measuring quantum states changes them.  
+ Very secure / based on laws of physics rather than mathematical difficulty.  

Drawbacks, one mark each:

+ Expensive specialist equipment is required.  
+ Limited distance / not yet widely practical over long distances.  
+ Technology is still developing / not widely available.  
+ High error rate / affected by transmission conditions.  

---

## Final Revision Checklist

- I can define the required terms precisely.
- I can explain each process in the correct order.
- I can apply the ideas to an unfamiliar scenario.
- I can complete the 10-mark check without notes.
- I can complete and self-mark the 20-mark practice.
