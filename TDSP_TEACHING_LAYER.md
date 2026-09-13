# TDSP Teaching Layer

This layer preserves the official school syllabus. It reframes each session through a decision process:

Ask better questions -> organize evidence -> understand signals -> model carefully -> deploy decisions responsibly.

## Module 1 - Python for Data Science

| Session | Official topic | Hidden real objective | Business / product interpretation | Practical project connection |
|---|---|---|---|---|
| 1 | Introduction data science, notebooks, weak signals | Learn to turn vague curiosity into a decision question. | A signal matters only if it can change a product, marketing, or operational choice. | Choose a public signal and define the decision it could inform. |
| 2 | Pandas: cleaning, types, missing values | Learn how bad data creates bad decisions. | Duplicates, broken dates, and inconsistent categories distort dashboards and priorities. | Build a clean, auditable table from raw snapshots. |
| 3 | EDA, visualization, storytelling | Learn to separate visible patterns from useful evidence. | Charts should reduce uncertainty, not decorate a report. | Produce one visual story with one decision implication and one limitation. |
| 4 | Supervised ML: baseline and evaluation | Learn when prediction improves a decision and when it only adds noise. | A model is useful only if it beats a simple baseline and its errors are acceptable. | Build a baseline to predict or classify a relevant signal. |
| 5 | Unsupervised ML: clustering and dimensionality reduction | Learn how to detect structure when labels do not exist. | Segments and patterns are hypotheses for action, not automatic truths. | Identify groups, regimes, or periods in public signals. |
| 6 | Reproducible pipeline | Learn to make analysis repeatable enough to trust. | A result that cannot be rerun cannot support a recurring decision process. | Package cleaning, features, and outputs into a simple pipeline. |
| 7 | Guided project | Learn to manage ambiguity from question to evidence. | Real data projects succeed by narrowing scope and making assumptions explicit. | Build the final notebook, dataset, and decision memo. |
| 8 | Restitution | Learn to defend a recommendation with evidence and limits. | Stakeholders need the decision, the confidence level, and the risks. | Present findings as a product or business recommendation. |

## Module 2 - Advanced ML + MLOps

| Session | Official topic | Hidden real objective | Business / product interpretation | Practical project connection |
|---|---|---|---|---|
| 1 | ML reminders and advanced models | Learn why a stronger model is not automatically a better decision. | Complexity must earn its cost through better decisions, not better-looking metrics. | Compare baseline and advanced model on the same decision target. |
| 2 | Neural networks and basic architectures | Learn when representation learning is worth using. | Deep learning is useful when simpler models cannot capture the signal responsibly. | Train a small neural model and compare reliability, not only score. |
| 3 | Optimization and regularization | Learn to control overconfidence. | Overfit models create fragile product decisions. | Tune regularization and document trade-offs. |
| 4 | Evaluation, errors, generalization | Learn to inspect failure modes before deployment. | False positives and false negatives have different business costs. | Produce an error analysis table and deployment risk note. |
| 5 | Packaging and experiment tracking | Learn to make experiments traceable. | Teams cannot trust models when data, code, parameters, and results are disconnected. | Track model versions, metrics, and assumptions. |
| 6 | API or prediction demo | Learn to expose a model as a usable decision service. | Deployment is where model output meets workflow, latency, failure, and ownership. | Build a minimal local API or demo. |
| 7 | Technical documentation | Learn to transfer trust to another engineer or stakeholder. | Good documentation reduces operational risk. | Write model card, data card, and run instructions. |
| 8 | Project defense | Learn to justify deployment readiness. | The key question is not “does it work?” but “should we rely on it?” | Present model, errors, monitoring plan, and go/no-go recommendation. |

## Module 3 - NLP + Computer Vision

| Session | Official topic | Hidden real objective | Business / product interpretation | Practical project connection |
|---|---|---|---|---|
| 1 | Introduction NLP and classical methods | Learn how language becomes decision data. | Text contains intent, feedback, risk, and demand signals. | Convert text into measurable signals for a product question. |
| 2 | Embeddings and transformers | Learn how semantic similarity changes what teams can automate. | Embeddings enable search, routing, clustering, and recommendation. | Build a semantic retrieval or classification prototype. |
| 3 | BERT/GPT use cases | Learn to use pretrained models without surrendering evaluation. | Generative or transformer outputs need task-specific validation. | Build a text application with clear acceptance criteria. |
| 4 | Computer vision and CNNs | Learn how images become operational evidence. | Vision models support inspection, classification, detection, and quality control. | Build a simple image classifier or detector. |
| 5 | Pretrained vision models | Learn when transfer learning is enough. | Reusing models can reduce cost, but domain shift must be tested. | Fine-tune or evaluate a pretrained model on a practical task. |
| 6 | NLP / Vision application | Learn to connect model output to user workflow. | An AI feature is valuable only if the user can act on it. | Build an applied prototype with input, output, and feedback loop. |
| 7 | Evaluation and ethics | Learn to evaluate harm, bias, robustness, and misuse. | Responsible AI is deployment risk management. | Add evaluation, limits, and ethical analysis. |
| 8 | Project defense | Learn to present an intelligent application as a decision system. | The final artifact should be useful, testable, and honest. | Deliver demo, report, limitations, and portfolio asset. |

## Teaching rule

Every session starts with a decision problem, then introduces tools only as the way to improve that decision.
