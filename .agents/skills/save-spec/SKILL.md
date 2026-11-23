---
name: save-spec
description: Save the requirements and acceptance criteria from a completed, user-approved grill-me interview as a Markdown spec in the current project's spec/ folder. Use after the user confirms the interview outcome and asks to capture it; do not re-interview, plan implementation, or start coding.
---

# Save Spec

Turn an approved requirements discussion into one concise, reviewable specification file in the current project.

## Source of truth

- Use the decisions and requirements the user has already confirmed in the current conversation, especially the completed `grill-me` interview.
- Do not repeat the interview or reopen settled choices. Do not invent requirements to fill gaps.
- Preserve unresolved items as open questions. If an unresolved decision prevents a useful spec, state the gap and ask only for that decision.
- Inspect the project for an existing `spec/` folder and spec naming or formatting conventions. Follow those conventions when present.

## Write the spec

- Save the file under the current project's `spec/` directory. Create that directory if it does not exist.
- Use a short kebab-case filename based on the agreed feature name, such as `spec/export-reports.md`.
- Never overwrite an existing spec. If the proposed filename exists, choose the next available numbered filename unless it appears to be the same spec; in that case, ask whether to update it or create a separate document.
- Create only the spec file. Do not edit project code, plans, indexes, or other documents as part of this skill.
- Include the sections that fit the discussion:
  - **Purpose** — the user problem and desired outcome.
  - **Requirements** — agreed behaviors and constraints.
  - **Acceptance criteria** — observable conditions that show the requirements are met.
  - **Out of scope** — explicitly excluded work, when any was agreed.
  - **Open questions** — unresolved decisions, when any remain.
- Separate confirmed decisions from assumptions. Label any necessary inference and keep it minimal.
- Keep criteria testable and faithful to the user's wording. Do not add implementation choices that were not agreed or required by the project context.

## Finish

Report the created file path and summarize any open questions. Stop after saving the spec; do not invoke planning skills, create tickets, or implement the feature unless the user asks in a later step.
