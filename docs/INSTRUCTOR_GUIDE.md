# Instructor Guide

Goal: teach the official syllabus through a practical decision process, not as isolated tools.

## Use the official syllabus

- Keep the school syllabus as the compliance reference: session titles, expected skills, evaluation format, and project requirements.
- Use this repository as the delivery layer: notebooks, TDSP framing, project workflow, and publication assets.
- Do not present TDSP as a replacement for the syllabus. Present it as the teaching method used to make the syllabus operational.

## Teach through the TDSP layer

Use `TDSP_TEACHING_LAYER.md` before each class.

For every session, identify:
- the official topic;
- the decision problem behind the topic;
- the business or product interpretation;
- the project artifact students should improve.

Default sequence:
1. Ask the decision question.
2. Inspect the data or evidence.
3. Introduce only the tools needed for that decision.
4. Validate the result.
5. Translate the result into a recommendation, limitation, or next action.

## Start every session with a decision problem

Avoid starting with “today we learn pandas / clustering / pipelines.”

Start with:
- “How can bad data create bad decisions?”
- “What pattern is strong enough to change what we do next?”
- “When does a model improve a decision?”
- “How do we detect structure when labels do not exist?”
- “Can this workflow be trusted next month?”

This makes tools feel necessary rather than arbitrary.

## Use notebooks in class

Recommended classroom rhythm:
- 5 min: decision problem and expected deliverable.
- 10 min: inspect the dataset and risks.
- 25 min: guided notebook execution.
- 20 min: student modification or mini-challenge.
- 15 min: interpretation and limitations.
- 10 min: link to project deliverable.

Notebook rules:
- run top-to-bottom;
- keep outputs interpretable;
- require one written decision note;
- require one limitation;
- do not reward charts without interpretation.

## Connect exercises to projects

Each session should improve one project asset:
- clean dataset;
- EDA story;
- baseline model;
- error analysis;
- reproducible pipeline;
- deployment or monitoring note;
- final decision memo.

Students should see the final project as accumulated evidence, not a separate assignment.

## Evaluate students

Evaluate decision quality, not only code completion.

Suggested criteria:
- problem framing: clear decision question;
- data quality: cleaning choices documented and justified;
- analysis: charts and metrics answer the question;
- validation: baselines, errors, and limitations are explicit;
- reproducibility: notebook or pipeline runs end-to-end;
- communication: recommendation is understandable to a non-specialist;
- responsibility: risks, bias, and uncertainty are stated.

Strong submissions are simple, reproducible, and honest about limits.

Weak submissions may have complex code but unclear decisions, missing validation, or unsupported claims.
